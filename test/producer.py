import json
from random import random
import pandas as pd
from sseclient import SSEClient as EventSource
from kafka import KafkaProducer

url = 'https://stream.wikimedia.org/v2/stream/recentchange'
bootstrap_servers = ['localhost:9091']#, 'localhost:9092', 'localhost:9093']
topicName = "Change_Log"

limit = 5
stream_db = pd.DataFrame()

## initialize Producer
producer = KafkaProducer(
    bootstrap_servers = bootstrap_servers,
    value_serializer=lambda m: json.dumps(m).encode('utf-8'), 
    )

if producer.bootstrap_connected():
    print("Connection Producer-Broker successful")
else: print("No connection Producer-Broker")

# producer.send("Test_Log","Test")
# producer.flush()

for event in EventSource(url):
    limit -= 1
    if event.event == 'message'and limit>= -1:
        try:
            change = json.loads(event.data)
        except ValueError:
            pass
        else:
            #print('{user} edited {title}'.format(**change))
            # change_db = pd.DataFrame(pd.json_normalize([change]))
            # stream_db = pd.concat([stream_db, change_db])
            # send stream to send_Buffer:
            producer.send(topicName, value=change)
            producer.flush(random())
        # try:
        #     producer.send(topicName, event.data)
        #     producer.flush()
        # except ValueError:
        #     pass      

    else: break
# print(stream_db)
# print(stream_db.columns, " with a length of ", len(stream_db.columns))



