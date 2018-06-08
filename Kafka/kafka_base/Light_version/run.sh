#!/bin/bash
chmod a+rw -R /var/log/kafka/
sed -i "s/@id/0/g" $KAFKA_HOME/config/server.properties
sed -i "s/@hostname/kafka1/g" $KAFKA_HOME/config/server.properties
cd $KAFKA_HOME && sudo -u hdmaster -g hadoop ./bin/kafka-server-start.sh ./config/server.properties