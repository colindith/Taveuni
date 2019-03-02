import requests
from django.utils import timezone
from taveuni.celery import app

FIELDS_LOOKUP = {
    '指數': {
        '指數': 'index_name',
        '收盤指數': 'close',
        '漲跌': 'delta'
    },
    '證券代號': {

    }
}

#### TWSE 每日收盤行情 ###
def daily_close_price(date=None):
    if not date:
        date_str = timezone.localtime().strftime('%y%m%d')
    else:
        date_str = date.strftime('%y%m%d')
    url = f'http://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date={date_str}&type=ALL&_=1551526602562'
    data = requests.get(url)

    #parse the data according to different json structure
    data = data.json()
    for i in range(1, 6):
        # '指數', '報酬指數', '成交統計', '類型', '證券代號'
        fields = data.get(f'fields{i}')
        if fields[0] == '指數':
            pass


@app.task()
def crawler():
    pass