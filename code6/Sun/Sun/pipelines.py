# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.conf import settings
from pymongo import MongoClient


class SunPipeline(object):
    def __init__(self):
        self.file = open('donggaun.json','w')

    def process_item(self, item, spider):
        str_data =  json.dumps(dict(item),ensure_ascii=False) + ',\n'

        self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()

class MongPipeline(object):
    def __init__(self):
        # 获取数据库参数
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        dbname = settings['MONGO_DBNAME']
        colname = settings['MONGO_COLNAME']

        # 链接数据库
        self.client = MongoClient(host,port)

        # 选择数据库
        self.db = self.client[dbname]

        # 选择集合
        self.col = self.db[colname]


    def process_item(self, item, spider):
        # 转换为字典
        dict_data = dict(item)
        #插入数据库
        self.col.insert(dict_data)
        return item


    def close_spider(self, spdier):
        self.client.close()
