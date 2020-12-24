import json
import requests
import configparser
from pathlib import Path

def get_accounts():
    """
    docstring
    """
    path = Path.cwd().home() / 'ynab' / 'data' / 'simple.ini'
    parser = configparser.ConfigParser()
    parser.read([path])
    TOKEN = parser.get('API', 'TOKEN')
    BUDGET_ID = parser.get('API', 'BUDGET_ID')
    ACCOUNT_ID = parser.get('API', 'ACCOUNT_ID')
    URL = 'https://api.youneedabudget.com/v1/'

    r = requests.get('{}budgets/{}/accounts?access_token={}'.format(URL, BUDGET_ID, TOKEN))
    print(r.status_code)
    data = r.json()
    with open('accounts_output.json', 'w') as out:
        json.dump(data, out)

if __name__ == "__main__":
    get_accounts()
