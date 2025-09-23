import os

from dotenv import load_dotenv

from parser.constants import (
    # AUCHAN_CLIENT_LOGINS,
    # CITILINK_CLIENT_LOGINS,
    EAPTEKA_CLIENT_LOGINS,
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

    date_list_direct = get_date_list(DAYS_TO_GENERATE_DIRECT)
    date_list_appmetrica = get_date_list(DAYS_TO_GENERATE_APPMETRICA)
    date_list_metrica = get_date_list(DAYS_TO_GENERATE_METRICA)

    # metrica = YandexMetricaReports(
    #     token_metrica,
    #     date_list_metrica,
    #     EAPTEKA_CLIENT_LOGINS
    # )

    # metrica._get_all_metrika_data()

    # direct = YandexDirectReports(
    #     token=token_direct,
    #     dates_list=date_list_direct,
    #     login=EAPTEKA_CLIENT_LOGINS
    # )
    # direct._get_all_direct_data()

    # appmetrica = YandexAppMetricaReports(
    #     token_appmetrica,
    #     date_list_appmetrica
    # )
    # appmetrica._get_all_appmetrica_data('2550202', 'test1.csv')


if __name__ == "__main__":
    main()
