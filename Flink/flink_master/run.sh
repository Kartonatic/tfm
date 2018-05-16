#!/bin/bash

echo wait flink
sleep 10
echo wait flink
sleep 4
echo wait flink
sleep 4

chown -R hdmaster:hadoop /var/data/flink/

sudo -u hdmaster -g hadoop /opt/bd/streaming/flink/bin/start-cluster.sh
sudo -u hdmaster -g hadoop /opt/bd/streaming/flink/bin/historyserver.sh start
sudo -u hdmaster -g hadoop /opt/bd/streaming/flink/bin/jobmanager.sh start cluster

while true
do
	sleep 100000
done
