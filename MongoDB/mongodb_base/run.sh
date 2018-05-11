#!/bin/bash
chmod a+rw -R /var/data/mongodb/
chmod a+rw -R /var/log/mongodb/

mongod --config /etc/mongodb.conf


while true
do
	sleep 100000
done
