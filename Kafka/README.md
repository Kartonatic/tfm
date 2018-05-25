![alt text](https://github.com/Kartonatic/tfm/blob/master/Kafka/logo.png "Logo de kafka")

Con Kafka tenemos un servicio productor/consumidor en donde varios productores y consumidores se pueden subscribir a una misma cola de mensajes.

Hemos implementado un servicio kafka de 3 nodos. Si falla un nodo, otro tendrá la copia de la cola por lo que se pueden redirigir los datos.

Se ha añadido auto.leader.rebalance.enable = true

Servicio kafka con 3 brokers (ids = 0,1 y 2).

Kafka service with 3 brokers (ids = 0,1 and 2).

 
