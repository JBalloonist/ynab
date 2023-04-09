import json
import requests
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('simple.ini')
TOKEN = parser.get('API', 'TOKEN')
BUDGET_ID = parser.get('API', 'BUDGET_ID')
ACCOUNT_ID = parser.get('API', 'ACCOUNT_ID')
URL = 'https://api.youneedabudget.com/v1/'

r = requests.get('{}budgets?access_token={}'.format(URL, TOKEN))
data = r.json()
with open('budget_output.json', 'w') as out:
    json.dump(data, out)
