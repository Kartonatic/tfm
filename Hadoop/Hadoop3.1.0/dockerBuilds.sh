#!/bin/bash
cd ./hadoop_base
docker build -t karton91/hadoop_base310 .
cd ../hadoop_namenode
docker build -t karton91/hadoop_namenode310 .
cd ../hadoop_datanode
docker build -t karton91/hadoop_datanode310 .
cd ../hadoop_resourcemanager
docker build -t karton91/hadoop_resourcemanager310 .
cd ../hadoop_historyserver
docker build -t karton91/hadoop_historyserver310 .
cd ../hadoop_nodemanager
docker build -t karton91/hadoop_nodemanager310 .
cd ../hadoop_checkpointnode
docker build -t karton91/hadoop_checkpointnode310 .
cd ../hadoop_proxyserver
docker build -t karton91/hadoop_proxyserver310 .

