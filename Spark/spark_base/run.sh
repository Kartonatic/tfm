#!/bin/bash
# sudo -u hdmaster -g hadoop /opt/spark/spark-shell

trap 'touch /home/spark/salirr' SIGINT
trap 'touch /home/spark/salirrSIGKILL' SIGKILL
trap 'touch /home/spark/salirrSIGTERM' SIGTERM

while true
do
	sleep 100000
done
