import datetime as dt
import pandas as pd

from parser.constants import DATE_FORMAT


def get_date_list(days_int) -> list[str]:
    """Функция генерирует список дат за указанное количество дней."""
    dates_list = []

    for i in range(days_int, 0, -1):
        tempday = dt.datetime.now()
        tempday -= dt.timedelta(days=i)
        tempday_str = tempday.strftime(DATE_FORMAT)
        dates_list.append(tempday_str)
    return dates_list


def _split_campaign(column):
    with open(
        'prod/eapteka_campaign.txt',
        'r',
        encoding='utf-8'
    ) as file:
        campaign_list = [line.strip() for line in file]

    df = pd.DataFrame({'campaign': campaign_list})

    for i, value in enumerate(column):
        df[value] = df['campaign'].apply(
            lambda x: (
                x + '-+all+'*((len(column)-1)-x.count('-'))
            ).split('-', len(column)-1)[i]
        )
    return df
