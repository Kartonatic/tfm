![alt text](https://github.com/Kartonatic/tfm/blob/master/ELK/logo.png "Logos de elastic")

(EN PROCESO... FALTA PONER CADA UNO EN FUNCIONAMIENTO CADA SERVICIO CON SU PROPIO DOCKERFILE)

ELK es una estructura de elastic que contiene: elasticsearch, kibana y logstash.

	- Elasticsearch: se trata de una base de datos con un motor de busquedas basado en lucence.

	- Kibana: se trata de una teconologia que nos permite ver los datos de una forma facil y montar dashboards.

	- Logstash: se tratan de colas con flujos de datos los cuales son recibidos, procesados y, por ultimo, insertados en elasticsearch. 

El usuario que ejecuta estos servicios es elastic y el grupo al que pertenece es bbdd.

IMPORTANTE: 
Para que puede ejecutarse, hay que aumentar la memoria virtual que puden usar nuestros servicios. Para hacerlo en ubuntu usa el comando:
	
	- sudo sysctl -w vm.max_map_count=262144
