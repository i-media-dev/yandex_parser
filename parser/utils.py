import datetime as dt

from parser.constants import DATE_FORMAT


def get_date_list(
    days_int: int,
    stop_int: int = 0,
    step_int: int = 1
) -> list[str]:
    """Функция генерирует список дат за указанное количество дней."""
    dates_list = []

    for i in range(days_int, stop_int, step_int):
        tempday = dt.datetime.now()
        tempday -= dt.timedelta(days=i)
        tempday_str = tempday.strftime(DATE_FORMAT)
        dates_list.append(tempday_str)
    return dates_list
