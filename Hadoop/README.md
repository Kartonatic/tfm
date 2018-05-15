![alt text](https://github.com/Kartonatic/tfm/blob/master/Hadoop/hadoop.png "Logo de hadoop")


Se han creado las dos versiones de hadoop por si alguien necesita cambiarlas.
 
En este caso se ha creado la 2.7.6 por si habia incompatibilidades con la 3.1.0 
cunado montaramos spark o flink. En el caso de spark no habia incompatibilidades 
sin embargo, flink, al coger la configuracion de hadoop, no entendia los -1 de 
dicha configuración (en hadoop 3 pudes usar -1 para que autodetecte el hardware
y actue segun las necesidades del momento). Sin embargo, se ha usado Hadoop 3.1.0
tambien para flink ya que cambiando los valores -1 de los xml podemos usarla.

Usuario que lanza hadoop: hdmaster 

This folder contains:

 - HADOOP 2.7.6

 - HADOOP 3.1.0

 