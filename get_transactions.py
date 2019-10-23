import json
import requests
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('simple.ini')
TOKEN = parser.get('API', 'TOKEN')
BUDGET_ID = parser.get('API', 'BUDGET_ID')
ACCOUNT_ID = parser.get('API', 'ACCOUNT_ID')
URL = 'https://api.youneedabudget.com/v1/'

date_since = '2019-10-01'
payload = {'type': 'uncategorized', 'since_date': date_since}
r = requests.get('{}budgets/{}/accounts/{}/transactions?access_token={}'.format(URL, BUDGET_ID, ACCOUNT_ID, TOKEN), params=payload)

print(r.status_code)
data = r.json()
with open('output.json', 'w') as out:
    json.dump(data, out)
