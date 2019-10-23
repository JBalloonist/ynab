import json
import requests

TOKEN = '83033ac834741dd1ee2517153339cc901819c72280a070211c901e5e2eb31954'
URL = 'https://api.youneedabudget.com/v1/'
BUDGET_ID = "ac30126d-1480-4b4f-a9c2-bb77fa4fae89"
ACCOUNT_ID = "61a88796-8932-470e-991a-0681d3e72d5c"

date_since = '2019-10-01'
payload = {'type': 'uncategorized', 'since_date': date_since}
r = requests.get('{}budgets/{}/accounts/{}/transactions?access_token={}'.format(URL, BUDGET_ID, ACCOUNT_ID, TOKEN), params=payload)

print(r.status_code)
data = r.json()
with open('output.json', 'w') as out:
    json.dump(data, out)
