from __future__ import print_function

import sys
import json
import time as time_py
from urllib.request import urlopen

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import Row, SparkSession
# spark sql function for columns
from pyspark.sql.functions import col, expr, to_json,
 struct, format_number, \
  monotonically_increasing_id, udf, unix_timestamp, \
  from_unixtime, datediff, array
# Se necesitara current_date para fecha actual cuando este en produccion
from pyspark.sql.types import *
# math spark sql function
from pyspark.sql.functions import acos, cos, sin, lit, radians
# Usamos pymongo porque no carga la collecion en memoria (la libreria que
# usa spark si lo hace)
import pymongo
from pymongo import MongoClient

'''
Instancia global de la sesion de spark (singleton, estancia perezosa)
'''


def getSparkSessionInstance(sparkConf):
 if ("sparkSessionSingletonInstance" not in globals()):
  globals()["sparkSessionSingletonInstance"] = SparkSession \
   .builder \
   .config(conf=sparkConf) \
   .getOrCreate()
 return globals()["sparkSessionSingletonInstance"]

'''
Obtiene los datos del usuarios con un singleton
'''


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
  users = spark.read.csv("Users.csv", header=True, schema=sch_user)
  userSensor = spark.read.csv(
   "UserSensor.csv", header=True, schema=sch_sen_user)

  # Join data form hdfs
  joinUserSensor = users.alias('user').join(userSensor.alias(
   'sensors'), col('user.id_user') == col('sensors.user'))

  globals()["UserSensorName"] = joinUserSensor
 return globals()["UserSensorName"]

'''
Obtiene los puntos negros de Espania
'''


def getBlackShapes(sparkContext):
 if ("BlackShapes" not in globals()):
  # Get data from csv (in hadoop)
  sch_blk_shp = StructType([
   StructField("", IntegerType()),
   StructField("Address", StringType()),
   StructField("Province", StringType()),
   StructField("Country", StringType()),
   StructField("numAccident", FloatType()),
   StructField("lat", FloatType()),
   StructField("long", FloatType())
  ])
  spark = getSparkSessionInstance(sparkContext.getConf())
  blk_shp = spark.read.csv(
   "blackshapes.csv", header=True, schema=sch_blk_shp)
  blk_shp = blk_shp.withColumn("lat_min",
          (format_number(blk_shp.lat, 3) - 0.005).
          cast(FloatType())).\
   withColumn("lat_max", (format_number(blk_shp.lat, 3) + 0.005).
      cast(FloatType())).\
   withColumn("long_min", (format_number(blk_shp.long, 3) - 0.005).
      cast(FloatType())).\
   withColumn("long_max", (format_number(
    blk_shp.long, 3) + 0.005).cast(FloatType()))

  globals()["BlackShapes"] = blk_shp
 return globals()["BlackShapes"]

'''
Distancia en km entre dos puntos (haversine)
'''


def dist(long_x, lat_x, long_y, lat_y):
 return acos(
  sin(radians(lat_x)) * sin(radians(lat_y)) +
  cos(radians(lat_x)) * cos(radians(lat_y)) *
  cos(radians(long_x) - radians(long_y))
 ) * lit(6371.0)


if __name__ == "__main__":
 if len(sys.argv) != 5:
  print("Usage: sparkStreaming2.py <zkServers> <topicIn>" +
    "<kServers> <topicOut>", file=sys.stderr)
  exit(-1)
 zkQuorum, topicIn, kServer, topicOut = sys.argv[1:]
 sc = SparkContext(appName="PythonStreamingKafkaJson")
 ssc = StreamingContext(sc, 10)
 # inicializamos los globals
 getBlackShapes(sc)
 getDataUsers(sc)
 kvs = KafkaUtils.createStream(
  ssc, zkQuorum, "spark-streaming-consumer", {topicIn: 1})

 # Convert RDDs of the words DStream to DataFrame and run SQL query
 def process(time, rdd):
  print("========= %s =========" % str(time))
  # 2018-05-28T13:52:07.0000000Z,2018-05-28T13:52:35.6721175Z
  format_1 = "yyyy-MM-dd'T'HH:mm:ss.SSSSSSS'Z'"
  a = time_py.time()

  try:
   # Get the singleton instance of SparkSession
   if (not rdd.isEmpty()):
    spark = getSparkSessionInstance(rdd.context.getConf())
    # rdd.context.clearCache()
    # Get data from kafka json to df
    df = spark.read.json(rdd.map(lambda x: x[1]))
    df = df.rdd.repartition(100).toDF()
    print(df.count())

    df = df.withColumn('observationDate',
         from_unixtime(
          unix_timestamp('observationTime',
              format_1))).\
     withColumn('serverDate', from_unixtime(
      unix_timestamp('serverTime', format_1)))
    # Usa current_date(), col("observationDate") en produccion
    df = df.where(datediff(col("serverTime"),
          col("observationDate")) < 7)

    joinUserSensor = getDataUsers(rdd.context)

    # join data from hdfs and stream
    joinData = df.alias('stream').join(joinUserSensor.alias('data'),
             col('stream.sensorId') == col(
     'data.sensorId'), "leftOuter")

    dataToSend = joinData.select("Type", "altitude", "coordinates_lat",
            "coordinates_long", "date",
            "observationTime", "observationDate",
            "dateSend", "serverDate",
            "heading", "location", "stream.sensorId",
            "serverTime", "speed",
            "speedmetric", "temp",
            "id_user", "name")
    dataToSend = dataToSend.withColumn(
     "id", monotonically_increasing_id())

    actualCoordinates = dataToSend.select(
     "id", "coordinates_lat", "coordinates_long")
    # Cargamos los puntos negros
    blackShapes = getBlackShapes(rdd.context)
    # Los cruzamos con las posiciones actuales de los vehiculos
    nearBlkShp = actualCoordinates.crossJoin(blackShapes)
    # Obtenemos solo los puntos mas cercanos a ~1km de distancia
    # How to find the most near position efficient?
    # https://gis.stackexchange.com/questions/8650/
    nearBlkShp = nearBlkShp.filter(
            (nearBlkShp.lat_min <= nearBlkShp.coordinates_lat) &
            (nearBlkShp.lat_max >= nearBlkShp.coordinates_lat) &
            (nearBlkShp.long_min <= nearBlkShp.coordinates_long) &
            (nearBlkShp.long_max >= nearBlkShp.coordinates_long))
    # Obtenemos las distancias a los puntos negros
    nearBlkShp = nearBlkShp.select(col("id"), col("Address"), 
            col("Province"), col("Country"), col("numAccident"),
            col("lat").alias("blk_point_lat"),
            col("long").alias("blk_point_long"),
            dist(col('coordinates_lat'),
             col('coordinates_long'),
             col('lat'),
             col('long')).alias("Distance"))
    # Nos quedamos con la menor
    minD4 = nearBlkShp.groupBy("id").min("Distance")
    # Ahora obtenemos los que tienen solo menor distancia
    finalNearBlkShp = minD4.alias('mins').join(
                nearBlkShp.alias('dataBlkShp'),
               (col('mins.id') == col('dataBlkShp.id')) &
               (col('mins.min(Distance)') == col('dataBlkShp.Distance')),
               "leftOuter").\
     select(col("dataBlkShp.id").alias('id'),
       col("dataBlkShp.Address").alias('address'),
       col("dataBlkShp.Province").alias('province'),
       col("dataBlkShp.Country").alias('country'),
       col("dataBlkShp.numAccident").alias('accidents'),
       col("dataBlkShp.blk_point_lat").alias(
        'blk_point_lat'),
       col("dataBlkShp.blk_point_long").alias(
        'blk_point_long'),
       col("dataBlkShp.Distance").alias('dist_to_blk_shp'))

    # Join de los puntos negros con los datos
    dataToSend = dataToSend.alias('data').join(finalNearBlkShp.alias(
     'blk_shp'), col('data.id') == col('blk_shp.id'), "leftOuter")
    dataToSend = dataToSend.select(col("data.Type").alias("Type"),
            col("data.altitude").alias("altitude"),
            col("data.observationTime").alias("observationTime"),
            col("data.dateSend").alias("dateSend"),
            col("data.serverTime").alias("serverTime"),
            col("data.heading").alias("heading"),
            col("data.location").alias("location"),
            col("data.sensorId").alias("sensorId"),
            col("data.speed").alias("speed"),
            col("data.speedmetric").alias("speedmetric"),
            col("data.temp").alias("temp"),
            col("data.id_user").alias(
             "id_user"),
            col("data.name").alias("user"),
            col("blk_shp.address").alias(
             "blk_shp_address"),
            col("blk_shp.province").alias(
             "blk_shp_province"),
            col("blk_shp.country").alias(
             "blk_shp_country"),
            col("blk_shp.accidents").alias(
             "blk_shp_accidents"),
            array(col('blk_shp.blk_point_lat'),
              col('blk_shp.blk_point_long')).
            alias("blk_shp_coordinates"),
            col("blk_shp.dist_to_blk_shp").
            alias("blk_shp_dist")
            )

    # Send data
    # dataToSend.printSchema()
    print(dataToSend.rdd.getNumPartitions())
    dataToSend.select(to_json(struct(
                     [dataToSend[x] for x in dataToSend.columns])).
                      alias("value")).write.format(
     "kafka").option("kafka.bootstrap.servers", kServer).
                      option("topic", topicOut).save()

  except Exception as e:
   print(str(e))
   pass

  b = time_py.time()
  c = (b - a)
  print(c)

 kvs.foreachRDD(process)
 ssc.start()
 ssc.awaitTermination()
