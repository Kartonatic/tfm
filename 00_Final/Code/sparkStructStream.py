from __future__ import print_function

import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, from_json
from pyspark.sql.types import *
from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("""
        Usage: structured_kafka_wordcount.py <bootstrap-servers> <subscribe-type> <topics>
        """, file=sys.stderr)
        exit(-1)

    bootstrapServers = sys.argv[1]
    subscribeType = sys.argv[2]
    topics = sys.argv[3]

    sc = SparkContext().getOrCreate()

    spark = SparkSession(sc)\
        .builder\
        .appName("StructuredKafkaGPS")\
        .getOrCreate()


    schema = StructType([StructField("sensorId", IntegerType()),
                         StructField("Type", StringType()),
                         StructField("coordinates_lat", FloatType()),
                         StructField("coordinates_long", FloatType()),
                         StructField("altitude", FloatType()),
                         StructField("heading", FloatType()),
                         StructField("speed", IntegerType()),
                         StructField("speedmetric", StringType()),
                         StructField("observationTime", StringType()),
                         StructField("serverTime", StringType()),
                         StructField("temp", FloatType()),
                         StructField("date", StringType()),
                         StructField("location", ArrayType(FloatType())),
                         StructField("dateSend", TimestampType())
                        ])

    # Create DataSet representing the stream of input lines from kafka
    lines = spark\
        .readStream\
        .format("kafka")\
        .option("kafka.bootstrap.servers", bootstrapServers)\
        .option(subscribeType, topics)\
        .option("startingoffsets", "earliest")\
        .load() \
        .select(from_json(col("value").cast("string"), schema).alias("stream"))
        #.select(from_json(col("value").cast("string"), schema).alias("data"))

    # lines.isStreaming()    # Returns True for DataFrames that have streaming sources

    lines.printSchema()

    # Generate running word count
    #carCounts = lines.groupBy('stream.Type').count()

    sch_user = StructType([
        StructField("id_user", IntegerType()),
        StructField("name", StringType())
        ])

    sch_sen_user = StructType([
        StructField("id_user_sensor", IntegerType()),
        StructField("sensorId", StringType()),
        StructField("user", IntegerType())
        ])


    users = spark.read.csv("Users.csv", header=True, schema = sch_user)
    userSensor = spark.read.csv("UserSensor.csv", header=True, schema=sch_sen_user)
    users.printSchema()
    userSensor.printSchema()
    #joinUserSensor = users.alias('user').join(sc.broadcast(userSensor.alias('sensors')), col('user.id_user') == col('sensors.user'))
    joinUserSensor = users.alias('user').join(userSensor.alias('sensors'), col('user.id_user') == col('sensors.user'))
    joinUserSensor.printSchema()

    joinData = lines.alias('stream').join(joinUserSensor.alias('data'), col('stream.sensorId') == col('data.sensorId'),"leftOuter") # can be "inner", "leftOuter", "rightOuter"
    joinData.printSchema()

    # Start running the query that prints the running counts to the console
    query = joinData.groupBy("data.name").count().sort(col("count").desc())\
        .writeStream\
        .outputMode('complete')\
        .format('console')\
        .trigger(processingTime='2 seconds')\
        .start()
        #.trigger(continuous='2 seconds')\
        #.start()

    query.awaitTermination()
