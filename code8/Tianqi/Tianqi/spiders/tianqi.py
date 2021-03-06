# -*- coding: utf-8 -*-
import scrapy
from Tianqi.items import TianqiItem
import time

# ----1 导入RedisSpider类
from scrapy_redis.spiders import RedisSpider


# ----2 修改类的继承
# class TianqiSpider(scrapy.Spider):
class TianqiSpider(RedisSpider):
    name = 'tianqi'

    # ----3 注销允许的域和起始的url
    # allowed_domains = ['tianqi.com']
    # 修改起始的url
    # start_urls = ['http://lishi.tianqi.com/']

    # ----4 动态获取允许的域
    def __init__(self, *args, **kwargs):
        # 从参数中获取域名
        domain = kwargs.pop("domain","")
        # 提取允许的域
        self.allowed_domains = list(filter(None,domain.split(',')))
        super(TianqiSpider,self).__init__(*args,**kwargs)

    # ----5 redis_key
    redis_key = "tianqi"

    def parse(self, response):
        # 获取地区节点列表
        node_list = response.xpath('//ul[@class="bcity"]/li/a[@target="_blank"]')
        # print (len(node_list))

        # 遍历节点列表
        for node in node_list[10:15]:
            # 抽取数据
            url = node.xpath('./@href').extract_first()
            area = node.xpath('./text()').extract_first()

            # 发起请求，并且将地区名传递下去
            yield scrapy.Request(url, callback=self.parse_area, meta={"meta_1":area})

    def parse_area(self, response):
        # 获取meta传参
        area = response.meta['meta_1']

        # 获取url列表
        url_list = response.xpath('//*[@id="tool_site"]/div[2]/ul/li/a/@href').extract()

        # 遍历url列表
        for url in url_list[10:15]:
            print (url)
            yield scrapy.Request(url, callback=self.parse_data, meta={"meta_2":area})


    def parse_data(self, response):
        area = response.meta['meta_2']

        # 获取所有的数据节点列表
        node_list = response.xpath('//*[@id="tool_site"]/div[@class="tqtongji2"]/ul')
        # print (len(node_list))

        # 遍历数据节点列表,切片去掉标题
        for node in node_list[1:]:
            # 创建item对象
            item = TianqiItem()
            # 抽取数据,存放到item中
            item['area'] = area
            item['crawl_time'] = time.time()
            item['url'] = response.url

            item['datetime'] = node.xpath('./li[1]/a/text()').extract_first()
            item['max_t'] = node.xpath('./li[2]/text()').extract_first()
            item['min_t'] = node.xpath('./li[3]/text()').extract_first()
            item['weather'] = node.xpath('./li[4]/text()').extract_first()
            item['wind_direction'] = node.xpath('./li[5]/text()').extract_first()
            item['wind_power'] = node.xpath('./li[6]/text()').extract_first()

            # print (item)
            # 返回数据
            yield item









