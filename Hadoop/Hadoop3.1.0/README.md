HADOOP 3.1.0

Este es el cluster hadoop:

	- La imagen base hereda de ubuntu_base

	- Hay 3 datanodes y los diferentes servicios (namenode, checkpointnode (secondarynamenode), nodemanager, historyserver, resourcemanager, proxyserver).
		Cada uno de ellos se ha configurado para ser arrancado de forma automatica y comunicarse entre ellos. 

	- En el directorio hadoop_resoruces estan los directorios donde se van a generar los volumenes. Si no existen seguir las instrucciones del README.
		Gracias a esto, conseguiremos la persistencia aunque se caigan los nodos o se reinicien los cluster (como podria ser el caso de añadir una
		actualizacion de hadoop).

	- La version en produccion se encuentra en /opt/bd/hadoop (es un link a hadoop-3.1.0 en la misma carpeta). De esta forma cuando queramos actualizar solo
		tendremos que cambiar dicho link a la version superior.

	- Toda la configuracion se encuentra en Default_Conf. AddHost contiene las direcciones para el DNS (mirar docker-compose.yml) y en hadoop3.1.0 esta la configuracion
		del cluster. Se han modificado los ficheros: 
			
			- core-site.xml

			- hadoop-env.sh

			- hdfs-site.xml

			- mapred-site.xml

			- mapred-env.sh

			- yarn-site.xml

			- yarn-env.sh

			- workers (no se usa porque no lanzo los demonios que lo usan)


Ejecutar dockerBuilds.sh y luego hacer docker-compose up.


IMPORTANTE:
	- AÑADIR A TU /etc/hosts LAS DIRECCIONES DE tfm/Hadoop/hadoop_base/Default_Conf/AddHosts/AddHosts si quieres que funcionen correctamente las url y la interfaz grafica

NOTA: Podriamos meter un DNS para sustituir en el docker-compose el hostname por nombres y que el dns los interpretara. 


This is my hadoop cluster:

	- On this cluster we have 3 datanodes and the other services of hadoop (namenode, checkpointnode (secondarynamenode), nodemanager, historyserver, resourcemanager, proxyserver).

	- On hadoop_resoureces direcotry please, read README to configure cluster. 

ADD TO YOUR /etc/hosts FILE THE IPs IN tfm/Hadoop/hadoop_base/Default_Conf/AddHosts/AddHosts