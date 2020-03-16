import scrapy
import dateutil.parser
import numpy as np

class StatsSpider(scrapy.Spider):
    name = "stats"
    rotate_user_agent = True

    # if not hxs.select('//get/site/logo'):
    #     yield Request(url=response.url, dont_filter=True)
    def parse(self, response):
        try:
            yield {
                'companyName': response.xpath("//div[@class='D(ib) ']/h1/text()").get().split("(")[0][:-1],
                'symbol': response.xpath("//div[@class='D(ib) ']/h1/text()").get().split("(")[1][:-1],
                'week52high': parseMax(response.xpath(".//td[@data-test='FIFTY_TWO_WK_RANGE-value']/text()").get()),
                'week52low':  parseMin(response.xpath(".//td[@data-test='FIFTY_TWO_WK_RANGE-value']/text()").get()),
                'open': parseNumber(response.xpath(".//td[@data-test='OPEN-value']/span/text()").get()),
                'previousClose': parseNumber(response.xpath(".//td[@data-test='PREV_CLOSE-value']/span/text()").get()),
                'marketCap': parseMarketCap(response.xpath(".//td[@data-test='MARKET_CAP-value']/span/text()").get()),
                'beta': parseNumber(response.xpath(".//td[@data-test='BETA_5Y-value']/span/text()").get()),
                'peRatio': parseNumber(response.xpath(".//td[@data-test='PE_RATIO-value']/span/text()").get()),
                'ttmEPS': parseNumber(response.xpath(".//td[@data-test='EPS_RATIO-value']/span/text()").get()),
                'forwardDividendYield': parseForwardDividendYield(response.xpath(".//td[@data-test='DIVIDEND_AND_YIELD-value']/text()").get()),
                # 'earningsDate': parseDate(response.xpath(".//td[@data-test='EARNINGS_DATE-value']/span/text()").get()),
                # 'exDividendDate': parseDate(response.xpath(".//td[@data-test='EX_DIVIDEND_DATE-value']/span/text()").get()),
                'oneYearTarget': parseNumber(response.xpath(".//td[@data-test='ONE_YEAR_TARGET_PRICE-value']/span/text()").get()),
                'volume': parseVolume(response.xpath(".//td[@data-test='TD_VOLUME-value']/span/text()").get()),
                'avgVolume3Months': parseVolume(response.xpath(".//td[@data-test='AVERAGE_VOLUME_3MONTH-value']/span/text()").get()),
            }
        except:
            return None
    
def parseVolume(string):
    try:
        return int(string.replace(",", ""))
    except:
        return None

def parseNumber(string):
    try:
        if string == 'N/A':
            return None
        else:
            return float(string)
    except:
        return None

def parseDate(string):
    try:
        if (string != None):
            return dateutil.parser.parse(string).strftime("%Y-%m-%d")
        else:
            return None
    except:
        return None

def parseMarketCap(string):
    try:
        marketCap = float(string[:-1])
        if (string[-1:] == 'B'): 
            marketCap = marketCap * 1000000000
        elif (string[-1:] == 'M'): 
            marketCap = marketCap * 1000000
        return marketCap
    except:
        return None

def parseForwardDividendYield(string):
    try:
        if string == 'N/A (N/A)':
            return None
        else:
            return float(string.split(" ")[0])
    except:
        return None

def parseMin(string):
    try:
        return min(np.array(string.split(' - ')).astype(np.float))
    except:
        return None

def parseMax(string):
    try:
        return max(np.array(string.split(' - ')).astype(np.float))
    except:
        return None