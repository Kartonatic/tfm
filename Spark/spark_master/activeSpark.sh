#!/bin/bash
cd /opt/bd/streaming/spark/jars
zip -r spark-archives.zip .
echo $HADOOP_HOME
echo $SPARK_HOME
/opt/bd/hadoop/bin/hadoop fs -mkdir /user
/opt/bd/hadoop/bin/hadoop fs -mkdir /user/hdmaster 
/opt/bd/hadoop/bin/hadoop fs -put ./spark-archives.zip /user/hdmaster/spark-archives.zip
/opt/bd/hadoop/bin/hadoop fs -mkdir /user/hdmaster/spark-logs
rm spark-archives.zip
../sbin/start-all.sh
../sbin/start-history-server.sh