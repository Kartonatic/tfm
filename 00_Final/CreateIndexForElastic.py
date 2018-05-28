from elasticsearch import helpers, Elasticsearch

elasticurl = "http://elasticsearch:9200"

es = Elasticsearch(elasticurl)

if es.indices.exists(index='car_gps'):
    es.indices.delete(index='car_gps')


es.indices.create(index='put', body='{ "settings" : {  "number_of_shards" : 1 }, "mappings" : { "car_gps": { "properties": { "sensorId": { "type": "keyword" }, "Type": { "type": "keyword" }, "coordinates.lat": { "type": "double" }, "coordinates.long": { "type": "double" }, "location": {"type": "geo_point"}, "altitude": { "type": "double" }, "heading": { "type": "integer" }, "speed": { "type": "integer" }, "speedmetric": { "type": "text" }, "temp": { "type": "integer" }, "observationTime": { "type": "text" }, "date2": { "type": "date" }, "dateSend": { "type": "date" } } } } } ')
