from elasticsearch import helpers, Elasticsearch

elasticurl = "http://elasticsearch:9200"

es = Elasticsearch(elasticurl)

if es.indices.exists(index='car_gps'):
    es.indices.delete(index='car_gps')


if es.indices.exists(index='actual_car_gps'):
    es.indices.delete(index='actual_car_gps')


es.indices.create(index='car_gps', body='{ "settings" : { "number_of_shards" : 1 }, "mappings" : { "car_gps": { "properties": { "id_user": { "type": "integer" }, "name": { "type": "keyword" }, "sensorId": { "type": "keyword" }, "Type": { "type": "keyword" }, "coordinates_lat": { "type": "double" }, "coordinates_long": { "type": "double" }, "location": {"type": "geo_point"}, "altitude": { "type": "double" }, "heading": { "type": "integer" }, "speed": { "type": "integer" }, "speedmetric": { "type": "text" }, "temp": { "type": "integer" }, "observationTime": { "type": "date" }, "date": { "type": "text" }, "serverTime": { "type": "text" }, "dateSend": { "type": "text" } } } } }')

es.indices.create(index='actual_car_gps', body='{ "settings" : { "number_of_shards" : 1 }, "mappings" : { "actual_car_gps": { "properties": { "id_user": { "type": "integer" }, "name": { "type": "keyword" }, "sensorId": { "type": "keyword" }, "Type": { "type": "keyword" }, "coordinates_lat": { "type": "double" }, "coordinates_long": { "type": "double" }, "location": {"type": "geo_point"}, "altitude": { "type": "double" }, "heading": { "type": "integer" }, "speed": { "type": "integer" }, "speedmetric": { "type": "text" }, "temp": { "type": "integer" }, "observationTime": { "type": "date" }, "date": { "type": "text" }, "serverTime": { "type": "text" }, "dateSend": { "type": "text" } } } } }')

