#!/bin/bash
chown -R hdmaster:hadoop /var/data/spark/
sleep 2
echo "wait spark"
sleep 2
echo "wait spark"
sleep 2
echo "wait spark"
sleep 2
echo "wait spark"
sleep 2
echo "wait spark"
sleep 2
echo "wait spark"
sleep 2
echo "wait spark"

if grep -q "False" /var/data/spark/isActive
then 
	sudo -u hdmaster -g hadoop /activeSpark.sh
	echo "True" > /var/data/spark/isActive
else 
	sudo -u hdmaster -g hadoop /opt/bd/streaming/spark/sbin/start-all.sh
	sudo -u hdmaster -g hadoop /opt/bd/streaming/spark/sbin/start-history-server.sh
fi


while true
do
	sleep 100000
done
