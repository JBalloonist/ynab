#!/usr/bin/python3.6

import sys
import configparser
import requests
import pandas as pd
from datetime import datetime, timedelta

now = datetime.now()
path = '/home/JBalloonist/ynab/'

parser = configparser.ConfigParser()
parser.read(path + 'simple.ini')
TOKEN = parser.get('API', 'TOKEN')
BUDGET_ID = parser.get('API', 'BUDGET_ID')
ACCOUNT_ID = parser.get('API', 'ACCOUNT_ID')
URL = 'https://api.youneedabudget.com/v1/'

payload = {'transaction': {'date': '2019-10-21',
  'payee': 'Union Savings Bank',
  'amount': 226150,
  'cleared': 'cleared',
  'account_id': 'e51c95d2-209a-4a30-9384-09b91863dff7'}}

df = pd.read_csv(path + 'loop.csv')
df.date = pd.to_datetime(df.date)
df.amount = df.amount *1000
df.amount = df.amount.astype('int64')

plus_day = now + timedelta(days=2)
minus_day = now - timedelta(days=2)
print(minus_day)
print(plus_day)
trans1 = df.loc[(df.date < plus_day) & (df.date > minus_day)].copy()
keep = df.loc[(df.date > plus_day)].copy()
fmt = '%Y-%m-%d'
trans1.date = trans1.date.dt.strftime(fmt)
trans_dict = trans1.T.to_dict()
trans1 = trans_dict[0]
payload = {'transaction': trans1}

url = '{}budgets/{}/transactions?access_token={}'.format(URL, BUDGET_ID, TOKEN)
r = requests.post(url, json=payload)
print('')
print(r.status_code)
print('')
print(r.text)
print('')
print(r.request.body)

keep.to_csv(path + 'loop.csv', index=False)



