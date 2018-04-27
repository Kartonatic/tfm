#!/bin/bash
cat /AddkafkaHost >> /etc/hosts
chmod a+rw -R /var/log/kafka/
sed -i "s/@id/0/g" $KAFKA_HOME/config/server.properties
sed -i "s/@hostname/kafka3/g" $KAFKA_HOME/config/server.properties
sudo -u hdmaster -g hadoop $KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties