import json
import requests
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('/home/JBalloonist/ynab/data/simple.ini')
TOKEN = parser.get('API', 'TOKEN')
BUDGET_ID = parser.get('API', 'BUDGET_ID')
URL = 'https://api.youneedabudget.com/v1/'

month = '2020-02-01'
category_id = '78bc9028-b0fb-4056-bc86-3b8ace523b92'
# r = requests.get('{}budgets/{}/categories?access_token={}'.format(URL, BUDGET_ID, TOKEN))
r = requests.get('{}budgets/{}/months/{}/categories/{}?access_token={}'.format(URL, BUDGET_ID, month, category_id, TOKEN))

print(r.status_code)
data = r.json()
with open('categories.json', 'w') as out:
    json.dump(data, out)