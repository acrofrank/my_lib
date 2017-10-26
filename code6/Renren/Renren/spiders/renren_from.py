# -*- coding: utf-8 -*-
import scrapy


class RenrenFromSpider(scrapy.Spider):
    name = 'renren_from'
    allowed_domains = ['renren.com']
    # 修改起始url
    start_urls = ['http://www.renren.com/']

    def parse(self, response):
        post_data = {
            "email": "17173805860",
            "password": "1qaz@WSX3edc"
        }
        yield scrapy.FormRequest.from_response(response,callback=self.parse_login,formdata=post_data)


    def parse_login(self, response):
        with open('renren2.html','w')as f:
            f.write(response.text)