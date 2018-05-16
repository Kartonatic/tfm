#!/bin/bash
cd ./ELK_base
docker build -t karton91/elk_base .
cd ../elasticserach
docker build -t karton91/elasticserach .
cd ../kibana
docker build -t karton91/kibana .
cd ../logstash
docker build -t karton91/logstash .
