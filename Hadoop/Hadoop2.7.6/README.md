HADOOP 2.7.6

Este es el cluster hadoop: 

	- Hay 3 datanodes y los diferentes servicios (namenode, checkpointnode (secondarynamenode), nodemanager, historyserver, resourcemanager, proxyserver).
	- En el directorio hadoop_resoruces estan los directorios donde se van a generar los volumenes. Si no existen seguir las instrucciones del README.

Ejecutar dockerBuilds.sh y luego hacer docker-compose up.

AÑADIR A TU /etc/hosts LAS DIRECCIONES DE tfm/Hadoop/hadoop_base/Default_Conf/AddHosts/AddHosts

NOTA: Podriamos meter un DNS para sustituir en el docker-compose el hostname por nombres y que el dns los interpretara. 

This is my hadoop cluster:
	- On this cluster we have 3 datanodes and the other services of hadoop (namenode, checkpointnode (secondarynamenode), nodemanager, historyserver, resourcemanager, proxyserver).
	- On hadoop_resoureces direcotry please, read README to configure cluster. 

ADD TO YOUR /etc/hosts FILE THE IPs IN tfm/Hadoop/hadoop_base/Default_Conf/AddHosts/AddHosts