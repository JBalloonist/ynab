import json
import requests
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('simple.ini')
TOKEN = parser.get('API', 'TOKEN')
BUDGET_ID = parser.get('API', 'BUDGET_ID')
ACCOUNT_ID = parser.get('API', 'ACCOUNT_ID')
URL = 'https://api.youneedabudget.com/v1/'

payload = {
    "transaction": {
        "account_id": "e51c95d2-209a-4a30-9384-09b91863dff7",
        "date": "2019-11-01",
        "amount": 1000,
        "memo": "test",
        "cleared": "cleared"
    }
}

# data={}
# data['account_id'] = "d9d9c545-b754-49af-87ac-cc9991df9224"
# data['date']="2019-10-23"
# data['amount']=1000
# data['memo'] ="test"
# data['cleared']="cleared"
# payload = {'transaction': data}

print(payload)


url = '{}budgets/{}/transactions?access_token={}'.format(URL, BUDGET_ID, TOKEN)
r = requests.post(url, json=payload)
print('')
print(r.status_code)
print('')
print(r.text)
print('')
print(r.request.body)
