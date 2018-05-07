#!/bin/bash

service ssh start

cat /AddHosts >> /etc/hosts

chown -R hdmaster:hadoop /var/data/hadoop/hdfs

# We need put exec $@ 
# to execute param on dokcer run or 
# in docker file CMD
exec $@