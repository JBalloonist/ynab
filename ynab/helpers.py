import json
import configparser
import requests
from pathlib import Path
import get_accounts

def account_names(parameter_list):
    pass


def get_account_id():
    """
    docstring
    """
    PATH = Path.cwd().parent / 'ynab' / 'data' / 'accounts_output.json'
    if PATH.exists():
        pass
    else:
        get_accounts.get_accounts()

    with open(PATH) as out:
        account_data = json.loads(out.read())

    accounts = account_data['data']['accounts']
    accounts = {acct['name']: acct['id'] for acct in accounts}
    for n, acct_name in enumerate(accounts.keys(), start=1):
        print(f'{n}: {acct_name}')

    choice = int(input('Which account? Type a number of 1 through {}')) - 1
    return accounts[accounts.keys()[choice]]


# this needs to be converted to a Class...
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


def get_scheduled_trans():
    parser = configparser.ConfigParser()
    PATH = Path.cwd().parent / 'data' / 'simple.ini'
    parser.read(PATH)
    TOKEN = parser.get('API', 'TOKEN')
    BUDGET_ID = parser.get('API', 'BUDGET_ID')
    URL = 'https://api.youneedabudget.com/v1/'

    r = requests.get('{}budgets/{}/scheduled_transactions?access_token={}'.format(URL, BUDGET_ID, TOKEN))

    print(r.status_code)
    return r.json()


def patch_trans(payload):
    parser = configparser.ConfigParser()
    PATH = Path.cwd().parent / 'data' / 'simple.ini'
    parser.read(PATH)
    TOKEN = parser.get('API', 'TOKEN')
    BUDGET_ID = parser.get('API', 'BUDGET_ID')
    ACCOUNT_ID = parser.get('API', 'ACCOUNT_ID')
    URL = 'https://api.youneedabudget.com/v1/'

    url = '{}budgets/{}/transactions?access_token={}'.format(URL, BUDGET_ID, TOKEN)
    r = requests.patch(url, json=payload)
    print('')
    print(r.status_code)
    print('')
    print(r.text)
    print('')
    print(r.request.body)
    return r.status_code