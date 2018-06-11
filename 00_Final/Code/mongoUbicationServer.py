#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import json
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.serving import run_simple

class UbicationService(object):
    def getWay(self, request, lat, long):
        try:
            latitude= float(lat)
            longitude = float(long)
            if (latitude is None or longitude is None):
                return Response("{}", content_type="text/json")
            query = self.ways.find({ "$and": [ {"loc": { "$near": [latitude, longitude], "$maxDistance": 0.01 } },
                                      { "$and": [ {"tg" : {'$elemMatch':{'$elemMatch':{'$in':['highway']}}}},
                                                {"tg" : {'$elemMatch':{'$elemMatch':{'$in':['motorway', 'trunk', 'primary',
                                                                                           'secundary', 'tertiary',
                                                                                           'unclassified', 'residential',
                                                                                           'service', 'road'
                                                                                           ]
                                                                                    }
                                                                      }
                                                        }
                                                }
                                                ]
                                      }
                                    ]} ).limit(1)

            if (query.count(with_limit_and_skip=True))>0:
                return Response(json.dumps(query[0]),  content_type='text/json')
            return Response("{}", content_type='text/json')
        except Exception as e:
            return Response(str(e))

    def __init__(self):
        self.ways =  MongoClient("mongomaster", 27017).osm.ways
        self.url_map = Map([
            Rule('/getway/<lat>/<long>', endpoint='getWay'),
        ])

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, endpoint)(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

if __name__ == '__main__':
    app = UbicationService()
    run_simple('0.0.0.0', 5000, app, use_debugger=False, use_reloader=True, processes=10) #threaded=True)#,