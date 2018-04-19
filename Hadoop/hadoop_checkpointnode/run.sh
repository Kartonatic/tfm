#!/bin/bash

chown -R hdmaster:hadoop /var/data/hadoop
chmod a+rw -R /var/data/hadoop
chown -R hdmaster:hadoop /var/log/hadoop/
chmod a+rw -R /var/log/hadoop/
sudo -u hdmaster -g hadoop $HADOOP_HOME/bin/hdfs namenode -checkpoint