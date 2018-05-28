from __future__ import print_function

import sys
import json

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import pymongo



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: sparkStreaming.py <zk> <topic>", file=sys.stderr)
        exit(-1)

    sc = SparkContext(appName="PythonStreamingKafkaJson")
    ssc = StreamingContext(sc, 10)

    zkQuorum, topic = sys.argv[1:]
    # ssc (streaming context object), zkQuorum(group zookeeper), groupId(The group id for this consumer),
    # topics (Dict of (topic_name -> numPartitions) to consume. Each partition is consumed in its own thread)
    kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 2})
    
    parsed = kvs.map(lambda x: json.loads(x[1]))
    parsed.pprint()

    sensor_counts = parsed.map(lambda sensorId: (sensorId['sensorId'],1)).reduceByKey(lambda x,y: x + y)
    sensor_counts.pprint()
    sensor_counts.count().pprint()
    parsed.count().pprint()

    client = MongoClient("mongomaster", 27017)
    db = client.osm
    ways = db.ways

    #sensor_directions = parsed.map(lambda x: (x['sensorId'], ways.find({"loc": { "$near": x['location'] , "$maxDistance": 0.001 } })[0])
    #sensor_directions.pprint()

    client.close()

    ssc.start()
    ssc.awaitTermination()