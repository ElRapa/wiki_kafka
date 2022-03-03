import json
from kafka import KafkaProducer
from sseclient import SSEClient as EventSource

url = 'https://stream.wikimedia.org/v2/stream/recentchange'
bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
topicName = "Change_Log"

## initialize Producer
producer = KafkaProducer(
    bootstrap_servers = bootstrap_servers,
    value_serializer=lambda m: json.dumps(m).encode('utf-8'), 
    )

if producer.bootstrap_connected():
    print("Connection Producer-Broker successful")
else: print("No connection Producer-Broker")

for event in EventSource(url):
    if event.event == 'message':
        try:
            change = json.loads(event.data)
        except ValueError:
            pass
        else:
            producer.send(topicName, value=change)
            producer.flush()
    else: break