import scrapy
from scrapy_splash import SplashRequest
from scrapy.spiders import BaseSpider


class InstaSpider(BaseSpider):
    name="instaspider"
    handle_httpstatus_list = [400]
    allowed_domains=['instagram.com']

    def start_requests(self):
        line='http://www.instagram.com/deepikapadukone'
        yield scrapy.Request(line.strip(),callback=self.parse,priority=1,meta={'splash':{'args':{'wait':'25'},'endpoint':'render.html'}})

    def parse(self,response):
        print('--------here--------- {} '.format(response.body))
        
