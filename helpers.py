import configparser
import requests
from pathlib import Path

def account_names(parameter_list):
    pass


def post_trans(payload):
    parser = configparser.ConfigParser()
    PATH = Path.cwd().parent / 'ynab' / 'data' / 'simple.ini'
    parser.read(PATH)
    TOKEN = parser.get('API', 'TOKEN')
    BUDGET_ID = parser.get('API', 'BUDGET_ID')
    ACCOUNT_ID = parser.get('API', 'ACCOUNT_ID')
    URL = 'https://api.youneedabudget.com/v1/'

    url = '{}budgets/{}/transactions?access_token={}'.format(URL, BUDGET_ID, TOKEN)
    r = requests.post(url, json=payload)
    print('')
    print(r.status_code)
    print('')
    print(r.text)
    print('')
    print(r.request.body)
    return r.status_code


def get_scheduled_trans(parameter_list):
    parser = configparser.ConfigParser()
    PATH = Path.cwd().parent / 'ynab' / 'data' / 'simple.ini'
    parser.read(PATH)
    TOKEN = parser.get('API', 'TOKEN')
    BUDGET_ID = parser.get('API', 'BUDGET_ID')
    URL = 'https://api.youneedabudget.com/v1/'

    r = requests.get('{}budgets/{}/scheduled_transactions?access_token={}'.format(URL, BUDGET_ID, TOKEN))

    print(r.status_code)
    data = r.json()
