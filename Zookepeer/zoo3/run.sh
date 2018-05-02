#!/bin/bash
chmod a+rw -R /var/log/zookeeper/
echo 3 >> /var/data/zookeeper/myid
sudo chown -R zkmaster:zk /var/data/zookeeper
sudo chown -R zkmaster:zk /var/log/zookeeper
cd $ZOOKEEPER_HOME && sudo -u zkmaster -g zk ./bin/zkServer.sh start-foreground