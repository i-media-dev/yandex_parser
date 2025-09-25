YANDEX_DIRECT_URL = 'https://api.direct.yandex.com/json/v5/reports'
"""URL для запроса отчета из Direct."""

YANDEX_METRICA_URL = 'https://api-metrika.yandex.net/stat/v1/data'
"""URL для запроса отчета из Metrica."""

YANDEX_APPMETRICA_URL = 'https://api.appmetrica.yandex.ru/stat/v1/data'
"""URL для запроса отчета из Appmetrica."""

DEFAULT_DELIMETER = '-'
"""Делиметр Campaign по умолчанию."""

DEFAULT_VALUE = '-all'
"""Значение для подставновки в пустые ячейки по умолчанию."""

DATE_FORMAT = '%Y-%m-%d'
"""Формат дат по умолчанию ('%Y-%m-%d')."""

REPORT_NAME = 'all_reports1'
"""Имя отчета по умолчанию."""

DEFAULT_FOLDER = 'data'
"""Папка для сохранения .csv файлов по умолчанию."""

DAYS_TO_GENERATE_DIRECT = 45
"""Количество дней для генерации списка дат по умолчанию."""

DAYS_TO_GENERATE_METRICA = 4
"""Количество дней для генерации списка дат по умолчанию."""

DAYS_TO_GENERATE_APPMETRICA = 1
"""Количество дней для генерации списка дат по умолчанию."""

DAYS_BEFORE = 7
"""Период в днях (7)."""

AUCHAN_M_ID = '24584168'
"""ID Ашан Метрика."""

EAPTEKA_M_ID = '22004554'
"""ID Еаптека Метрика."""

CITILINK_M_ID = '155462'
"""ID Ситилинк Метрика."""

AUCHAN_AM_ID = '4431094'
"""ID Ашан АппМетрика."""

EAPTEKA_AM_ID = '2550202'
"""ID Еаптека АппМетрика."""

CITILINK_AM_ID = '4309264'
"""ID Ситилинк АппМетрика."""

APPMETRICA_LIMIT = '1000'
"""Лимит выдачи отчета на страницу."""

METRICA_LIMIT = 10000
"""Лимит выдачи данных (10000)"""

DEFAULT_COLUMNS_CAMPAIGN = [
    'Geo',
    'Site_type',
    'Generation_method',
    'Category',
    'Subject',
    'Url_type'
]
"""Поля для разбивки Campaign."""

REPORT_FIELDS_DIRECT = [
    "Date",
    "CampaignName",
    "CampaignId",
    "Device",
    "Impressions",
    "Clicks",
    "Cost"
]
"""Запрашиваемые поля для Яндекс Директ."""

REPORT_FIELDS_APPMETRICA = [
    'Date',
    'CampaignName',
    'Transactions',
    'Revenue'
]
"""Запрашиваемые поля для Яндекс Аппметрики."""

REPORT_FIELDS_METRICA = [
    'Date',
    'CampaignName',
    'Device',
    'Transactions',
    'Revenue'
]
"""Запрашиваемые поля для Яндекс Аппметрики."""

AUCHAN_CLIENT_LOGINS = []
"""Список логинов Ашан."""

CITILINK_CLIENT_LOGINS = [
    'citilink-nvsb', 'imedia-citilinkweb',
    'imedia-citilink2', 'imedia-citilink-blg',
    'imedia-citilink-cat', 'imedia-citilink-chb',
    'imedia-citilink-chlb', 'imedia-citilink-ekb',
    'imedia-citilink-generator', 'imedia-citilink-ivn',
    'imedia-citilink-izh', 'imedia-citilink-krasn',
    'imedia-citilink-krd', 'imedia-citilink-kronar',
    'imedia-citilink-kvs', 'imedia-citilink-kzn',
    'imedia-citilink-lip', 'imedia-citilink-mgn',
    'imedia-citilink-nch', 'imedia-citilink-new',
    'imedia-citilink-newreg', 'imedia-citilink-nnov',
    'imedia-citilink-nz', 'imedia-citilink-penza',
    'imedia-citilink-performans', 'imedia-citilink-perm',
    'imedia-citilink-rnd', 'imedia-citilink-smr',
    'imedia-citilink-spb', 'imedia-citilink-srt',
    'imedia-citilink-stav', 'imedia-citilink-tlt',
    'imedia-citilink-tmn', 'imedia-citilink-tula',
    'imedia-citilink-vendor', 'imedia-citilink-vlg',
    'imedia-citilink-vlzh', 'imedia-citilink-vrnzh',
    'imedia-citilink-yar', 'imedia-kcitilink',
    'citilink-nz-dsa-msk', 'citilink-brand',
    'citilink-nz-dsa-spb', 'citilink-nz-dsa-ekat',
    'citilink-nz-dsa-nnov', 'citilink-nz-dsa-smr',
    'citilink-nz-dsa-omk', 'citilink-nz-dsa-kzn',
    'citilink-nz-dsa-rnd', 'citilink-nz-dsa-ufa',
    'citilink-nz-dsa-vlg', 'citilink-nz-dsa-perm',
    'citilink-nz-dsa-krasn', 'citilink-nz-dsa-vrzh',
    'citilink-nz-dsa-srt', 'citilink-nz-dsa-krd',
    'citilink-nz-dsa-segm1', 'citilink-nz-dsa-segm2',
    'citilink-nz-dsa-segm3', 'citilink-nz-dsa-segm4',
    'citilink-nz-dsa-segm5', 'citilink-nz-dsa-segm6',
    'citilink-nz-dsa-segm7', 'citilink-nz-dsa-segm8',
    'citilink-category-msk', 'citilink-category-spb',
    'citilink-category-ekat', 'citilink-category-nnov',
    'citilink-category-smr', 'citilink-category-omk',
    'citilink-category-kzn', 'citilink-category-rnd',
    'citilink-category-ufa', 'citilink-category-vlg',
    'citilink-category-perm', 'citilink-category-krasn',
    'citilink-category-vrzh', 'citilink-category-srt',
    'citilink-category-krd', 'citilink-category-segm1',
    'citilink-category-segm2', 'citilink-category-segm3',
    'citilink-category-segm4', 'citilink-category-segm5',
    'citilink-category-segm6', 'citilink-category-segm7',
    'citilink-category-segm8', 'citilink-cv-msk',
    'citilink-cv-spb', 'citilink-cv-ekat',
    'citilink-cv-nnov', 'citilink-cv-smr',
    'citilink-cv-rnd', 'citilink-cv-omk',
    'citilink-cv-kzn', 'citilink-cv-ufa',
    'citilink-cv-vlg', 'citilink-cv-perm',
    'citilink-cv-krasn', 'citilink-cv-vrzh',
    'citilink-cv-srt', 'citilink-cv-krd',
    'citilink-cv-segm4', 'citilink-cv-segm3',
    'citilink-cv-segm2', 'citilink-cv-segm1',
    'citilink-cv-segm8', 'citilink-cv-segm7',
    'citilink-cv-segm6', 'citilink-cv-segm5',
    'citilink-cv-segm9', 'citilink-category-segm9',
    'citilink-nz-dsa-segm9', 'citilink-category-segm10',
    'citilink-nz-dsa-segm10', 'citilink-cv-tmsk',
    'citilink-category-tmsk', 'citilink-nz-dsa-tmsk',
    'citilink-cv-segm10', 'citilink-nz-dsa-irk',
    'citilink-nz-dsa-nvsb', 'citilink-category-nvsb',
    'citilink-cv-nvsb', 'citilink-nz-dsa-chlb',
    'citilink-category-chlb', 'citilink-cv-chlb',
    'citilink-cv-irk', 'citilink-category-irk',
    'citilink-sportzoo', 'imedia-citilink-vendor-1c',
    'imedia-citilink-vendor-huawei', 'imedia-citilink-vendor-xiaomi',
    'imedia-citilink-vendor-acer', 'imedia-citilink-vendor-kitfort',
    'imedia-citilink-vendor-sber', 'imedia-citilink-vendor-tefal',
    'imedia-citilink-vendor-tangem', 'imedia-citilink-vendor-hiper',
    'imedia-citilink-vendor-reg', 'imedia-citilink-reg-cpm',
    'imedia-citilink-ezviz', 'imedia-citilink-vendor-xpg',
    'imedia-citilink-jurnal', 'imedia-citilink-vendor-msi',
    'imedia-citilink-vendor-bosch', 'imedia-citilink-vendor-basealt',
    'imedia-citilink-vendor-polaris', 'imedia-citilink-vendor-wisenet',
    'imedia-citilink-vendor-micros', 'imedia-citilink-vendor-samsung',
    'imedia-citilink-vendor-philips', 'imedia-citilink-vendor-itel',
    'imedia-citilink-vendor-tefal-v', 'imedia-citilink-vendor-tcl',
    'imedia-citilink-vendor-polar-v', 'imedia-citilink-xiaomi-v',
    'imedia-citilink-vendor-haier', 'imedia-citilink-vendor-tecno',
    'imedia-citilink-vendor-infocus', 'imedia-citilink-vendor-makita',
    'imedia-citilink-vendor-xiao-v2', 'imedia-citilink-vendor-ventura',
    'imedia-citilink-vndr-samsung-y', 'imedia-citilink-vendor-beko',
    'imedia-citilink-vendor-elikor', 'imedia-citilink-vendor-gg',
    'imedia-citilink-vendor-haier-v', 'imedia-citilink-vendor-hotpoin',
    'imedia-citilink-vendor-kvadra', 'imedia-citilink-vendor-lex',
    'imedia-citilink-vendor-xgimi', 'imedia-citilink-vendor-gigabyt',
    'porg-5gi7f4um', 'porg-5yb5r4kg', 'porg-u3ymtw4n'

]
"""Список логинов Ситилинк."""

EAPTEKA_CLIENT_LOGINS = [
    'imedia-eapteka',
]
"""Список логинов Еаптека."""


DEVICES = {
    'PC': 'DESKTOP',
    'Smartphones': 'MOBILE',
    'TV': 'SMART_TV',
    'Tablets': 'TABLET'
}
"""Словарь стандаритизации значений колонки Device"""

CLIENT_INFO = {
    # 'auchan': (AUCHAN_CLIENT_LOGINS, AUCHAN_M_ID, AUCHAN_AM_ID),
    # 'citilink': (CITILINK_CLIENT_LOGINS, CITILINK_M_ID, CITILINK_AM_ID),
    'eapteka': (EAPTEKA_CLIENT_LOGINS, EAPTEKA_M_ID, EAPTEKA_AM_ID)
}
"""Словарь сгруппированной информации по клиентам."""
