#!/bin/bash
cd ./spark_base
docker build -t karton91/spark_base .
cd ./Light_version
docker build -t karton91/spark_light .
cd ../../spark_master
docker build -t karton91/spark_master .
cd ../spark_worker
docker build -t karton91/spark_worker .

