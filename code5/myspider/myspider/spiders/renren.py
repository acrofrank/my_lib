#coding:utf-8
import scrapy

class Renren(scrapy.Spider):
    name = "renren"
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/']

    def parse(self, response):
        with open('renren.html','w')as f:
            f.write(response.body.decode())