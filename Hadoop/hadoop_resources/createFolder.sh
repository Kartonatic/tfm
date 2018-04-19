rm -r datanode1
rm -r datanode2
rm -r datanode3
rm -r historyserver
rm -r namenode

mkdir historyserver
mkdir namenode
mkdir namenode/nn namenode/cpn namenode/dn 
echo False > namenode/isActive
mkdir datanode1
mkdir datanode1/nn datanode1/cpn datanode1/dn
mkdir datanode2
mkdir datanode2/nn datanode2/cpn datanode2/dn
mkdir datanode3
mkdir datanode3/nn datanode3/cpn datanode3/dn 
