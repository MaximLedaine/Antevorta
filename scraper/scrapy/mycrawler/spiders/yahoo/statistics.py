import scrapy
import dateutil.parser
import numpy as np

class StatsSpider(scrapy.Spider):
    name = "statistics"
    rotate_user_agent = True

    # if not hxs.select('//get/site/logo'):
    #     yield Request(url=response.url, dont_filter=True)
    def parse(self, response):
        try:
            yield {
                'companyName': response.xpath("//div[@class='D(ib) ']/h1/text()").get().split("(")[0][:-1],
                'symbol': response.xpath("//div[contains(@class, 'D(ib)')]/h1/text()").get().split("(")[1][:-1],
                'marketCap': parseValue(response.xpath("//td//span[contains(text(),'Market Cap')]/following::td[1]/text()").get()),
                'enterpriseValue': parseValue(response.xpath("//td//span[contains(text(),'Enterprise Value')]/following::td[1]/text()").get()),
                'trailingPe': parseNumber(response.xpath("//td//span[contains(text(),'Trailing P/E')]/following::td[1]/text()").get()),
                'forwardPe': parseNumber(response.xpath("//td//span[contains(text(),'Forward P/E')]/following::td[1]/text()").get()),
                'pegRatio': parseNumber(response.xpath("//td//span[contains(text(),'PEG Ratio')]/following::td[1]/text()").get()),
                'priceToSales': parseNumber(response.xpath("//td//span[contains(text(),'Price/Sales')]/following::td[1]/text()").get()),
                'priceToBook': parseNumber(response.xpath("//td//span[contains(text(),'Price/Book')]/following::td[1]/text()").get()),
                'enterpriseValueToRevenue': parseNumber(response.xpath("//td//span[contains(text(),'Enterprise Value/Revenue')]/following::td[1]/text()").get()),
                'enterpriseValueToEBITDA': parseNumber(response.xpath("//td//span[contains(text(),'Enterprise Value/EBITDA')]/following::td[1]/text()").get()),
            
                'fiscalYearEnds': parseDate(response.xpath("//td//span[contains(text(),'Fiscal Year Ends')]/following::td[1]/text()").get()),
                'mostRecentQuarter': parseDate(response.xpath("//td//span[contains(text(),'Most Recent Quarter')]/following::td[1]/text()").get()),
                'profitMargin': parsePercentage(response.xpath("//td//span[contains(text(),'Profit Margin')]/following::td[1]/text()").get()),
                'operatingMargin': parsePercentage(response.xpath("//td//span[contains(text(),'Operating Margin')]/following::td[1]/text()").get()),
                'returnOnAssets': parsePercentage(response.xpath("//td//span[contains(text(),'Return on Assets')]/following::td[1]/text()").get()),
                'returnOnEquity': parsePercentage(response.xpath("//td//span[contains(text(),'Return on Equity')]/following::td[1]/text()").get()),
                'revenue': parseValue(response.xpath("//td//span[contains(text(),'Revenue')]/following::td[1]/text()").get()),
                'revenuePerShare': parseNumber(response.xpath("//td//span[contains(text(),'Revenue Per Share')]/following::td[1]/text()").get()),
                'quarterlyRevenueGrowth': parsePercentage(response.xpath("//td//span[contains(text(),'Quarterly Revenue Growth')]/following::td[1]/text()").get()),
                'grossProfit': parseValue(response.xpath("//td//span[contains(text(),'Gross Profit')]/following::td[1]/text()").get()),
                'EBITDA': parseValue(response.xpath("//td//span[contains(text(),'EBITDA')]/following::td[1]/node()")[1].get()),
                'dilutedEPS': parseNumber(response.xpath("//td//span[contains(text(),'Diluted EPS')]/following::td[1]/text()").get()),
                'quarterlyEarningsGrowth': parsePercentage(response.xpath("//td//span[contains(text(),'Quarterly Earnings Growth')]/following::td[1]/text()").get()),
                'operatingCashFlow': parseValue(response.xpath("//td//span[contains(text(),'Operating Cash Flow')]/following::td[1]/text()").get()),
                'leveredFreeCashFlow': parseValue(response.xpath("//td//span[contains(text(),'Levered Free Cash Flow')]/following::td[1]/text()").get()),
                'Week52Change': parsePercentage(response.xpath("//td//span[contains(text(),'52-Week Change')]/following::td[1]/text()").get()),
                'week52ChangeS&P500': parsePercentage(response.xpath("//td//span[contains(text(),'S&P500 52-Week Change')]/following::td[1]/text()").get()),
                'week52High': parseNumber(response.xpath("//td//span[contains(text(),'52 Week High')]/following::td[1]/text()").get()),
                'week52Low': parseNumber(response.xpath("//td//span[contains(text(),'52 Week Low')]/following::td[1]/text()").get()),
                'day50MovingAverage': parseNumber(response.xpath("//td//span[contains(text(),'50-Day Moving Average')]/following::td[1]/text()").get()),
                'day200MovingAverage': parseNumber(response.xpath("//td//span[contains(text(),'200-Day Moving Average')]/following::td[1]/text()").get()),
                'Avg3MonthVol': parseValue(response.xpath("//td//span[contains(text(),'Avg Vol (3 month)')]/following::td[1]/text()").get()),
                'Avg10DayVol': parseValue(response.xpath("//td//span[contains(text(),'52 Week Low')]/following::td[1]/text()").get()),
                'float': parseValue(response.xpath("//td//span[contains(text(),'Float')]/following::td[1]/text()").get()),
                'heldbyInsiders': parsePercentage(response.xpath("//td//span[contains(text(),'Held by Insiders')]/following::td[1]/text()").get()),
                'heldByInstitutions': parsePercentage(response.xpath("//td//span[contains(text(),'Held by Institutions')]/following::td[1]/text()").get()),
                'shortRatio': parseNumber(response.xpath("//td//span[contains(text(),'Short Ratio')]/following::td[1]/text()").get()),
                'shortPercentageOfFloat': parsePercentage(response.xpath("//td//span[contains(text(),'Short % of Float')]/following::td[1]/text()").get()),
                'shortPercentageOfSharesOutstanding': parsePercentage(response.xpath("//td//span[contains(text(),'Short % of Shares Outstanding')]/following::td[1]/text()").get()),
                'sharesShortMonthBefore': parseValue(response.xpath("//td//span[contains(text(),'Shares Short (prior month')]/following::td[1]/text()").get()),
                'sharesShort': parseValue(response.xpath("//td//span[contains(text(),'Shares Short')]/following::td[1]/node()[1]").get()),
                'forwardAnnualDividendRate': parseNumber(response.xpath("//td//span[contains(text(),'Forward Annual Dividend Rate')]/following::td[1]/text()").get()),
                'forwardAnnualDividendYield': parsePercentage(response.xpath("//td//span[contains(text(),'Forward Annual Dividend Yield')]/following::td[1]/text()").get()),
                'trailingAnnualDividendRate': parseNumber(response.xpath("//td//span[contains(text(),'Trailing Annual Dividend Rate')]/following::td[1]/text()").get()),
                'trailingAnnualDividendYield': parsePercentage(response.xpath("//td//span[contains(text(),'Trailing Annual Dividend Yield')]/following::td[1]/text()").get()),
                'year5AverageDividendYield': parseNumber(response.xpath("//td//span[contains(text(),'5 Year Average Dividend Yield')]/following::td[1]/text()").get()),
                'payoutRatio': parsePercentage(response.xpath("//td//span[contains(text(),'Payout Ratio')]/following::td[1]/text()").get()),
                'dividendDate': parseDate(response.xpath("//td//span[contains(text(),'Dividend Date')]/following::td[1]/text()").get()),
                'exDividendDate': parseDate(response.xpath("//td//span[contains(text(),'Ex-Dividend Date')]/following::td[1]/text()").get()),
            }
        except:
            return None
    
def parseVolume(string):
    try:
        return int(string.replace(",", ""))
    except:
        return None

def parsePercentage(string):
    try:
        if string == 'N/A':
            return None
        else:
            return float(string.split('%')[0]) / 100
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

def parseValue(string):
    try:
        if string != 'N/A':
            marketCap = float(string[:-1])
            if (string[-1:] == 'B'): 
                marketCap = marketCap * 1000000000
            elif (string[-1:] == 'M'): 
                marketCap = marketCap * 1000000
            return marketCap
        else:
            return None
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