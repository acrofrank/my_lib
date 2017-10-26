# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Douban.items import DoubanItem

class MovieSpider(CrawlSpider):
    name = 'movie'
    # 检查允许的域名
    allowed_domains = ['douban.com']
    # 修改起始的url
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print (response.url)
        # 获取节点列表o
        node_list = response.xpath('//div[@class="info"]')
        # print (len(node_list))
        # 遍历节点列表
        for node in node_list:
            # 创建 item对象
            item = DoubanItem()

            # 解析数据，赋值到item指定字段
            # extract_first()没有数据自动补None
            item['name'] = node.xpath('./div[1]/a/span[1]/text()').extract_first()
            item['score'] = node.xpath('./div[2]/div/span[2]/text()').extract_first()
            item['info'] = ''.join([data.strip() for data in node.xpath('./div[2]/p[1]/text()').extract()])
            item['desc'] = node.xpath('./div[2]/p[2]/span/text()').extract_first()
            # print (item)
            # 返回数据
            yield item

