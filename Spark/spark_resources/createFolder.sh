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
