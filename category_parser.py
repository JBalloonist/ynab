import json
# from collections import defaultdict

with open('/home/JBalloonist/ynab/data/categories.json', 'r') as out:
    data = json.load(out)

# print(json.dumps(data['data'], indent=4))

category_groups = data['data']['category_groups']

def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i)<128)


# category = []
# balances = defaultdict(category)
balances = []

# update to add the main category and each of its balances as a dict
for main_cat in category_groups:
    if main_cat['name'] in ['Needs', 'True Expenses', 'Debt and Taxes', 'Credit Card Payments', 'Quality of Life']:
        # print(json.dumps(main_cat['categories'], indent=4))
        categories = main_cat['categories']
        for cat_data in categories:
            name = remove_non_ascii(cat_data['name'])
            bal = cat_data['balance']
            # print('{}: {}').format(name, bal)

            if bal < 0:
                balances.append(bal)

print(balances)
overspent = sum(balances) / 1000
print('Total overspent: {}').format(overspent)