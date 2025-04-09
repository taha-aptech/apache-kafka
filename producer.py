from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:6667')

for i in range(10):
    message = 'Hello Kafka! Message {}'.format(i)
    producer.send('test_topic_python', message.encode('utf-8'))
    print("Sent: {}".format(message))
    time.sleep(1)

producer.flush()
