#!/bin/bash
chmod a+rw -R /var/data/mongodb/
chmod a+rw -R /var/log/mongodb/

sudo -u mongodb -g mongodb mongod --config /etc/mongodb.conf


