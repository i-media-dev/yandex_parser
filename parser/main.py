import os

from dotenv import load_dotenv

from parser.constants import (
    # AUCHAN_CLIENT_LOGINS,
    # CITILINK_CLIENT_LOGINS,
    EAPTEKA_CLIENT_LOGINS,
    # AUCHAN_ID,
    # CITILINK_ID,
    EAPTEKA_ID,
    DAYS_TO_GENERATE_APPMETRICA,
    DAYS_TO_GENERATE_DIRECT,
    DAYS_TO_GENERATE_METRICA,
)
from parser.decorators import time_of_script
from parser.ya_direct import YandexDirectReports
from parser.ya_appmetrica import YandexAppMetricaReports
from parser.ya_metrica import YandexMetricaReports
from parser.utils import get_date_list

load_dotenv()


@time_of_script
def main():
    """Основная логика скрипта."""
    token_direct = str(os.getenv('YANDEX_DIRECT_TOKEN'))
    token_metrica = str(os.getenv('YANDEX_METRICA_TOKEN'))
    token_appmetrica = str(os.getenv('YANDEX_APPMETRICA_TOKEN'))

    date_list_direct = get_date_list(DAYS_TO_GENERATE_DIRECT, 0, -1)
    date_list_appmetrica = get_date_list(DAYS_TO_GENERATE_APPMETRICA, 2)
    date_list_metrica = get_date_list(DAYS_TO_GENERATE_METRICA, 0, -1)

    metrica = YandexMetricaReports(
        token=token_metrica,
        dates_list=date_list_metrica,
        login=EAPTEKA_CLIENT_LOGINS,
        counter_id=EAPTEKA_ID
    )

    direct = YandexDirectReports(
        token=token_direct,
        dates_list=date_list_direct,
        login=EAPTEKA_CLIENT_LOGINS
    )

    appmetrica = YandexAppMetricaReports(
        token=token_appmetrica,
        dates_list=date_list_appmetrica
    )

    direct.save_data('eapteka_direct.csv')
    metrica.save_data('eapteka_metrica.csv')
    appmetrica.save_data(
        shop_id=EAPTEKA_ID,
        filename_temp='eapteka_direct.csv',
        filename_data='eapteka_appmetrica.csv'
    )


if __name__ == "__main__":
    main()
