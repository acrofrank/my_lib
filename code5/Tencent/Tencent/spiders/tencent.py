# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    # 检查允许的域名
    allowed_domains = ['tencent.com']
    # 修改起始的url列表
    start_urls = ['http://hr.tencent.com/position.php']

    def parse(self, response):
        # 获取当前页面所有职位节点
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        # print (len(node_list))

        # 遍历节点列表
        for node in node_list:
            # 创建存储数据的item实例
            item = TencentItem()

            # 抽取数据，将数据赋值到item中对应的键
            item['job_name'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['detail_link'] = 'http://hr.tencent.com/' + node.xpath('./td[1]/a/@href').extract()[0]
            # extract_first()提取第一个，如果没有，则返回None
            item['job_type'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract()[0]
            item['address'] = node.xpath('./td[4]/text()').extract()[0]
            item['pub_time'] = node.xpath('./td[5]/text()').extract()[0]
            # 将数据返回给引擎
            yield item


        try:
            # 获取下一页url
            next_url = 'http://hr.tencent.com/' + response.xpath('//a[@id="next"]/@href').extract()[0]
            # 将url做成请求，返回给引擎
            yield scrapy.Request(next_url,callback=self.parse)
        except:
            pass














