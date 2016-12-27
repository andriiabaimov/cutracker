import os

UKRPOSHTA_ID = os.getenv('UKRPOSHTA_ID')
UKRPOSHTA_URL = 'http://services.ukrposhta.ua/bardcodesingle/Default.aspx'
UKRPOSHTA_FIELD_ID = 'ctl00_centerContent_txtBarcode'
UKRPOSHTA_ANSWER_ID = 'ctl00_centerContent_divInfo'
UKRPOSHTA_TIME_ID = 'ctl00_centerContent_lblDate'
UKRPOSHTA_WAIT = 10
UKRPOSHTA_FAIL = 'Ukrposhta goes out to smoke, waiting...'

POSHTASTAT_ID = os.getenv('POSHTASTAT_ID')
POSHTASTAT_SEARCH_STRING = 'Надійшло у ММПО України (імпорт)'
POSHTASTAT_LAST_UPDATE = 'Останнє оновлення'
POSHTASTAT_URL = '{}/{}'.format('https://poshta-stat.tk/track/', POSHTASTAT_ID)
POSHTASTAT_FAIL = 'Poshtastat goes out to smoke, waiting...'
POSHTASTAT_NO_IMPORT = 'Poshtastat says there is no import'
POSHTASTAT_IMPORT = 'Poshtastat tracked import on '

PHANTOMJS_PATH = os.getenv('PHANTOMJS_PATH')

REQUEST_EVERY_SECONDS = 300