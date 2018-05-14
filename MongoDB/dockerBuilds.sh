#!/bin/bash
cd ./mongodb_base
docker build -t karton91/mongodb_base .

cd ../mongodb_master
docker build -t karton91/mongodb_master .
