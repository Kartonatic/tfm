from kafka import KafkaClient
from kafka import SimpleProducer
from kafka import KafkaProducer
import sys
import time

kafka = KafkaClient('kafka1:9092')
producer = SimpleProducer(kafka, async=True)

topic_name = "fast-messages"
print("sending messages to topic:" + str(topic_name))

for i in range(100):
	msg = 'async message-' + str(i)
	print("sending message: " + msg)
	producer.send_messages('fast-messages', bytes(msg, 'UTF-8'))
	time.sleep(5)