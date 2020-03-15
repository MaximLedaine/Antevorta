from flask_restful import Resource
from flask import request, jsonify, make_response
import requests
from ..modules.connection import url
from ..modules.errorHandling import BadRequest
import json
class Company(Resource):
    def get(self, symbol):
        try:
            return make_response(get_company(symbol))
        except BadRequest as e:
            return make_response(jsonify(message=e.message), e.status)
        except:
            return make_response(jsonify(message="Internal server error"), 500)

class CompanyList(Resource):
    def get(self):
        try:
            symbols = request.args.get('symbols').split(',')
            print(symbols)
            results = {}
            for symbol in symbols:
                print(symbol)
                results[symbol] = json.loads(get_company(symbol)[0].data.decode('utf-8'))

            return make_response(jsonify(data=results), 200)
        except BadRequest as e:
            return make_response(jsonify(message=e.message), e.status)
        except:
            return make_response(jsonify(message="Internal server error"), 500)

def get_company(symbol):
    print('hello')
    response = requests.get(
        f'{url}/crawl.json?spider_name=company&url=https://finance.yahoo.com/quote/{symbol}/profile?p={symbol}'
        )
    
    if not response.json()['items']:
        raise BadRequest('Not found', 404)
    
    return jsonify(data=response.json()['items'][0]), 200
