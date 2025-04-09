from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test_topic_python',
    bootstrap_servers='localhost:6667',
    auto_offset_reset='earliest',
    group_id='test-group'
)

print("Listening to Kafka topic...")
for message in consumer:
    print("Received: %s" % message.value.decode('utf-8'))
