# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.utils.project import get_project_settings
import os


class DouyuPipeline(object):
    def __init__(self):
        self.file = open('douyu.json','w')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item),ensure_ascii=False) + ',\n')

        return item

    def close_spider(self, spider):
        self.file.close()


class ImagePipeline(ImagesPipeline):
    # 获取图片存储路径
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    # 提交需要下载图片的请求
    def get_media_requests(self, item, info):
        # print ('-------',item['image_url'])
        yield scrapy.Request(item['image_url'])


    # 接收下载文件的相关信息
    def item_completed(self, results, item, info):
        # print (results)
        images = [data['path'] for status,data in results if status]
        # print (images)
        old_name = self.IMAGES_STORE + os.sep + images[0]
        new_name = self.IMAGES_STORE + os.sep + images[0].split(os.sep)[0] + os.sep + item['nick_name'] + '.jpg'

        # 重命名
        os.rename(old_name,new_name)
        item['image_path'] = new_name

        return item