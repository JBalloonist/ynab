import requests

TOKEN = '83033ac834741dd1ee2517153339cc901819c72280a070211c901e5e2eb31954'
URL = 'https://api.youneedabudget.com/v1/'

# r = requests.get('{}budgets'.format(URL), headers={'Content-Type':'application/json', 'Authorization': 'Bearer: {}'.format(TOKEN)})
r = requests.get('{}budgets?access_token={}'.format(URL, TOKEN))

print(r.status_code)
print(r.text)
print(r.json())