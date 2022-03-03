import json
from sseclient import SSEClient as EventSource


print("Line 5")
url = 'https://stream.wikimedia.org/v2/stream/recentchange'
for event in EventSource(url):
    if event.event == 'message':
        try:
            change = json.loads(event.data)
        except ValueError:
            pass
        else:
            print('{user} edited {title}'.format(**change))

print("End")