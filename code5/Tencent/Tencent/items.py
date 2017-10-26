# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名
    job_name = scrapy.Field()
    # 详情页面
    detail_link = scrapy.Field()
    # 职位类别
    job_type = scrapy.Field()
    # 人数
    number = scrapy.Field()
    # 工作地点
    address = scrapy.Field()
    # 发布时间
    pub_time = scrapy.Field()
    pass
