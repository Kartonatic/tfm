from __future__ import print_function

import sys
import json

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import Row, SparkSession
from pyspark.sql.functions import col, expr, to_json, struct
from pyspark.sql.functions import broadcast
from pyspark.sql.types import *


# Lazily instantiated global instance of SparkSession
def getSparkSessionInstance(sparkConf):
    if ("sparkSessionSingletonInstance" not in globals()):
        globals()["sparkSessionSingletonInstance"] = SparkSession \
            .builder \
            .config(conf=sparkConf) \
            .getOrCreate()
    return globals()["sparkSessionSingletonInstance"]



def getDataUsers(sparkContext):
    if ("UserSensorName" not in globals()):
        # Get data from csv (in hadoop)
        sch_user = StructType([
                         StructField("id_user", IntegerType()),
                         StructField("name", StringType())
                   ])

        sch_sen_user = StructType([
                         StructField("id_user_sensor", IntegerType()),
                         StructField("sensorId", StringType()),
                         StructField("user", IntegerType())
                   ])

        spark = getSparkSessionInstance(sparkContext.getConf())
        users = spark.read.csv("Users.csv", header=True, schema = sch_user)
        userSensor = spark.read.csv("UserSensor.csv", header=True, schema=sch_sen_user)

        #Join data form hdfs
        joinUserSensor = users.alias('user').join(userSensor.alias('sensors'), col('user.id_user') == col('sensors.user'))
        joinUserSensor.printSchema()

        globals()["UserSensorName"] = joinUserSensor
    return globals()["UserSensorName"]




if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: sparkStreaming2.py <zkServers> <topicIn> <topicOut>", file=sys.stderr)
        exit(-1)
    zkQuorum, topicIn, topicOut = sys.argv[1:]
    sc = SparkContext(appName="PythonStreamingKafkaJson")
    ssc = StreamingContext(sc, 10)

    kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topicIn: 1})

    # Convert RDDs of the words DStream to DataFrame and run SQL query
    def process(time, rdd):
        print("========= %s =========" % str(time))

        try:
            # Get the singleton instance of SparkSession
            if (not rdd.isEmpty()):
                spark = getSparkSessionInstance(rdd.context.getConf())

                # Get data from kafka json to df
                df = spark.read.json(rdd.map(lambda x: x[1]))

                joinUserSensor = getDataUsers(rdd.context)

                # join data from hdfs and stream
                joinData = df.alias('stream').join(joinUserSensor.alias('data'), col('stream.sensorId') == col('data.sensorId'),"leftOuter") # can be "inner", "leftOuter", "rightOuter"

                joinData.show()

                dataToSend = joinData.select("Type","altitude","coordinates_lat","coordinates_long","date","dateSend", "heading","location","observationTime","stream.sensorId","serverTime","speed","speedmetric","temp","id_user", "name")

                dataToSend.select(to_json(struct([dataToSend[x] for x in dataToSend.columns])).alias("value")).write.format("kafka").option("kafka.bootstrap.servers", "kafka1:9092,kafka2:9092,kafka3:9092").option("topic", topicOut).save()
                dataToSend.show()

        except Exception as e:
            print(str(e))
            pass

    kvs.foreachRDD(process)
    ssc.start()
    ssc.awaitTermination()
