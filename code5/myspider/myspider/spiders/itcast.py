# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # 限定爬虫的采集范围,允许的与不能加url协议，不能加/
    allowed_domains = ['itcast.cn']
    # 修改起始的url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # print (dir(response))
        # 获取所有讲师节点
        node_list = response.xpath('//div[@class="li_txt"]')
        # print ('#######',len(node_list))

        # data_list = []

        # 遍历节点列表
        for node in node_list:
            # 创建存储数据的item实例
            item = MyspiderItem()

            # 抽取数据翻入到item中
            item['name'] = node.xpath('./h3/text()').extract()[0]
            item['title'] = node.xpath('./h4/text()').extract()[0]
            item['desc'] = node.xpath('./p/text()').extract()[0]
            yield item
            # data_list.append(item)

        # return data_list




