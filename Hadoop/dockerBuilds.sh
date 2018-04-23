#!/bin/bash
cd ./hadoop_base
docker build -t karton91/hadoop_base .
cd ../hadoop_namenode
docker build -t karton91/hadoop_namenode .
cd ../hadoop_datanode
docker build -t karton91/hadoop_datanode .
cd ../hadoop_resourcemanager
docker build -t karton91/hadoop_resourcemanager .
cd ../hadoop_historyserver
docker build -t karton91/hadoop_historyserver .
cd ../hadoop_nodemanager
docker build -t karton91/hadoop_nodemanager .
cd ../hadoop_checkpointnode
docker build -t karton91/hadoop_checkpointnode .
cd ../hadoop_proxyserver
docker build -t karton91/hadoop_proxyserver .

# docker push karton91/hadoop_base
# docker push karton91/hadoop_namenode
# docker push karton91/hadoop_datanode
# docker push karton91/hadoop_resourcemanager
# docker push karton91/hadoop_historyserver
# docker push karton91/hadoop_nodemanager 
# docker push karton91/hadoop_checkpointnode
# docker push karton91/hadoop_proxyserver
