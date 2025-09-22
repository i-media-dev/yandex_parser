import io
import json
import logging
import time
from typing import Any
from pathlib import Path

from dotenv import load_dotenv
import pandas as pd
import requests

from parser.constants import (
    # CAMPAIGN_CATEGORIES,
    DEFAULT_FOLDER,
    # DEFAULT_RETURNES,
    # PLATFORM_TYPES,
    DEFAULT_COLUMNS_CAMPAIGN,
    REPORT_FIELDS_DIRECT,
    REPORT_NAME,
    YANDEX_DIRECT_URL
)
from parser.logging_config import setup_logging

load_dotenv()
setup_logging()


class DirectSaveClient:
    """Класс для получения и сохранения данных отчетов из Яндекс.Директ."""

    def __init__(
        self,
        token: str,
        dates_list: list,
        login: list,
        columns: list = DEFAULT_COLUMNS_CAMPAIGN,
        folder_name: str = DEFAULT_FOLDER
    ):
        if not token:
            logging.error('Токен отсутствует или не действителен')
        self.token = token
        self.logins = login
        self.dates_list = dates_list
        self.folder = folder_name
        self.columns = columns

    def _split_campaign(self, column):
        df = pd.DataFrame()

        for i, value in enumerate(self.columns):
            df[value] = column.apply(
                lambda x: (
                    str(x) + '-all'*((len(self.columns)-1)-str(x).count('-'))
                ).split('-', len(self.columns)-1)[i]
            )
        return df

    def _decode_if_bytes(self, x: Any) -> Any:
        """
        Защищенный метод. Декодирует байтовую строку в UTF-8,
        если передан bytes.
        """
        if type(x) is type(b''):
            return x.decode('utf8')
        else:
            return x

    def _get_file_path(self, filename: str) -> Path:
        """Защищенный метод. Создает путь к файлу в указанной папке."""
        try:
            file_path = Path(__file__).parent.parent / self.folder
            file_path.mkdir(parents=True, exist_ok=True)
            return file_path / filename
        except Exception as e:
            logging.error(f'Ошибка: {e}')
            raise

    def _get_direct_report(
        self,
        login: str,
        date_from: str,
        date_to: str
    ) -> str:
        """
        Защищенный метод.
        Получает отчет из Яндекс.Директ для указанного логина и периода.
        """

        headers = {
            "Authorization": "Bearer " + self.token,
            "Client-Login": login,
            "Accept-Language": "ru",
            "processingMode": "auto"
        }

        body = {
            "params": {
                "SelectionCriteria": {
                    "DateFrom": date_from,
                    "DateTo": date_to
                },
                "FieldNames": REPORT_FIELDS_DIRECT[0],
                "ReportName": REPORT_NAME,
                "ReportType": "CUSTOM_REPORT",
                "DateRangeType": "CUSTOM_DATE",
                "Format": "TSV",
                "IncludeVAT": "NO",
                "IncludeDiscount": "NO"
            }
        }

        body = json.dumps(body, indent=4)

        while True:
            try:
                response = requests.post(
                    YANDEX_DIRECT_URL,
                    body,
                    headers=headers
                )
                response.encoding = 'utf-8'

                if response.status_code == requests.codes.bad_request:

                    logging.error(
                        'Параметры запроса указаны неверно или достигнут '
                        'лимит отчетов в очереди\n'
                        'RequestId: '
                        f'{response.headers.get('RequestId', None)}\n'
                        f'JSON-код запроса: {self._decode_if_bytes(body)}\n'
                        'JSON-код ответа сервера: '
                        f'{self._decode_if_bytes(response.json())}'
                    )
                    break
                elif response.status_code == requests.codes.ok:
                    logging.info('Ответ успешно получен')
                    break
                elif response.status_code == requests.codes.created:
                    retryIn = int(response.headers.get('retryIn', 60))
                    logging.warning('Отчет еще создается')
                    time.sleep(retryIn)
                elif response.status_code == requests.codes.accepted:
                    retryIn = int(response.headers.get('retryIn', 60))
                    logging.warning('Отчет еще создается')
                    time.sleep(retryIn)
                elif response.status_code == \
                        requests.codes.internal_server_error:
                    logging.error(
                        'Ошибка. Повторить запрос позднее.\n'
                        'RequestId: '
                        f'{response.headers.get('RequestId', None)}\n'
                        'JSON-код ответа сервера: '
                        f'{self._decode_if_bytes(response.json())}'
                    )
                    break
                elif response.status_code == requests.codes.bad_gateway:
                    logging.error(
                        'Время формирования отчета превышено. '
                        'Изменить параметры запроса.\n'
                        'RequestId: '
                        f'{response.headers.get('RequestId', None)}\n'
                        f'JSON-код запроса: {self._decode_if_bytes(body)}\n'
                        'JSON-код ответа сервера: '
                        f'{self._decode_if_bytes(response.json())}'
                    )
                    break
                else:
                    logging.error(
                        'Произошла непредвиденная ошибка.\n'
                        'RequestId: '
                        f'{response.headers.get('RequestId', None)}\n'
                        f'JSON-код запроса: {self._decode_if_bytes(body)}\n'
                        'JSON-код ответа сервера: '
                        f'{self._decode_if_bytes(response.json())}'
                    )
                    break

            except requests.exceptions.ConnectionError:
                logging.error('Произошла ошибка соединения с сервером API')
                break

            except Exception as e:
                logging.error(f'ошибка: {e}')
                break

        return response.text

    def _get_all_direct_data(self) -> pd.DataFrame:
        """Метод получает данные из Яндекс.Директ для всех клиентов."""
        data_frames = []

        for i, login in enumerate(self.logins, 1):
            try:
                logging.info(
                    f'Выгрузка {i}/{len(self.logins)}, аккаунт: {login}')
                data = self._get_direct_report(
                    login,
                    self.dates_list[0],
                    self.dates_list[-1]
                )
                df = pd.read_csv(
                    io.StringIO(data),
                    sep='\t',
                    encoding='cp1251',
                    header=1
                )
                df['Account'] = login
                campaign_parts = self._split_campaign(df['CampaignName'])
                df = pd.concat([df, campaign_parts], axis=1)
                data_frames.append(df)

                time.sleep(1)

            except Exception as e:
                logging.error(f'Ошибка в аккаунте {login}: {e}')
                continue

        if not data_frames:
            return pd.DataFrame()

        data = pd.concat(data_frames, ignore_index=True)
        temp_cache_path = self._get_file_path('test1.csv')
        data['Source'] = 'yandex'
        data['Cost'] = data['Cost'] * 1.2 / 1000000
        data = data[~data['Date'].str.contains(
            'Total',
            case=False,
            na=False
        )]
        data.to_csv(
            temp_cache_path,
            index=False,
            header=True,
            sep=';',
            encoding='utf-8'
        )
        return data

    def _get_filtered_cache_data(self, filename_data: str) -> pd.DataFrame:
        """Метод получает отфильтрованные данные из кэш-файла."""
        temp_cache_path = self._get_file_path(filename_data)
        try:
            old_df = pd.read_csv(
                temp_cache_path,
                sep=';',
                encoding='cp1251',
                header=0
            )
            for dates in self.dates_list:
                old_df = old_df[
                    ~old_df['Date'].fillna('').str.contains(
                        fr'{dates}',
                        case=False,
                        na=False
                    )
                ]

            return old_df
        except FileNotFoundError:
            logging.warning('Файл кэша не найден. Первый запуск.')
            return pd.DataFrame()
        except pd.errors.EmptyDataError:
            logging.warning('Файл кэша пустой.')
            return pd.DataFrame()
        except Exception as e:
            logging.error(f'Ошибка: {e}')
            raise

    def save_data(self, filename_data: str) -> None:
        """Метод сохраняет новые данные, объединяя с существующими."""
        df_new = self._get_all_direct_data()
        df_old = self._get_filtered_cache_data(filename_data)
        try:
            temp_cache_path = self._get_file_path(filename_data)
            if df_new.empty:
                logging.warning('Нет новых данных для сохранения')
                return
            if not isinstance(df_old, pd.DataFrame) or df_old.empty:
                df_new.to_csv(
                    temp_cache_path,
                    index=False,
                    header=True,
                    sep=';',
                    encoding='cp1251'
                )
                logging.info(
                    'Новые данные сохранены. Исторические данные отсутствовали'
                )
                return
            for dates in self.dates_list:
                df_old = df_old[~df_old['Date'].fillna('').str.contains(
                    fr'{dates}',
                    case=False,
                    na=False
                )]

            df_old = pd.concat([df_new, df_old])
            df_old.to_csv(
                temp_cache_path,
                index=False,
                header=True,
                sep=';',
                encoding='cp1251'
            )
            logging.info('Данные успешно обновлены')
        except Exception as e:
            logging.error(f'Ошибка во время обновления: {e}')
