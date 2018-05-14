cd ./UpdatedUbuntu
./dockerPulls.sh
cd ../Hadoop
cd Hadoop2.7.6
./dockerPulls.sh
cd ../Hadoop3.1.0
./dockerPulls.sh
 cd ../../Zookeeper
./dockerPulls.sh
cd ../Kafka
./dockerPulls.sh
cd ../Spark
./dockerPulls.sh
cd ../Flink
./dockerPulls.sh
cd ../ELK
./dockerPulls.sh
cd ../MongoDB
./dockerPulls.sh