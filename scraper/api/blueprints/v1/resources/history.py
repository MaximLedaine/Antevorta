from flask_restful import Resource
from flask import request, jsonify, make_response
import requests
import yfinance as yf
from ..modules.errorHandling import BadRequest
import json

class History(Resource):
    def get(self, symbol):
        try:
            return make_response(get_history(symbol))
        except BadRequest as e:
            return make_response(jsonify(message=e.message), e.status)
        except:
            return make_response(jsonify(message="Internal server error"), 500)

class HistoryList(Resource):
    def get(self):
        try:
            symbols = request.args.get('symbols').split(',')
            results = {}
            for symbol in symbols:
                res = get_history(symbol)
                results[symbol] = res[0].data.decode("utf-8") 
            return make_response(jsonify(data=results), 200)
        except BadRequest as e:
            return make_response(jsonify(message=e.message), e.status)
        except:
            return make_response(jsonify(message="Internal server error"), 500)

def get_history(symbol):
    # results is a dataframe
    results = yf.Ticker(symbol).history(period="max")
    if results.empty:
        raise BadRequest('Not found, symbol may be delisted', 404)
    
    return jsonify(data=results.to_csv()), 200