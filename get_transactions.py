import configparser
import json
import requests
from pathlib import Path

path = Path.cwd().home() / 'ynab' / 'data' / 'simple.ini'
parser = configparser.ConfigParser()
parser.read([path])
TOKEN = parser.get('API', 'TOKEN')
BUDGET_ID = parser.get('API', 'BUDGET_ID')
# ACCOUNT_ID = parser.get('API', 'ACCOUNT_ID')
ACCOUNT_ID = 'a8b7ddf0-787a-4fe5-8431-bc93603741cb'
URL = 'https://api.youneedabudget.com/v1/'

date_since = '2020-01-20'
payload = {'type': 'uncategorized', 'since_date': date_since}
payload = {'flag': 'red', 'since_date': date_since}
r = requests.get('{}budgets/{}/accounts/{}/transactions?access_token={}'.format(URL, BUDGET_ID, ACCOUNT_ID, TOKEN), params=payload)
# r = requests.get('{}budgets/{}/transactions?access_token={}'.format(URL, BUDGET_ID, TOKEN), params=payload)

print(r.status_code)
data = r.json()
output = Path.cwd().home() / 'ynab' / 'data' / 'output.json'
with open(output, 'w') as out:
    json.dump(data, out)
