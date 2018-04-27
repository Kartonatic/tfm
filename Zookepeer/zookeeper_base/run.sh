#!/bin/bash
cat /AddZooKeeperHost >> /etc/hosts
chmod a+rw -R /var/log/zookeeper/
sudo -u hdmaster -g hadoop $ZOOKEEPER_HOME/bin/zkServer.sh start-foreground
