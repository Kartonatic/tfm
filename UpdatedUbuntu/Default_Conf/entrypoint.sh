#!/bin/bash

service ssh start

cat /AddHosts >> /etc/hosts

# We need put exec $@ 
# to execute param on dokcer run or 
# in docker file CMD
exec $@