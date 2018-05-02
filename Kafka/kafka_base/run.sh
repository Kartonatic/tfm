#!/bin/bash
chmod a+rw -R /var/log/kafka/
sed -i "s/@id/-1/g" $KAFKA_HOME/config/server.properties
sed -i "s/@hostname/kafka/g" $KAFKA_HOME/config/server.properties
sudo -u queuesmaster -g queues $KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties