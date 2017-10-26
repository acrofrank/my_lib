# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Sun.items import SunItem

class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    # 修改允许的域名
    allowed_domains = ['sun0769.com']
    # 修改起始的url
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']

    rules = (
        # 翻页
        Rule(LinkExtractor(allow=r'questionType'), follow=True),
        # 提取详情页面的链接
        Rule(LinkExtractor(allow=r'html/question/\d+/\d+.shtml'), callback='parse_item'),
    )

    def parse_item(self, response):
        # 创建item对象
        item = SunItem()

        # 抽取数据，存放到item中
        item['number'] = response.xpath('/html/body/div[6]/div/div[1]/div[1]/strong/text()').extract_first().split(':')[-1].strip()
        item['url'] = response.url
        item['title'] = response.xpath('/html/body/div[6]/div/div[1]/div[1]/strong/text()').extract_first().split(' ')[0].split('：')[-1].strip()
        data = ''
        contents = response.xpath('/html/body/div[6]/div/div[2]/div[1]/div[2]/text()|/html/body/div[6]/div/div[2]/div[1]/text()').extract()
        for content in contents:
            data += content.strip()
        item['content'] = data

        # 返回给引擎
        yield item