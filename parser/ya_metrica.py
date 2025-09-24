# from datetime as dt
import logging

from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
import requests

from parser.logging_config import setup_logging
from parser.constants import (
    DEFAULT_FOLDER,
    YANDEX_METRICA_URL,
    METRICA_LIMIT,
    REPORT_FIELDS_METRICA,
    DEFAULT_COLUMNS_CAMPAIGN,
    DEFAULT_DELIMETER,
    DEFAULT_VALUE,
    DEVICES
)

setup_logging()
load_dotenv()


class YandexMetricaReports:
    """Класс для получения и сохранения данных отчетов из Яндекс.Метрики."""

    def __init__(
        self,
        token: str,
        dates_list: list,
        login: list,
        counter_id: str,
        report_fields: list = REPORT_FIELDS_METRICA,
        columns: list = DEFAULT_COLUMNS_CAMPAIGN,
        folder_name: str = DEFAULT_FOLDER,
        limit: int = METRICA_LIMIT
    ):
        if not token:
            logging.error('Токен отсутствует или не действителен')
        self.token = token
        self.logins = login
        self.report_fields = report_fields
        self.columns = columns
        self.dates_list = dates_list
        self.counter_id = counter_id
        self.folder = folder_name
        self.limit = limit

    def _split_campaign(
        self,
        column,
        default_value: str = DEFAULT_VALUE,
        delimeter: str = DEFAULT_DELIMETER
    ):
        df = pd.DataFrame()

        for i, value in enumerate(self.columns):
            df[value] = column.apply(
                lambda x: (
                    str(x) + default_value *
                    ((len(self.columns)-1)-str(x).count(delimeter))
                ).split('-', len(self.columns)-1)[i]
            )
        return df

    def _rename_columns(self, df):
        df['Devices'] = df['Device'].apply(lambda x: DEVICES.get(x))
        del df['Device']
        df.rename(columns={'Devices': 'Device'}, inplace=True)
        return df

    def _get_file_path(self, filename: str) -> Path:
        """Защищенный метод. Создает путь к файлу в указанной папке."""
        try:
            file_path = Path(__file__).parent.parent / self.folder
            file_path.mkdir(parents=True, exist_ok=True)
            return file_path / filename
        except Exception as e:
            logging.error(f'Ошибка: {e}')
            raise

    def _get_metrica_reports(self):
        """Получаем данные из Метрики."""
        start_date = self.dates_list[0]
        end_date = self.dates_list[-1]
        url = YANDEX_METRICA_URL
        headers = {
            "Authorization": f"OAuth {self.token}"
        }
        params = {
            "ids": self.counter_id,
            "metrics": "ym:s:ecommercePurchases,ym:s:ecommerceRevenue",
            "dimensions": "ym:s:date,ym:s:lastsignDirectClickOrder, "
            "ym:s:DeviceCategory",
            "date1": start_date,
            "date2": end_date,
            "accuracy": "full",
            "limit": self.limit
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == requests.codes.ok:
                data = response.json()

                if not data or 'data' not in data or not data['data']:
                    logging.warning('Нет данных для кампании ')
                    return []

                return data['data']
            else:
                logging.error(f'Ошибка API: {response.status_code}')
                return []
        except Exception as e:
            logging.error(f'Ошибка: {e}')
            return []

    def _get_all_metrika_data(self):
        result = []
        data = self._get_metrica_reports()

        for i in data:
            if '-' in str(i['dimensions'][1]['name']):
                result.append(
                    [
                        i['dimensions'][0]['name'],
                        i['dimensions'][1]['name'].split('|')[0],
                        i['dimensions'][2]['name'],
                        int(i['metrics'][0]),
                        int(float(i['metrics'][1]))
                    ]
                )

        df = pd.DataFrame(result, columns=self.report_fields)
        campaign_parts = self._split_campaign(df['CampaignName'])
        df = pd.concat([df, campaign_parts], axis=1)
        df = self._rename_columns(df)
        return df

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
                old_df = old_df[~old_df['Date'].fillna('').str.contains(
                    fr'{dates}', case=False, na=False
                )]
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
        df_new = self._get_all_metrika_data()
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
                    fr'{dates}', case=False, na=False
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
