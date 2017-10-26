# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    # 修改起始的url
    start_urls = ['http://www.renren.com/PLogin.do']

    def start_requests(self):
        post_data = {
            "email": "17173805860",
            "password": "1qaz@WSX3edc"
        }
        # 构建post请求并发送出去
        yield scrapy.FormRequest(self.start_urls[0],formdata=post_data)

    def parse(self, response):
        with open('renren.html','wb')as f:
            f.write(response.body)
