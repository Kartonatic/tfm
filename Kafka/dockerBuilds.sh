#!/bin/bash
cd ./kafka_base
docker build -t karton91/kafka_base .
cd ../kafka1
docker build -t karton91/kafka1 .
cd ../kafka2
docker build -t karton91/kafka2 .
cd ../kafka3
docker build -t karton91/kafka3 .


# docker push karton91/kafka_base
# docker push karton91/kafka1
# docker push karton91/kafka2
# docker push karton91/kafka3
