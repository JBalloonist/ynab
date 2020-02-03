#!/usr/bin/python3.6

import json
from twilio.rest import Client

PATH = '/home/JBalloonist/ynab/data/'

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

for n,i in enumerate(uncat_trans):
    name = i['payee_name']
    amt = int(i['amount']) / -1000
    acct = i['account_name']
    date = i['date']
    message = f'Name: {name}\nAccount: {acct}\nDate:{date}\nAmount: ${amt}'

    if n == 0:
        message = header + message

    print(message)

    message = client.messages \
                .create(
                     body=message,
                     from_='+14159171602',
                     to='+19372316721'
                 )
