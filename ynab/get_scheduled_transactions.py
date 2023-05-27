import json
from pathlib import Path
from helpers import get_scheduled_trans


pth = Path.cwd().parent / 'data'
data = get_scheduled_trans()
with open(pth / 'scheduled.json', 'w') as out:
    json.dump(data, out)
    