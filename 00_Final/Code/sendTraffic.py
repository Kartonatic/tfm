from kafka import KafkaProducer
import sys
import time
import datetime
import pandas as pd
import json

producer = KafkaProducer(bootstrap_servers=['kafka1:9092'])

topic_name = "streamKafka"
print("sending messages to topic:" + str(topic_name))

#Compatible with logstash
for chunck_df in  pd.read_csv("../Data/miniTraffic.csv", chunksize=100):
    for index, point  in chunck_df.iterrows():
        # Los puntos no funcionan bien en las columnas de spark
        #point.index = [x.replace(".","_") for x in point.index]
        point['location'] = [point['coordinates_long'],point['coordinates_lat']]
        point['dateSend'] = datetime.datetime.now()
        msg = point.to_json()
        msg2 = json.loads(msg, encoding='utf-8')
        msgJson = json.dumps(msg2)
        producer.send(str(topic_name), bytes(msgJson + '\n', 'utf-8'))
producer.close()
