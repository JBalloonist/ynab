#!/usr/bin/python3.6

import datetime
import json
import configparser
import requests
from twilio.rest import Client
from dateutil import parser

conf_parser = configparser.ConfigParser()
conf_parser.read('/home/JBalloonist/ynab/data/simple.ini')
PATH = '/home/JBalloonist/ynab/data/'
TOKEN = conf_parser.get('API', 'TOKEN')
BUDGET_ID = conf_parser.get('API', 'BUDGET_ID')
ACCOUNT_ID = conf_parser.get('API', 'ACCOUNT_ID')
URL = 'https://api.youneedabudget.com/v1/'

now = datetime.datetime.now() - datetime.timedelta(days=3)
date_since = now.strftime('%Y-%m-%d')

payload = {'type': 'uncategorized', 'since_date': date_since}
# r = requests.get('{}budgets/{}/accounts/{}/transactions?access_token={}'.format(URL, BUDGET_ID, ACCOUNT_ID, TOKEN), params=payload)
r = requests.get('{}budgets/{}/transactions?access_token={}'.format(URL, BUDGET_ID, TOKEN), params=payload)

print(r.status_code)
data = r.json()
with open('output.json', 'w') as out:
    json.dump(data, out)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACf4c509e765fab2a05da9204c7820139f'
auth_token = '0b66ae908b2b9d8b4ea869788a860cdc'
client = Client(account_sid, auth_token)

with open(f'{PATH}accounts_output.json') as out:
    accounts = json.load(out)
    accounts = accounts['data']['accounts']
    budget_accounts = [i['name'] for i in accounts if i['on_budget'] is True]

with open('output.json', 'r') as out:
    data = json.load(out)
    trans = data['data']['transactions']
    uncat_trans = [i for i in trans if i['transfer_account_id'] is None and i['account_name'] in budget_accounts]

num = len(uncat_trans)
header = f"There are {num} uncategorized transactions in YNAB.\n"

if num > 0:
    for n,i in enumerate(uncat_trans):
        name = i['payee_name']
        amt = int(i['amount']) / -1000
        acct = i['account_name']
        date = parser.parse(i['date']).strftime('%b %d, %Y')
        message = f'Name: {name}\nAccount: {acct}\nDate: {date}\nAmount: ${amt}'

        if n == 0:
            message = header + message

        print(message)

        message = client.messages \
                    .create(
                         body=message,
                         from_='+14159171602',
                         to='+19374090100'
                     )
