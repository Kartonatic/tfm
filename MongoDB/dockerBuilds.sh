#!/bin/bash
cd ./mongodb_base
docker build -t karton91/mongodb_base .

cd ../mongodb_master
docker build -t karton91/mongodb_master .

cd ../mongoosm_master
docker build -t karton91/mongoosm_master .
