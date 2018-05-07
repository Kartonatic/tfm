#!/bin/bash
cd ./hadoop_base
docker build -t karton91/hadoop_base276 .
cd ../hadoop_namenode
docker build -t karton91/hadoop_namenode276 .
cd ../hadoop_datanode
docker build -t karton91/hadoop_datanode276 .
cd ../hadoop_resourcemanager
docker build -t karton91/hadoop_resourcemanager276 .
cd ../hadoop_historyserver
docker build -t karton91/hadoop_historyserver276 .
cd ../hadoop_nodemanager
docker build -t karton91/hadoop_nodemanager276 .
cd ../hadoop_checkpointnode
docker build -t karton91/hadoop_checkpointnode276 .
cd ../hadoop_proxyserver
docker build -t karton91/hadoop_proxyserver276 .

