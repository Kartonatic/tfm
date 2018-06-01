cd ..
mkdir -p hadoop_resources
cd hadoop_resources


rm -r namenode
rm -r datanode1
rm -r datanode2
rm -r datanode3
rm -r historyserver
rm -r resourcemanager
rm -r nodemanager
rm -r checkpointnode
rm -r proxyserver

mkdir -p namenode
mkdir -p namenode/hdfs
mkdir -p namenode/hdfs/nn namenode/hdfs/cpn namenode/hdfs/dn 
echo False > namenode/hdfs/isActive
mkdir -p namenode/log
mkdir -p namenode/log/yarn namenode/log/hdfs namenode/log/mapred

mkdir -p datanode1
mkdir -p datanode1/hdfs
mkdir -p datanode1/hdfs/nn datanode1/hdfs/cpn datanode1/hdfs/dn
mkdir -p datanode1/log
mkdir -p datanode1/log/yarn datanode1/log/hdfs datanode1/log/mapred

mkdir -p datanode2
mkdir -p datanode2/hdfs
mkdir -p datanode2/hdfs/nn datanode2/hdfs/cpn datanode2/hdfs/dn
mkdir -p datanode2/log
mkdir -p datanode2/log/yarn datanode2/log/hdfs datanode2/log/mapred

mkdir -p datanode3
mkdir -p datanode3/hdfs
mkdir -p datanode3/hdfs/nn datanode3/hdfs/cpn datanode3/hdfs/dn 
mkdir -p datanode3/log
mkdir -p datanode3/log/yarn datanode3/log/hdfs datanode3/log/mapred

mkdir -p historyserver
mkdir -p historyserver/log
mkdir -p historyserver/log/yarn historyserver/log/hdfs historyserver/log/mapred

mkdir -p resourcemanager
mkdir -p resourcemanager/log
mkdir -p resourcemanager/log/yarn resourcemanager/log/hdfs resourcemanager/log/mapred

mkdir -p nodemanager
mkdir -p nodemanager/log
mkdir -p nodemanager/log/yarn nodemanager/log/hdfs nodemanager/log/mapred

mkdir -p proxyserver
mkdir -p proxyserver/log
mkdir -p proxyserver/log/yarn proxyserver/log/hdfs proxyserver/log/mapred

mkdir -p checkpointnode
mkdir -p checkpointnode/hdfs
mkdir -p checkpointnode/hdfs/nn checkpointnode/hdfs/cpn checkpointnode/hdfs/dn
mkdir -p checkpointnode/log
mkdir -p checkpointnode/log/yarn checkpointnode/log/hdfs checkpointnode/log/mapred

cd ..
chmod a+rw -R hadoop_resources
mkdir -p zookeeper_resources
cd zookeeper_resources


rm -r zookeeper
rm -r zoo1
rm -r zoo2
rm -r zoo3

mkdir -p zookeeper
mkdir -p zookeeper/data
mkdir -p zookeeper/log

mkdir -p zoo1
mkdir -p zoo1/data
mkdir -p zoo1/log

mkdir -p zoo2
mkdir -p zoo2/data
mkdir -p zoo2/log

mkdir -p zoo3
mkdir -p zoo3/data
mkdir -p zoo3/log

cd ..
chmod a+rw  -R zookeeper_resources
mkdir -p kafka_resources
cd kafka_resources


rm -r kafka
rm -r kafka1
rm -r kafka2
rm -r kafka3

mkdir -p kafka
mkdir -p kafka/log

mkdir -p kafka1
mkdir -p kafka/log

mkdir -p kafka2
mkdir -p kafka/log

mkdir -p kafka3
mkdir -p kafka3/log


cd ..
chmod a+rw  -R kafka_resources
mkdir -p spark_resources
cd spark_resources

rm -r spark
rm -r spark_master
rm -r spark_worker1
rm -r spark_worker2
rm -r spark_worker3

mkdir -p spark
mkdir -p spark/data
mkdir -p spark/data/shuffle_rdd spark/data/worker spark/data/zoo 


mkdir -p spark_master
mkdir -p spark_master/data
mkdir -p spark_master/data/shuffle_rdd spark_master/data/worker spark_master/data/zoo 
echo False > spark_master/data/isActive

mkdir -p spark_worker1
mkdir -p spark_worker1/data
mkdir -p spark_worker1/data/shuffle_rdd spark_worker1/data/worker spark_worker1/data/zoo 

mkdir -p spark_worker2
mkdir -p spark_worker2/data
mkdir -p spark_worker2/data/shuffle_rdd spark_worker2/data/worker spark_worker2/data/zoo 

mkdir -p spark_worker3
mkdir -p spark_worker3/data
mkdir -p spark_worker3/data/shuffle_rdd spark_worker3/data/worker spark_worker3/data/zoo 



cd ..
chmod a+rw  -R spark_resources
mkdir -p ELK_resources
cd ELK_resources


rm -r elasticsearch
rm -r kibana
rm -r logstash

mkdir -p elasticsearch
mkdir -p elasticsearch/data elasticsearch/log

mkdir -p kibana
mkdir -p kibana/data kibana/log

mkdir -p logstash
mkdir -p logstash/data logstash/log


cd ..
chmod a+rw  -R elasticsearch