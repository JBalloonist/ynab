import json
from helpers import get_scheduled_trans

data = get_scheduled_trans()
with open('scheduled.json', 'w') as out:
    json.dump(data, out)
    