Montando apache elasticsearch, kibana y logstash
Para que puede ejecutarse, hay que aumentar la memoria virtual que puden usar nuestros servicios. Para hacerlo en ubuntu usa el comando:
	
	- sudo sysctl -w vm.max_map_count=262144
