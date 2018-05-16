#!/bin/bash
chmod a+rw -R /var/data/influxdb/
chmod a+rw -R /var/log/influxdb/
chmod a+rw -R /var/lib/influxdb/

sudo -u influxdb -g influxdb $INFLUXDB_HOME/usr/bin/influxd --config $INFLUXDB_HOME/etc/influxdb/influxdb.conf