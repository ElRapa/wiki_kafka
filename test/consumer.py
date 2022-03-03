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

for m in consumer:
    print(m)