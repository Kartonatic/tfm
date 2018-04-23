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
