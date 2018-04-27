#!/bin/bash
cat /AddZooKeeperHost >> /etc/hosts
chmod a+rw -R /var/log/zookeeper/
echo 1 >> /var/data/zookeeper/myid
sudo chown -R hdmaster:hadoop /var/data/zookeeper
sudo chown -R hdmaster:hadoop /var/log/zookeeper
sudo -u hdmaster -g hadoop $ZOOKEEPER_HOME/bin/zkServer.sh start-foreground
