from kafka import SimpleConsumer, SimpleClient
from kafka import KafkaConsumer
from kafka import KafkaClient

group_name = "my-group"
topic_name = "fast-messages"

kafka = KafkaClient('kafka1:9092')
consumer = SimpleConsumer(kafka, group_name, topic_name)

print ("Created consumer for group:"+ group_name + " and topic: " + topic_name + "")
print("Waiting for messages...")

for msg in consumer:
	print(msg)
