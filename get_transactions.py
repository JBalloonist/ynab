#!/usr/bin/python3.6

import json
import configparser
import requests
from pathlib import Path
# from helpers import get_account_id

path = Path.cwd().home() / 'ynab' / 'data' / 'simple.ini'
parser = configparser.ConfigParser()
parser.read([path])
TOKEN = parser.get('API', 'TOKEN')
BUDGET_ID = parser.get('API', 'BUDGET_ID')
# ACCOUNT_ID = parser.get('API', 'ACCOUNT_ID')
# ACCOUNT_ID = 'd9d9c545-b754-49af-87ac-cc9991df9224'
# ACCOUNT_ID = get_account_id()
ACCOUNT_ID = '77420872-399a-471e-a9a8-f328addfaab7'
URL = 'https://api.youneedabudget.com/v1/'

date_since = '2021-09-01'
payload = {'type': 'uncategorized', 'since_date': date_since}
payload = {'since_date': date_since}
r = requests.get('{}budgets/{}/accounts/{}/transactions?access_token={}'.format(URL, BUDGET_ID, ACCOUNT_ID, TOKEN), params=payload)
# r = requests.get('{}budgets/{}/transactions?access_token={}'.format(URL, BUDGET_ID, TOKEN), params=payload)

print(r.status_code)
data = r.json()
output = Path.cwd().home() / 'ynab' / 'data' / 'transactions.json'
with open(output, 'w') as out:
    json.dump(data, out)
