import scrapy
import dateutil.parser
import numpy as np

class StatsSpider(scrapy.Spider):
    name = "company"
    rotate_user_agent = True

    # if not hxs.select('//get/site/logo'):
    #     yield Request(url=response.url, dont_filter=True)
    def parse(self, response):
        try:
            yield {
                'companyName': response.xpath("//div[contains(@class, 'D(ib)')]/h1/text()").get().split("(")[0][:-1],
                'symbol': response.xpath("//div[contains(@class, 'D(ib)')]/h1/text()").get().split("(")[1][:-1],
                'description': response.xpath("//section[contains(@class, 'quote-sub-section')]//p/text()").get(),
                'CEO': response.xpath("//table//tbody//tr[1]//td[1]//span/text()").get(),
                'sector': response.xpath(".//div[@data-test='asset-profile']//span[text()='Sector']/following::span[1]/text()").get(),
                'industry': response.xpath(".//div[@data-test='asset-profile']//span[text()='Industry']/following::span[1]/text()").get(),
                'employees': parseEmployees(response.xpath(".//div[@data-test='asset-profile']//span[text()='Full Time Employees']/following::span[1]//span/text()").get())
            }
        except:
            return None

def parseEmployees(string):
    try:
        if string == 'N/A' or string == None:
            return None
        else:
            return float(string.replace(',', ''))
    except:
        return None