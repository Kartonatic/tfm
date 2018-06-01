#!/bin/bash
chmod a+rw -R /var/data/mongodb/
chmod a+rw -R /var/log/mongodb/
chmod a+rwx -R /var/run/mongodb  # location of pidfile
chmod a+rwx -R /usr/share/
while true
do
	sleep 100000
done
