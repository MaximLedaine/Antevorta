from flask_restful import Resource
from flask import request, jsonify, make_response
import requests
from ..modules.connection import url
from ..modules.errorHandling import BadRequest
import json
class Stats(Resource):
    def get(self, symbol):
        try:
            return make_response(get_stats(symbol))
        except BadRequest as e:
            return make_response(jsonify(message=e.message), e.status)
        except:
            return make_response(jsonify(message="Internal server error"), 500)

class StatsList(Resource):
    def get(self):
        try:
            symbols = request.args.get('symbols').split(',')
            results = {}
            for symbol in symbols:
                results[symbol] = json.loads(get_stats(symbol)[0].data.decode('utf-8'))
            
            return make_response(jsonify(results), 200)
        except BadRequest as e:
            return make_response(jsonify(message=e.message), e.status)
        except:
            return make_response(jsonify(message="Internal server error"), 500)

def get_stats(symbol):
    response = requests.get(
        f'{url}/crawl.json?spider_name=stats&url=https://finance.yahoo.com/quote/{symbol}?p={symbol}'
        )
    
    if not response.json()['items']:
        print('not found')
        raise BadRequest('Not found', 404)
    
    return jsonify(data=response.json()['items'][0]), 200