Para ejecutar esto hay que descargarse cualquiera de los mapas que queramos de OSM y usar:

python insert_osm_data.py <OSM filename>

que está ubicado en el directorio mongosm-master.

Puedes descargar mapas de OSM en http://download.geofabrik.de/


Para probarlo podemos usar el siguiente codigo de python:

```
import pymongo
from pymongo import MongoClient
import pprint


client = MongoClient("mongomaster", 27017)
db = client.osm
nodes = db.nodes
ways = db.ways
realations = db.realations


#Te devuelve el nodo mas cercano a la ubicación expuesta:
query = nodes.find({"loc": { "$near": [37.7743462, -1.0465891], "$maxDistance": 0.0001 } })
pprint.pprint(query[0])

#Si quieres obtener mas informacion hay que buscarlo por ways ya que buscar el nodo en ways es mas costoso que por ubicacion
query2 = ways.find({"loc": { "$near": [39.443829, -0.391207], "$maxDistance": 0.001 } })
pprint.pprint(query2[0])
```