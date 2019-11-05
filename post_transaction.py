#!/usr/bin/python3.6

import configparser
import requests
import pandas as pd
from datetime import datetime, timedelta

now = datetime.now()
PATH = '/home/JBalloonist/ynab/'
parser = configparser.ConfigParser()
parser.read(PATH + 'simple.ini')
TOKEN = parser.get('API', 'TOKEN')
BUDGET_ID = parser.get('API', 'BUDGET_ID')
ACCOUNT_ID = parser.get('API', 'ACCOUNT_ID')
URL = 'https://api.youneedabudget.com/v1/'
fmt = '%Y-%m-%d'


def post_trans(payload):
    url = '{}budgets/{}/transactions?access_token={}'.format(URL, BUDGET_ID, TOKEN)
    r = requests.post(url, json=payload)
    print('')
    print(r.status_code)
    print('')


def amortization_parser(file, add_days, sub_days):
    df = pd.read_csv(file)
    df.date = pd.to_datetime(df.date)

    plus_day = now + timedelta(days=add_days)
    minus_day = now - timedelta(days=sub_days)
    print(minus_day)
    print(plus_day)

    keep = df.loc[(df.date > plus_day)].copy()
    print('Data to keep from {}: '.format(file))
    print(keep.head())
    keep.to_csv(file, index=False)

    trans = df.loc[(df.date < plus_day) & (df.date > minus_day)].copy()
    return trans


def create_ynab_trans(trans):
    trans.date = trans.date.dt.strftime(fmt)
    trans_dict = trans.T.to_dict()
    trans = trans_dict[0]
    payload = {'transaction': trans}
    post_trans(payload)


create_ynab_trans(amortization_parser(PATH + 'loop.csv', 1, 1))
create_ynab_trans(amortization_parser(PATH + 'cudgel.csv', 1, 1))

sheets = ['Cornerstone-{}.csv'.format(i) for i in range(1, 7)]
sheets.pop(2)

for i in sheets:
    try:
        create_ynab_trans(amortization_parser(PATH + i, 1, 1))
    except:
        pass
