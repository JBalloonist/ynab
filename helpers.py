import configparser
import requests
from pathlib import Path

def account_names(parameter_list):
    pass


def post_trans(payload):
    parser = configparser.ConfigParser()
    parser.read(PATH + 'simple.ini')
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
