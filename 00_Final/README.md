Si es la primera vez que lanzas este proyecto, debes lanzar el script:

	- cd ToGenerateFolders
	- ./createFoldersFromGit.sh 

Para usar este proyecto debemos de lanzar lo siguiente:

	- sudo sysctl -w vm.max_map_count=262144

	- docker-compose up


Revisar que ninguna maquina esté caida, en caso de que se haya caido alguna probar a apagarlas y usar docker-compose rm y luego docker-compose up (esto podria pasar si es la primera vez que las lanzas).

Si es la primera vez que lo ejecutas (y solo si es la primera vez) lanza el script 'CreateIndexForElastic.py' con python3 para crear el indice en elasticsearch cuando las maquinas estén creadas. También tendrás que meter los ficheros Users.csv y UserSensor.csv en el directorio ./spark_resources/spark_master/data/

Una vez tenemos las maquinas en vuelo nos meteremos en spark y loghstash para lanzar los scripts correspondientes:
	
	- docker exec -it sparkmaster /bin/bash
		
		- su hdmaster

		- Si es la primera vez que vas a usarlo necesitaras subir los csv correspondientes al hdfs:

			- cd /var/data/spark

			- Aqui tendremos que tener los ficheros Users.csv, UserSensor.csv y blackshapes.csv que subiremos a hadoop

				- Para esto podemos meter los ficheros (que se encuentran en Data) en el directorio spark_resources/spark_master/data/

			- hadoop fs -put Users.csv

			- hadoop fs -put UserSensor.csv

                        - hadoop fs -put blackshapes.csv

		- cd ~/streaming/spark

		- # Ahora pegamos sparkStreaming.py que hay en nuestro git en el directorio Code (podemos hacerlo con nano sparkStreaming.py pegando el codigo)

		- # Ahora lanzamos spark streaming (recuerda que si quieres lanzarlo en vez de con yarn con las maquinas spark puedes usar el parametro --master spark://sparkmaster:7077):

		- spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0,org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.0  sparkStreaming2.py zoo1,zoo2,zoo3 streamKafka sparkOut

	- Existe otra version con spark struct streaming que se ha testeado:

		- o tambien podemos probar la version de pruebas con spark struct streaming añadiendo sparkStructStream.py

		- spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.0  sparkStructStream.py kafka1:9092,kafka2:9092,kafka3:9092 subscribe streamKafka 

	
	- # Ahora ya tenemos spark streaming en vuelo 

	
	- docker exec -it logstash /bin/bash
		
		- su elastic

		- cd ~/logstash

		- # Ahora pegamos logstashkafka.conf que hay en nuestro git en el directorio 00_Final/Code/Logstash/ (podemos hacerlo con nano logstashkafka.conf pegando el yaml)

		- # Tambien se ha creado una version que actualiza las posiciones de los vehiculos: logstashkafkaUpdates.conf

		- logstash -f logstashkafka.conf

Una vez hecho esto empezaremos a mandar mensajes (trafico) a la cola kafka con el script 'sendTraffic.py' de python3.

Ahora configuraremos kibana:

	- Nos vamos a la pestaña de Management y le damos a IndexPatterns.

	- Seleccionamos car_gps y pasamos a next step

	- En este caso vamos a usar @timestamp como timeFilter ya que es el proposito del tfm y le damos a create index

	- Ahora podemos ver nuestros datos en discover

Si queremos exportar el dashboard en kibana tenemos que hacer lo siguiente:

	- Nos vamos a la pestaña de Management y le damos a Save Objects.
	
	- Pinchamos en el boton Import y exportamos los dashboard (es el json de la carpeta DASHBOARD_KIBANA)
 


NOTA_IMPORTANTE: Recuerda tener en tu /etc/hosts las rutas que aparecen en el fichero AddHosts

NOTA: Para esta versión de github, para acceder a mongodb, el cual, tiene la base de datos de OSM para españa, debes montarla tu mismo con las instrucciones de mongosm. Aun así, no es necesario tenerlo para ejecutarlo.