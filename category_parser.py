#!/usr/bin/python3.6

import json
import configparser
from pathlib import Path
from twilio.rest import Client
from collections import defaultdict
from datetime import datetime

PATH = Path.home() / 'ynab' / 'data'
conf_parser = configparser.ConfigParser()
simple = PATH / 'simple.ini'
conf_parser.read([simple])
account_sid = conf_parser.get('TWILIO', 'account_sid')
auth_token = conf_parser.get('TWILIO', 'auth_token')
client = Client(account_sid, auth_token)

with open(PATH / 'categories.json', 'r') as out:
    data = json.load(out)

# print(json.dumps(data['data'], indent=4))

category_groups = data['data']['category_groups']

def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i)<128)


category = []
balances = defaultdict(list)


# update to add the main category and each of its balances as a dict
for main_cat in category_groups:
    if main_cat['name'] in ['Needs', 'True Expenses', 'Debt and Taxes', 'Credit Card Payments', 'Quality of Life']:
        # print(json.dumps(main_cat['categories'], indent=4))
        categories = main_cat['categories']
        master_cat = main_cat['name']
        mast_balances = []
        for cat_data in categories:
            name = remove_non_ascii(cat_data['name'])
            bal = cat_data['balance']
            # print('{}: {}').format(name, bal)

            if bal < 0:
                # balances.append(bal)
                mast_balances.append(bal)

        balances[master_cat] = mast_balances

now = datetime.now()
first_msg = f"--------------\nBalances as of {now}:\n -------------"
client.messages.create(body=first_msg, from_='+14159171602', to='+19374090100')

overspent = []
for k, v in balances.items():
    tot = round(sum(v) / 1000, 2)
    if tot < 0:
        text_message = (f'{k}: {tot}')
        overspent.append(tot)
        message = client.messages \
                            .create(
                             body=text_message,
                             from_='+14159171602',
                             to='+19374090100'
                         )

total_ovspnt = round(sum(overspent), 2)
ovspent_msg = (f'\nTotal overspent: {total_ovspnt}')
client.messages.create(body=ovspent_msg, from_='+14159171602', to='+19374090100')
