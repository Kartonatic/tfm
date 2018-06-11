#!/bin/bash
chmod a+rw -R /var/data/mongodb/
chmod a+rw -R /var/log/mongodb/

sudo -u mongodb -g mongodb mongod  --fork --config /etc/mongodb.conf

sudo -u mongodb -g mongodb python3 /opt/bd/mongodb/mongoUbicationServer.py
