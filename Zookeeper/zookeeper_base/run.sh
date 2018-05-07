#!/bin/bash
chmod a+rw -R /var/log/zookeeper/
sudo -u zkmaster -g zk $ZOOKEEPER_HOME/bin/zkServer.sh start-foreground
