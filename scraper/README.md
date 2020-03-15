# Scraper

## Concept
Scraper allows you to scrape any website with rotating user-agents and proxies


# Routes

request url: localhost:9081

## requests

```
GET /v1/yahoo/stocks/{symbol}/stats
```
```
GET /v1/yahoo/stocks/{symbol}/company
```
```
GET /v1/yahoo/stocks/{symbol}/statistics
```
```
GET /v1/yahoo/stocks/{symbol}/history
```
To batch request: <br/>
{symbol} = <i>'market'</i><br/> 
symbols parameter is comma seperated list of stock symbols<br/>
example: <br/>
```
GET /v1/yahoo/stocks/market/stats?symbols=aapl,goog,amd
```

# Run developoment

```
bin/dev.sh
```

or

```
docker-compose build
docker-compose up
```