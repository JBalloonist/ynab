#!/usr/bin/python3.6

import json
import requests
import configparser
from pathlib import Path

PATH = Path.home() / 'ynab' / 'data'
parser = configparser.ConfigParser()
parser.read([PATH / 'simple.ini'])
TOKEN = parser.get('API', 'TOKEN')
BUDGET_ID = parser.get('API', 'BUDGET_ID')
URL = 'https://api.youneedabudget.com/v1/'

month = '2022-02-01'
category_id = '78bc9028-b0fb-4056-bc86-3b8ace523b92'
r = requests.get('{}budgets/{}/categories?access_token={}'.format(URL, BUDGET_ID, TOKEN))
# r = requests.get('{}budgets/{}/months/{}/categories/{}?access_token={}'.format(URL, BUDGET_ID, month, category_id, TOKEN))

print(r.status_code)
data = r.json()
with open(PATH / 'categories.json', 'w') as out:
    json.dump(data, out)