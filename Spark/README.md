![alt text](https://github.com/Kartonatic/tfm/blob/master/Spark/logo.png "Logo de Spark")

Spark es una tecnologia que nos permite hacer procesamiento de datos muy rapidamente ya que almacena la informacion en memoria. 

El spark que se ha montado se conecta directamente con hadoop 3.1.0 de este mismo proyecto, por lo que podemos usar spark perfectamente integrado con hadoop. El usuario que lanza el
proceso spark es hdmaster para que no tenga problemas de permisos con hadoop. También se conecta con zookeeper para que tenga alta disponibilidad a la hora de elegir un nuevo master. 

Se ha configurado un nodo master que contiene la web principal y el history server. Hay configurados 3 workers que se dedicaran a hacer el procesamiento de los datos de 
manera distribuida (si se quiere).

Lo bueno es que actualmente tienes dos posibilidades en esta arquitectura segun se quiera... Puedes elegir que se ejecuten los procesos de forma distribuida en los 
nodos del yarn (asignados como nodemanager) o ejecutar los nodos con la configuración que he puesto para spark. Por defecto se ejecutará sobre el yarn. La forma de usarlo es:
	
	- Para el usar el cluster yarn:
		spark-shell --master yarn

	- Para usar el cluster spark:
		 spark-shell --master spark://sparkmaster:7077 