import datetime
import json
import configparser
import pprint
import requests
from pathlib import Path
from helpers import patch_trans
from dateutil import parser                                                                                                                                                                                                                                      
conf_parser = configparser.ConfigParser()
PATH = Path.cwd().parent / 'data'
conf_parser.read(PATH / 'simple.ini')
TOKEN = conf_parser.get('API', 'TOKEN')
BUDGET_ID = conf_parser.get('API', 'BUDGET_ID')
ACCOUNT_ID = conf_parser.get('API', 'AMAZON_ID')
URL = 'https://api.youneedabudget.com/v1/'

account_sid = conf_parser.get('TWILIO', 'account_sid')
auth_token = conf_parser.get('TWILIO', 'auth_token')
 
now = datetime.datetime.now() - datetime.timedelta(days=30)
date_since = now.strftime('%Y-%m-%d')

payload = {'type': 'unapproved', 'since_date': date_since}
r = requests.get('{}budgets/{}/accounts/{}/transactions?access_token={}'.format(URL, BUDGET_ID, ACCOUNT_ID, TOKEN), params=payload)
 
print(r.status_code)
data = r.json()
print(type(data))
# with open('unapproved.json', 'w') as out:
#     json.dump(data, out)

def memo_replace(memo):
    """
    docstring
    """
    memo = memo.replace('AMAZON', '').replace('MARKETPLACE', '')
    return memo.replace('SEATTLE WA', '').replace('RETAIL', '').replace('SHIPPING AND TAX', '').strip()
 
def set_memo(transactions):
    for trans in transactions['data']['transactions']:
        memo = memo_replace(trans['import_payee_name_original'])
        print(memo)
        trans['memo'] = memo
    return transactions['data']

pretty = pprint.PrettyPrinter(indent=4)
payload = set_memo(data)
pretty.pprint(payload)
patch_trans(payload)