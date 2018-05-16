#!/bin/bash
chmod a+rw -R /var/data/influxdb/
chmod a+rw -R /var/log/influxdb/
chmod a+rw -R /var/lib/influxdb/

while true
do
	sleep 100000
done
