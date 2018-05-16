#!/bin/bash
cd ./influxdb_base
docker build -t karton91/influxdb_base .
cd ../influxdb
docker build -t karton91/influxdb .
cd ../kapacitor
docker build -t karton91/kapacitor .
cd ../chronograf
docker build -t karton91/chronograf .
cd ../telegraf
docker build -t karton91/telegraf .