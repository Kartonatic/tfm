#!/bin/bash
cd ./flink_base
docker build -t karton91/flink_base .
cd ../flink_master
docker build -t karton91/flink_master .
cd ../flink_worker
docker build -t karton91/flink_worker .
