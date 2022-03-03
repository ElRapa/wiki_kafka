print("test start")
import json
import sseclient
from sseclient import SSEClient as EventSource

url = 'https://stream.wikimedia.org/v2/stream/recentchange'

counter = 0

for event in EventSource(url):
    if counter < 20:
        counter += 1
        if event.event == 'message':
            try:
                change = json.loads(event.data)
            except ValueError:
                pass
            else:
                print('{user} edited {title}'.format(**change))
                print(change["meta"]["domain"])
    else:
        break

print("test end")

'''
{
'$schema': '/mediawiki/recentchange/1.0.0',
'meta': {'uri': 'https://commons.wikimedia.org/wiki/Category:Swindon_Town_F.C.',
        'request_id': '407b57b3-806e-4d7a-ba34-c69e25f5cdd8', 
        'id': '08a6d100-5d9a-492b-a1da-8cb0b7f1c972', 
        'dt': '2022-03-03T09:04:07Z', 
        'domain': 'commons.wikimedia.org', 
        'stream': 'mediawiki.recentchange', 
        'topic': 'eqiad.mediawiki.recentchange', 
        'partition': 0, 
        'offset': 3683567402
        },
'id': 1876971282, 
'type': 'categorize', 
'namespace': 14, 
'title': 'Category:Swindon Town F.C.', 
'comment': '[[:File:Sam Allen Blue Plaque.jpg]] added to category', 
'timestamp': 1646298247, 
'user': 'Shaun Sheep', 
'bot': False, 
'server_url': 'https://commons.wikimedia.org', 
'server_name': 'commons.wikimedia.org', 
'server_script_path': '/w', 
'wiki': 'commonswiki', 
'parsedcomment': '<a href="/wiki/File:Sam_Allen_Blue_Plaque.jpg" title="File:Sam Allen Blue Plaque.jpg">File:Sam Allen Blue Plaque.jpg</a> added to category'
}
'''