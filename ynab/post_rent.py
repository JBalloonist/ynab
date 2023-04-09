#!/usr/bin/python3.6

import argparse
import json
from sys import argv
from datetime import date, datetime
from pathlib import Path
from helpers import post_trans


def create_ynab_trans(payload, amount=1045, date=None):
    now = datetime.now()
    fmt = '%Y-%m-%d'
    print(now.strftime(fmt))

    transactions = payload['transactions']
    for tran in transactions:
        tran['date'] = now.strftime(fmt)
        if amount:
            amount *= 1000
            tran['amount'] = amount
        if date:
            tran['date'] = date

    payload['transactions'] = transactions
    return post_trans(payload)


def main(args):
    path = Path.cwd().parent / 'ynab' / 'data' / 'rent.json'
    with open(path) as out:
        trans = json.load(out)

    ap = argparse.ArgumentParser()
    ap.add_argument('-a', '--amt', help='enter an amount to post')
    ap.add_argument('-d', '--date', 
    help='enter a date for the transaction (use "yyyy-mm-dd" format')
    opts = ap.parse_args(args)

    if opts.date:
        create_ynab_trans(trans, date=opts.date)
    if opts.amt:
        amt = int(opts.amt)
        create_ynab_trans(trans, amount=amt)
    else:
        create_ynab_trans(trans)


if __name__ == "__main__":
    main(argv[1:])
