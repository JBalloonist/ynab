#!/usr/bin/python3.6

import pandas as pd
from helpers import post_trans
from datetime import datetime, timedelta


def main():
    PATH = '/home/JBalloonist/ynab/data/'
    sheets = ['loop.csv', 'cudgel.csv', 'sofi.csv']
    sheets = sheets + ['Navient-0{}.csv'.format(i) for i in range(1, 3)]

    for i in sheets:
        try:
            parser = Amortization(PATH + i, 1, 25)
            if str(create_ynab_trans(parser.get_next())) == '201':
                parser.export_remaining()
        except:
            pass


class Amortization(object):
    now = datetime.now()

    def __init__(self, file, add_days, sub_days):
        self.file = file
        self.add_days = add_days
        self.sub_days = sub_days
        self.df = pd.read_csv(self.file)
        self.df.date = pd.to_datetime(self.df.date)

    def plus_day(self):
        return self.now + timedelta(days=self.add_days)

    def minus_day(self):
        return self.now - timedelta(days=self.sub_days)

    def get_next(self):
        df = self.df.copy()
        trans = df.loc[(df.date < self.plus_day()) & (df.date > self.minus_day())].copy()
        return trans

    def get_remaining(self):
        df = self.df.copy()
        df = df.loc[(df.date > self.plus_day())]
        print('Data to keep: ')
        print(df.head())
        return df

    def export_remaining(self):
        self.get_remaining().to_csv(self.file, index=False)


def create_ynab_trans(trans):
    fmt = '%Y-%m-%d'
    trans.date = trans.date.dt.strftime(fmt)
    trans_dict = trans.T.to_dict()
    trans = trans_dict[0]
    payload = {'transaction': trans}
    return post_trans(payload)


if __name__ == "__main__":
    main()
