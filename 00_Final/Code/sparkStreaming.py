from __future__ import print_function

import sys
import json

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import Row, SparkSession
#spark sql function for columns
from pyspark.sql.functions import col, expr, to_json, struct, format_number, \
                                  monotonically_increasing_id, udf, unix_timestamp, \
                                  from_unixtime, datediff, array #current_date para fecha actual cuando este en produccion
from pyspark.sql.types import *
#math spark sql function 
from pyspark.sql.functions import acos, cos, sin, lit, radians
#Usamos pymongo porque no carga la collecion en memoria (la libreria que usa spark si lo hace)
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
Obtiene los datos del usuario con un singleton
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
        users = spark.read.csv("Users.csv", header=True, schema = sch_user)
        userSensor = spark.read.csv("UserSensor.csv", header=True, schema=sch_sen_user)

        #Join data form hdfs
        joinUserSensor = users.alias('user').join(userSensor.alias('sensors'), col('user.id_user') == col('sensors.user'))

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
        blk_shp = spark.read.csv("blackshapes.csv", header=True, schema = sch_blk_shp)
        blk_shp = blk_shp.withColumn("lat_min", (format_number(blk_shp.lat, 3) - 0.005).cast(FloatType())).\
                withColumn("lat_max", (format_number(blk_shp.lat, 3) + 0.005).cast(FloatType())).\
                withColumn("long_min", (format_number(blk_shp.long, 3) - 0.005).cast(FloatType())).\
                withColumn("long_max", (format_number(blk_shp.long, 3) + 0.005).cast(FloatType()))

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

#   bearing = atan2(sin(long2-long1)*cos(lat2), cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(long2-long1))
#   bearing = degrees(bearing)
#   bearing = (bearing + 360) % 360


'''
Obtener datos de OSM
'''
def getWay(lat, long, waysConnection):
    try:
        query = waysConnection.find({ "$and": [ {"loc": { "$near": [lat, long], "$maxDistance": 0.01 } }, 
                                  { "$and": [ {"tg" : {'$elemMatch':{'$elemMatch':{'$in':['highway']}}}},
                                            {"tg" : {'$elemMatch':{'$elemMatch':{'$in':['motorway', 'trunk', 'primary',
                                                                                       'secundary', 'tertiary',
                                                                                       'unclassified', 'residential',
                                                                                       'service', 'road'
                                                                                       ]
                                                                                }
                                                                  }
                                                    }
                                            }
                                            ]
                                  }
                                ]} ).limit(1)
        if (query.count(with_limit_and_skip=True))>0:
            return query[0]
        return None
    except:
        return None

#Datos de velocidad
carLimit = {
    'motorway' : 120,
    'trunk' : 100,
    'primary' : 100,
    'secundary' : 90,
    'tertiary' : 90,
    'unclassified' : 60,
    'residential' : 30,
    'service' : 50,
    'road' : 80
}

busLimit = {
    'motorway' : 100,
    'trunk' : 90,
    'primary' : 90,
    'secundary' : 80,
    'tertiary' : 80,
    'unclassified' : 60,
    'residential' : 30,
    'service' : 50,
    'road' : 80
}

truckLimit = {
    'motorway' : 100,
    'trunk' : 90,
    'primary' : 90,
    'secundary' : 70,
    'tertiary' : 70,
    'unclassified' : 60,
    'residential' : 30,
    'service' : 50,
    'road' : 80
}

'''
Obtener los datos que nos interesan de mongodb
'''
def getInfo(query):
    speedLimit = 120
    tagSpeed=False
    tafRef = False
    name = ""
    try:
        if (query is None):
            return (name, speedLimit)
        for i in query['tg']:
            if ("maxspeed" == i[0]):
                speedLimit = int(i[1])
                tagSpeed = True
            elif ("highway" == i[0]):
                if not tagSpeed:
                    speedLimit = carLimit.get(i[1], 120)
            elif ("name" in i[0]):
                if not tagSpeed:
                    name = i[1]
            elif ("ref" in i[0]):
                name = i[1]
        return (name, speedLimit)
    except:
        return (name, speedLimit)

'''
Funcion que pasaremos por el udf que obtiene los datos de mongo OSM
Hay que pasarle las columnas latitud y longitud
'''
def reference_to_dict(l):
    d = []
    if ((l[0] is not None) and (l[1] is not None)):
        client = MongoClient("mongomaster", 27017)
        db = client.osm
        ways = db.ways
        d = getInfo(getWay(l[0], l[1], ways))
        client.close()
        return [d[0], d[1]]
    else:
        return []


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
        #2018-05-28T13:52:07.0000000Z,2018-05-28T13:52:35.6721175Z
        format_1 = "yyyy-MM-dd'T'HH:mm:ss.SSSSSSS'Z'"

        try:
            # Get the singleton instance of SparkSession
            if (not rdd.isEmpty()):
                spark = getSparkSessionInstance(rdd.context.getConf())

                # Get data from kafka json to df
                df = spark.read.json(rdd.map(lambda x: x[1]))
                print(df.count())

                df = df.withColumn('observationDate', from_unixtime(unix_timestamp('observationTime', format_1))).\
                         withColumn('serverDate', from_unixtime(unix_timestamp('serverTime', format_1)))
                #Usa current_date(), col("observationDate") en produccion
                df = df.where(datediff(col("serverTime"), col("observationDate")) < 7)
                print(df.count())

                joinUserSensor = getDataUsers(rdd.context)

                # join data from hdfs and stream
                joinData = df.alias('stream').join(joinUserSensor.alias('data'), col('stream.sensorId') == col('data.sensorId'),"leftOuter") # can be "inner", "leftOuter", "rightOuter"

                dataToSend = joinData.select("Type","altitude","coordinates_lat","coordinates_long","date","observationTime","observationDate","dateSend", "serverDate", "heading","location","stream.sensorId","serverTime","speed","speedmetric","temp","id_user", "name")
                dataToSend = dataToSend.withColumn("id", monotonically_increasing_id())

                #Convertimos la funcion en udf
                schema4udf = StructType([StructField("addrs_name", StringType()),
                                            StructField("max_speed", IntegerType())
                                        ])
                reference_to_dict_udf = udf(reference_to_dict, schema4udf)

                #Obtenemos la georeferenciacion
                dataToSend = dataToSend.withColumn("data_osm", reference_to_dict_udf(struct([dataToSend[x] for x in ['coordinates_lat','coordinates_long']])))
                dataToSend = dataToSend.select("id", "Type","altitude","coordinates_lat","coordinates_long","date","observationTime","observationDate","dateSend", "serverDate",
                                   "serverTime","heading","location","stream.sensorId","speed",
                                   "speedmetric","temp","id_user", "name", col("data_osm.addrs_name").alias("addrs_name"), col("data_osm.max_speed").alias("max_speed") )

                
                #actualCoordinates = dataToSend.rdd.map(lambda x: (x['id'], x['coordinates_lat'], x['coordinates_long'])).toDF(["id", "coordinates_lat","coordinates_long"])
                actualCoordinates = dataToSend.select("id", "coordinates_lat","coordinates_long")
                # Cargamos los puntos negros
                blackShapes = getBlackShapes(rdd.context)
                # Los cruzamos con las posiciones actuales de los vehiculos
                nearBlkShp = actualCoordinates.crossJoin(blackShapes)
                # Obtenemos solo los puntos mas cercanos a ~1km de distancia
                # How to find the most near position efficient?
                # https://gis.stackexchange.com/questions/8650/measuring-accuracy-of-latitude-and-longitude?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
                nearBlkShp = nearBlkShp.filter((nearBlkShp.lat_min <= nearBlkShp.coordinates_lat) & (nearBlkShp.lat_max >= nearBlkShp.coordinates_lat) & (nearBlkShp.long_min <= nearBlkShp.coordinates_long) & (nearBlkShp.long_max >= nearBlkShp.coordinates_long))
                #Obtenemos las distancias a los puntos negros
                nearBlkShp = nearBlkShp.select(col("id"), col("Address"), # col("coordinates_lat"), col("coordinates_long"), NOT NECESSARY
                    col("Province"), col("Country"), col("numAccident"), col("lat").alias("blk_point_lat"), col("long").alias("blk_point_long"),
                    dist(col('coordinates_lat'),col('coordinates_long'),col('lat'),col('long')).alias("Distance"))
                #Nos quedamos con la menor
                minD4 = nearBlkShp.groupBy("id").min("Distance")
                #Ahora obtenemos los que tienen solo menor distancia
                finalNearBlkShp = minD4.alias('mins').join(nearBlkShp.alias('dataBlkShp'), 
                    (col('mins.id')==col('dataBlkShp.id')) & (col('mins.min(Distance)') == col('dataBlkShp.Distance')),"leftOuter").\
                    select(col("dataBlkShp.id").alias('id'), 
                    col("dataBlkShp.Address").alias('address'),
                    col("dataBlkShp.Province").alias('province'), col("dataBlkShp.Country").alias('country'), col("dataBlkShp.numAccident").alias('accidents'), 
                    col("dataBlkShp.blk_point_lat").alias('blk_point_lat'), col("dataBlkShp.blk_point_long").alias('blk_point_long'), col("dataBlkShp.Distance").alias('dist_to_blk_shp'))

                #Join de los puntos negros con los datos 
                dataToSend = dataToSend.alias('data').join(finalNearBlkShp.alias('blk_shp'), col('data.id')==col('blk_shp.id'), "leftOuter")
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
                                               col("data.id_user").alias("id_user"),
                                               col("data.name").alias("user"),
                                               col("data.addrs_name").alias("actual_address"),
                                               col("data.max_speed").alias("max_speed"),
                                               col("blk_shp.address").alias("blk_shp_address"),
                                               col("blk_shp.province").alias("blk_shp_province"),
                                               col("blk_shp.country").alias("blk_shp_country"),
                                               col("blk_shp.accidents").alias("blk_shp_accidents"),
                                               array(col('blk_shp.blk_point_lat'),col('blk_shp.blk_point_long')).alias("blk_shp_coordinates"),
                                               col("blk_shp.dist_to_blk_shp").alias("blk_shp_dist")
                                              )
                dataToSend.orderBy("blk_shp.Province", ascending=False).show()

                #Send data
                dataToSend.printSchema()
                dataToSend.select(to_json(struct([dataToSend[x] for x in dataToSend.columns])).alias("value")).write.format("kafka").option("kafka.bootstrap.servers", "kafka1:9092,kafka2:9092,kafka3:9092").option("topic", topicOut).save()

        except Exception as e:
            print(str(e))
            pass

    kvs.foreachRDD(process)
    ssc.start()
    ssc.awaitTermination()
