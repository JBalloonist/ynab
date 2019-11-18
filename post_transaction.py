#!/usr/bin/python3.6

import json
import configparser
import requests

PATH = '/home/JBalloonist/ynab/'
parser = configparser.ConfigParser()
parser.read(PATH + 'simple.ini')
TOKEN = parser.get('API', 'TOKEN')
BUDGET_ID = parser.get('API', 'BUDGET_ID')
ACCOUNT_ID = parser.get('API', 'ACCOUNT_ID')
URL = 'https://api.youneedabudget.com/v1/'


def post_trans(payload):
    url = '{}budgets/{}/transactions?access_token={}'.format(URL, BUDGET_ID, TOKEN)
    r = requests.post(url, json=payload)
    print('')
    print(r.status_code)
    print('')
    print(r.text)
    print('')
    print(r.request.body)
    return r.status_code

if __name__ == "__main__":
    data = input("Where is the file")
    trans = json.dumps(data)
    payload = {'transaction': trans}
    