#!/bin/bash
cd ./zookeeper_base
docker build -t karton91/zookeeper_base .
cd ../zoo1
docker build -t karton91/zoo1 .
cd ../zoo2
docker build -t karton91/zoo2 .
cd ../zoo3
docker build -t karton91/zoo3 .


 docker push karton91/zookeeper_base
 docker push karton91/zoo1
 docker push karton91/zoo2
 docker push karton91/zoo3
