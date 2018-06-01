#!/bin/bash
chmod a+rw -R /var/data/mongodb/
chmod a+rw -R /var/log/mongodb/
chown mongodb:mongodb /mongosm-master
chmod a+rw -R /mongosm-master


sudo -u mongodb -g mongodb mongod --config /etc/mongodb.conf


