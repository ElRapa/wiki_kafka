from kafka import KafkaConsumer
from json import loads

bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
topicName = "Change_Log"

consumer = KafkaConsumer(
    topicName,
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='group-1',
    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=bootstrap_servers
    )

if consumer.bootstrap_connected():
    print("Connection Consumer-Broker successful")
else: print("No connection Consumer-Broker")

count_global = 0
count_ger = 0
timestamp_pre = 0

for m in consumer:
    if m.timestamp - timestamp_pre <= 60000:
        count_global += 1
        if m.value["meta"]["domain"] == "de.wikipedia.org":
            count_ger += 1
    else:
        print( m.timestamp, " global: ", count_global, " germany: ", count_ger)
        count_global = 0
        count_ger = 0
        timestamp_pre = m.timestamp
