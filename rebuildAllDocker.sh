cd ./UpdatedUbuntu
./dockerBuilds.sh
cd ../Hadoop
cd Hadoop2.7.6
./dockerBuilds.sh
cd ../Hadoop3.1.0
./dockerBuilds.sh
 cd ../../Zookeeper
./dockerBuilds.sh
cd ../Kafka
./dockerBuilds.sh
cd ../Spark
./dockerBuilds.sh