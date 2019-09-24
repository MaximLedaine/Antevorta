import requests as requests
import json
import random
import asyncio
from aiohttp import ClientSession
from pymongo import MongoClient
client = MongoClient()
db = client['test']

collection = 'statistics'

# get symbols of corresponding exchanges
exchanges = [
    {'exchange': 'NAS', 'suffix': ''},
    {'exchange': 'NYS', 'suffix': ''},
    {'exchange': 'ASE', 'suffix': ''},
    {'exchange': 'LON', 'suffix': 'l'},
    {'exchange': 'PAR', 'suffix': 'pa'},
    {'exchange': 'AMS', 'suffix': 'as'},
    {'exchange': 'BRU', 'suffix': 'br'},
    {'exchange': 'LIS', 'suffix': 'ls'},
    {'exchange': 'TSE', 'suffix': 'to'},
    {'exchange': 'TSX', 'suffix': 'v'},
    {'exchange': 'MEX', 'suffix': 'mx'},
    {'exchange': 'ETR', 'suffix': 'de'},
    # {'exchange': 'KRX', 'suffix': ['kq', 'ks']},
    {'exchange': 'BOM', 'suffix': 'bo'},
    {'exchange': 'TAE', 'suffix': 'ta'}
]

res =  db['symbols'].find({ 'exchange': { '$in' : [x['exchange'] for x in exchanges] }})

# result
symbols = list(res)
random.shuffle(symbols)
for stock in symbols:
    suffix =  [x for x in exchanges if x['exchange'] == stock['exchange']][0]['suffix']
    stock['yahooSymbol'] = stock['symbol'].split('-')[0] + (f'.{suffix}' if len(suffix) else '')
    print(stock['yahooSymbol'])
print(len(symbols))

# functions
async def fetch(url, symbol, session, count):
    async with session.get(url) as response:
        delay = response.headers.get("DELAY")
        date = response.headers.get("DATE")
        print(count)
        print(response.url)
        data = await response.read()
        if 'message' in (json.loads(data)):
            print('------------error--------------')
        else:
            print('------------succes--------------')
            symbol = symbol.lower()
            requests.put(f'http://localhost:4000/v1/{collection}/{symbol}', data=json.dumps((json.loads(data))['data']), headers={'content-type': 'application/json'})
            requests.put(f'http://localhost:4100/v1/{collection}/{symbol}', data=json.dumps((json.loads(data))['data']), headers={'content-type': 'application/json'})
        return json.loads(data)

async def bound_fetch(sem, url, symbol, session, count):
    # Getter function with semaphore.
    async with sem:
        return await fetch(url, symbol, session, count)

async def run(r):
    url = "http://localhost:9081/v1/yahoo/{0}/{1}"
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(1)

    # Create client session that will ensure we dont open new connection
    # per each request.
    async with ClientSession() as session:
        for i, stock in enumerate(symbols):
            try:
                # pass Semaphore and session to every GET request
                task = asyncio.ensure_future(bound_fetch(sem, url.format(collection, stock['yahooSymbol']), stock['symbol'], session, i))
                tasks.append(task)
            except:
                print('error')
                continue
            
        responses = await asyncio.gather(*tasks)
        return responses

# run loop
number = len(symbols)
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(number))
loop.run_until_complete(future)

# results
results = future.result()
print(len(results))

# for stock in results:
#     if 'data' in stock:
#         symbol = stock['data']['symbol'].lower()
#         requests.put(f'http://localhost:4000/v1/{collection}/{symbol}', data=json.dumps(stock['data']), headers={'content-type': 'application/json'})
#         requests.put(f'http://localhost:4100/v1/{collection}/{symbol}', data=json.dumps(stock['data']), headers={'content-type': 'application/json'})