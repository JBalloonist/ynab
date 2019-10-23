from __future__ import print_function
import time
import ynab
from ynab.rest import ApiException
from pprint import pprint

API_KEY = open('key.txt', 'r').readline()


# Configure API key authorization: bearer
configuration = ynab.Configuration()

configuration.api_key['Authorization'] = '83033ac834741dd1ee2517153339cc901819c72280a070211c901e5e2eb31954'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = ynab.AccountsApi()
budget_id = 'budget_id_example' # str | The ID of the Budget.
account_id = 'account_id_example' # str | The ID of the Account.

try:
    api_response = api_instance.get_account_by_id(budget_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_by_id: %s\n" % e)

