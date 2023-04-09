import configparser
import json
import requests
from pathlib import Path


def main():
    flagged_trans = get_flagged_data()
    new_transactions = create_update_trans(flagged_trans)
    payload = {'transactions': new_transactions}
    post_trans(payload)

    
def get_flagged_data():
    data = Path.cwd().home() / 'ynab' / 'data' / 'output.json'

    with open(data, 'rb') as out:
        transactions = json.load(out)
        transactions = transactions['data']['transactions']
        flagged_trans = [i for i in transactions if i['flag_color'] != None]
    
    return flagged_trans


def create_update_trans(transactions):
    id_and_flag = [{key: tran[key] for key in tran.keys() & {'id', 'flag_color', 'account_id', 'date', 'amount'}} for tran in transactions]

    for tran in id_and_flag:
        tran['flag_color'] = None

    return id_and_flag
    


def post_trans(payload):
    path = Path.cwd().home() / 'ynab' / 'data' / 'simple.ini'
    parser = configparser.ConfigParser()
    parser.read([path])
    TOKEN = parser.get('API', 'TOKEN')
    BUDGET_ID = parser.get('API', 'BUDGET_ID')
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

if __name__ == "__main__":
    main()
