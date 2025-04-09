from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:6667')

for i in range(10):
    message = f'Hello Kafka! Message {i}'
    producer.send('test_topic_python', message.encode('utf-8'))
    print(f"Sent: {message}")
    time.sleep(1)

producer.flush()
