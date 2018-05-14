Este es el Trabajo de Fin de Master que estoy haciendo...

Estoy ahora intentando montar una arquitectura lambda. 

EVOLUCION DEL PROYECTO:

	- UBUNTU 16.04 (actualizado, con java 8 y scala 2.12. Ademas ssh a traves de certificado)

	- HADOOP 3.1.0 aunque si esta tambien la 2.7.6

	- ZOOKEEPER 3.4.10

	- KAFKA 1.1.0

	- SPARK 2.3.0

	- FLINK 1.4.2 

	- ELK 6.2.4 (Elasticsearh, Kibana  and Logstash)
	
	- MONGODB (instalado con apt-get install mongodb)

¿Por qué es bueno tener este tipo de arquitecturas, además con docker?

	- Son muy flexibles. Podemos cambiar cualquiera de los componentes cuando queramos. Imaginamos que en vez de spark podemos cambiar... solo tenenmos que rehacer el codigo de spark. 

	- Si queremos cambiar una base de datos, solo tenemos que cambiar el codigo de la base de datos mientras que los demás componentes permanecen inmutables. 

	- Son realmente rapidos.

	- Son facilmente replicables.

	- Son altamente escalables. Siempre que queramos añadirle espacio o potencia, solo tenemos que añadir una nueva maquina.

	- ¿Y docker? Es muy facil de usar y ocupa muy poco espacio. Realmente el objetivo final es usar kubernetes ya que podemos añadir nuevas maquinas de una forma muy facil.

¿Como se conecta entre si los containers y como contectarse desde localhost?

	- Se ha instalado ssh a traves de certificado. Para generar el certificado hay que renovar la capa de ubuntu que genera un nuevo certificado. Si obtenemos ese certificado
		y lo guardamos en local podemos acceder a las maquinas. 

	- Una parte buena de este cluster es que podemos acceder a cualquier maquina si sabemos su IP ya que todas las maquinas contienen dicho certificado.


¿Como se mantiene la información?

	- Para mantener la información he creado diferentes volumenes que con el docker-compose se mapearan a su correspondiente carpeta con el nombre de la teconologia y '_resources'. 
		Gracias a esto, la información se mantendrá cada vez que hagamos docker-compose up

¿Como se configura cada tecnologia?

	- He creado un sistema que nos permite configurar una base y despues configurar los diferentes roles de cada container.

	- En cada carpeta '_base' se encuentra una carpeta Default_Conf donde se encuentra la configuracion basica que podemos modificar para cada 
		tecnologia. Por ejemplo, en hadoop tendriamos los ficheros de <path_hadoop>/etc/hadoop

¿Existe alguna forma automatica de generar los container y sus directorios de persistencia?
	
	- Se han creado una jerarquia de scripts que nos permite esto. El script dockerBuilds.sh de cada directorio generará el container, el script dockerPulls.sh subirá los 
		container a docker hub y el script createFolders.sh llamará al script createFolder.sh de cada carpeta '_resources' de cada tecnologia (dicho script genera las carpetas necesarias
		para la persistencia).

HOSTS:

172.28.0.2	namenode

172.28.0.3	resourcemanager

172.28.0.4	historyserver

172.28.0.5	checkpointnode

172.28.0.6	nodemanager

172.28.0.7	proxyserver

172.28.0.8	datanode1

172.28.0.9	datanode2

172.28.0.10	datanode3

172.28.0.11	zoo1

172.28.0.12	zoo2

172.28.0.13	zoo3

172.28.0.14	kafka1

172.28.0.15	kafka2

172.28.0.16	kafka3

172.28.0.17	sparkmaster

172.28.0.18	sparkworker1

172.28.0.19	sparkworker2

172.28.0.20	sparkworker3

172.28.0.21     flinkmaster

172.28.0.22     flinkworker1

172.28.0.23     flinkworker2

172.28.0.24     flinkworker3

172.28.0.25     elasticsearch

172.28.0.26     kibana

172.28.0.27     logstash

172.28.0.28     mongomaster


Docker (AVISO: COMO TOPE HAY 150 LAYERS):

Ubuntu_base:

[![](https://images.microbadger.com/badges/image/karton91/ubuntu_base.svg)](https://microbadger.com/images/karton91/ubuntu_base.svg "Ubuntu 16.04 updated")

[![](https://images.microbadger.com/badges/version/karton91/ubuntu_base.svg)](https://microbadger.com/images/karton91/ubuntu_base.svg "Ubuntu 16.04 updated")


Hadoop_base:

[![](https://images.microbadger.com/badges/image/karton91/hadoop_base310.svg)](https://microbadger.com/images/karton91/hadoop_base310 "HADOOP 3.1.0")

[![](https://images.microbadger.com/badges/version/karton91/hadoop_base310.svg)](https://microbadger.com/images/karton91/hadoop_base310 "HADOOP 3.1.0")


Zookeeper_base:

[![](https://images.microbadger.com/badges/image/karton91/zookeeper_base.svg)](https://microbadger.com/images/karton91/zookeeper_base "ZOOKEEPER 3.4.1")

[![](https://images.microbadger.com/badges/version/karton91/zookeeper_base.svg)](https://microbadger.com/images/karton91/zookeeper_base "ZOOKEEPER 3.4.1")


Kafka_base:

[![](https://images.microbadger.com/badges/image/karton91/kafka_base.svg)](https://microbadger.com/images/karton91/kafka_base "KAFKA 1.1.0")

[![](https://images.microbadger.com/badges/version/karton91/kafka_base.svg)](https://microbadger.com/images/karton91/kafka_base "KAFKA 1.1.0")


Spark_base:

[![](https://images.microbadger.com/badges/image/karton91/spark_base.svg)](https://microbadger.com/images/karton91/spark_base "SPARK 2.3.0")

[![](https://images.microbadger.com/badges/version/karton91/spark_base.svg)](https://microbadger.com/images/karton91/spark_base "SPARK 2.3.0")


Flink_base:

[![](https://images.microbadger.com/badges/image/karton91/flink_base.svg)](https://microbadger.com/images/karton91/flink_base "FLINK 1.4.2")

[![](https://images.microbadger.com/badges/version/karton91/flink_base.svg)](https://microbadger.com/images/karton91/flink_base "FLINK 1.4.2")



ELK_base:

[![](https://images.microbadger.com/badges/image/karton91/elk_base.svg)](https://microbadger.com/images/karton91/elk_base "ELK 6.2.4")

[![](https://images.microbadger.com/badges/version/karton91/elk_base.svg)](https://microbadger.com/images/karton91/elk_base "ELK 6.2.4")


MongoDB_base:

[![](https://images.microbadger.com/badges/image/karton91/mongodb_base.svg)](https://microbadger.com/images/karton91/mongodb_base "MONGODB")

[![](https://images.microbadger.com/badges/version/karton91/mongodb_base.svg)](https://microbadger.com/images/karton91/mongodb_base "MONGODB")

This is my Master's Thesis...

Now, I'm make a cluster with docker to do a lambda arquitecture.

EVOLUTION OF THE PROYECT:


	- UBUNTU 16.04 (S.O updated with java 8, scala 2.12 and ssh with certificate)

	- HADOOP 3.1.0 and, if you need, I put 2.7.6 version

	- ZOOKEEPER 3.4.10

	- KAFKA 1.1.0

	- SPARK 2.3.0

	- FLINK 1.4.2 

	- ELK 6.2.4 (Elasticsearh, Kibana  and Logstash)
	
	- MONGODB (installed with apt-get install mongodb)
