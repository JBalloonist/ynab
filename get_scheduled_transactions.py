import json
import requests
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('simple.ini')
TOKEN = parser.get('API', 'TOKEN')
BUDGET_ID = parser.get('API', 'BUDGET_ID')
URL = 'https://api.youneedabudget.com/v1/'

r = requests.get('{}budgets/{}/scheduled_transactions?access_token={}'.format(URL, BUDGET_ID, TOKEN))

print(r.status_code)
data = r.json()
with open('output.json', 'w') as out:
    json.dump(data, out)

with open('output.json', 'r') as out:
    data = json.load(out)
