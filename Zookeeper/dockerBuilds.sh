#!/bin/bash
cd ./zookeeper_base
docker build -t karton91/zookeeper_base .
cd ./Light_version
docker build -t karton91/zookeeper_light .
cd ../../zoo1
docker build -t karton91/zoo1 .
cd ../zoo2
docker build -t karton91/zoo2 .
cd ../zoo3
docker build -t karton91/zoo3 .
