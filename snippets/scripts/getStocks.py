import requests as requests
import json
baseUrl = 'https://cloud.iexapis.com/v1'
apikey = 'pk_8a31fe45ab0c48c785d7f10d0021b0e9'
from elasticsearch import Elasticsearch
es = Elasticsearch()
from pymongo import MongoClient
client = MongoClient()
db = client['test']
import math

def getSymbols(exchange):
#     exchange = 'nys' # nasdaq = nas; nyse = NYS
    response = requests.get(
        baseUrl + f'/ref-data/exchange/{exchange}/symbols',
        params= {
            'token': apikey,
            'format': 'json'
            }
        )
    symbols = json.loads(response.content)
    stockSymbols = list(filter(lambda x : x['type'] == 'cs', symbols))
    
    print(len(stockSymbols))
    return stockSymbols

def setSymbols(symbols):
    for stock in list(filter(lambda x : x['type'] == 'cs', symbols)):
        es.index(index="symbols", id=stock['symbol'].lower(), doc_type='_doc', body=stock)
        stock['_id'] = stock['symbol'].lower()
        db.symbols.update_one({'_id': stock['_id']}, {'$set': stock}, upsert=True)

def getExchanges():
    response = requests.get(
    baseUrl + f'/ref-data/exchanges',
    params= {
        'token': apikey,
        'format': 'json'
        }
    )
    exchanges = response.json()
    return exchanges

def getCompanyList(symbols):
    docs = {}
    for i in range(math.ceil(len(list(filter(lambda x : x['type'] == 'cs', symbols)))/100)):
        print((i+1) * 100)
        symbolStr = (','.join(map(lambda x: x['symbol'], list(filter(lambda x : x['type'] == 'cs', symbols))[(i)*100:(i+1) * 100])))
        response = requests.get(
        baseUrl + f'/stock/market/batch?symbols={symbolStr}&types=company',
        params= {
            'token': apikey,
            'format': 'json'
            }
        )
        newDocs = response.json()
        docs = {**docs, **newDocs}
    return docs

def setCompanyList(docs):
    for key, value in docs.items():
        try:
            print('----key----')
            print(key)
            doc = value['company']
            es.index(index="company", id=doc['symbol'].lower(), doc_type='_doc', body=doc)
            doc['_id'] = doc['symbol'].lower()
            db.company.update_one({'_id': doc['_id']}, {'$set': doc}, upsert=True)
        except Exception as e:
            print('------error-------')
            print(e)
            print(key)
            print(value)
            continue

exchanges = getExchanges()
for exchange in exchanges:
    print(exchange['exchange'])
    # symbols
    symbols = getSymbols(exchange['exchange'])
    setSymbols(symbols)
    # company
    docs = getCompanyList(symbols)
    setCompanyList(docs)

# list all exchanges
# [x for x in exchanges if ...]