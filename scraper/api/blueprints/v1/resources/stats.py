from flask_restful import Resource
from flask import request, jsonify, make_response
import requests
from ..modules.connection import url
from ..modules.errorHandling import BadRequest

class Stats(Resource):
    def get(self, symbol):
        try:
            return get_stats(symbol)
        except:
            raise BadRequest('Internal server error', 500)

class StatsList(Resource):
    def get(self):
        try:
            symbols = request.args.get('symbols').split(',')
            results = []
            for symbol in symbols:
                results.append(get_stats(symbol))
            return jsonify(results)
        except:
            raise BadRequest('Internal server error', 500)

def get_stats(symbol):
    try:
        response = requests.get(
            f'{url}/crawl.json?spider_name=stats&url=https://finance.yahoo.com/quote/{symbol}?p={symbol}'
            )
        
        if not response.json()['items']:
            raise BadRequest('Not found', 404)
        
        return make_response(jsonify(data=response.json()['items'][0]), 200)

    except BadRequest as e:
        return make_response(jsonify(message=e.message), e.status)
    except:
        raise BadRequest('Internal server error', 500)