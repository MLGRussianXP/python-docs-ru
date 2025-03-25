import json
import os
import urllib.request
from datetime import datetime

key = os.environ.get('TX_TOKEN')
project = os.environ.get('TX_PROJECT')

url = "https://rest.api.transifex.com/resource_language_stats?filter[project]=o%3Apython-doc%3Ap%3A{}&filter[language]=l%3Aru".format(project)

headers = {
    "accept": "application/vnd.api+json",
    "authorization": "Bearer " + key
}

total = 0
reviewed = 0

while url:
    request = urllib.request.Request(url=url, headers=headers)
    
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode("utf-8"))
        url = data['links'].get('next')
        for resource in data['data']:
            reviewed += resource['attributes']['reviewed_strings']
            total += resource['attributes']['total_strings']

p = '{:.2%}'.format(reviewed / total if total > 0 else 0)
print(json.dumps({
    'translation': p,
    'updated_at': datetime.utcnow().isoformat(timespec='seconds') + 'Z',
}))
