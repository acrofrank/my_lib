# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    # 修改允许的域
    allowed_domains = ['douyucdn.cn']
    offset = 0
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset='
    # 修改起始的url
    start_urls = [base_url]

    def parse(self, response):
        data_list = json.loads(response.body)['data']
        # print (data_list)

        # 遍历数据列表
        for data in data_list:
            # 创建 item实例
            item = DouyuItem()

            # 从data中获取相应的数据字段值，存放到item中
            item['nick_name'] = data['nickname']
            item['uid'] = data['owner_uid']
            item['city'] = data['anchor_city']
            item['image_url'] = data['vertical_src']
            # print (item)

            # 返回数据
            yield item

        # 模拟翻页
        # 判断翻页终止条件
        if len(data_list) != 0:
            self.offset += 100
            url = self.base_url + str(self.offset)
            # 创建请求并发送
            yield scrapy.Request(url, callback=self.parse)






