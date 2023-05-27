import json
from pathlib import Path

PATH = Path.cwd().parent
DATA = PATH / 'data'
with open(DATA / 'scheduled.json') as out:
    data = json.load(out)
    trans = data['data']['scheduled_transactions']

card_list = ["Diamond Preferred (1978) E", "Emigrant Direct (0286) R", "Marriott 9290", "53 Credit Card", "D Preferred (5217) R"]
minimum = [i for i in trans if i['account_name'] in card_list]

total = 0
for tr in minimum:
    amt = tr['amount'] / 1000
    total = total + amt
    print(f"{tr['account_name']}\namount: {amt}\ndate: {tr['date_next']}\n\n")
    
print(f'Total: {total}')
