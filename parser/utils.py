import datetime as dt
import pandas as pd

from parser.constants import DATE_FORMAT


def get_date_list(days_int) -> list[str]:
    """Функция генерирует список дат за указанное количество дней."""
    dates_list = []

    # for i in range(days_int, 0, -1):
    for i in range(days_int, 2):
        tempday = dt.datetime.now()
        tempday -= dt.timedelta(days=i)
        tempday_str = tempday.strftime(DATE_FORMAT)
        dates_list.append(tempday_str)
    return dates_list
