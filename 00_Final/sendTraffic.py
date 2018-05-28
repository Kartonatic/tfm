from kafka import KafkaClient
from kafka import SimpleProducer
from kafka import KafkaProducer
import sys
import time
import datetime
import pandas as pd
import json



kafka = KafkaClient('kafka1:9092')
producer = SimpleProducer(kafka, async=True)

topic_name = "streamKafka"
print("sending messages to topic:" + str(topic_name))

#Compatible with logstash
for chunck_df in  pd.read_csv("miniTraffic.csv", chunksize=100):
    for index, point  in chunck_df.iterrows():
        point['location'] = [point['coordinates.long'],point['coordinates.lat']]
        point['dateSend'] = datetime.datetime.now()
        msg = point.to_json()
        msg2 = json.loads(msg, encoding='utf-8')
        msgJson = json.dumps(msg2)
        producer.send_messages(str(topic_name), bytes(msgJson + '\n', 'UTF-8'))
        time.sleep(0.006)