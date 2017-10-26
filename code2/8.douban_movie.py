#coding:utf-8
from __future__ import unicode_literals

import requests
import json

# python
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


class Douban(object):
    def __init__(self):
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?&start=0&count=100"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        }

    def get_data(self):
        # 发送请求获取json响应数据
        response = requests.get(self.url,headers=self.headers)
        return response.content.decode()

    def parse_data(self,data):
        # 将json字符串转换成Python字典
        dict_data = json.loads(data)
        # 使用key获取对应的值
        movie_list= dict_data['subject_collection_items']

        # 构建一个存储数据列表(用于将数据一并返回)
        data_list= []
        for movie in movie_list:
            #创建存放单条数据的字典
            temp = {}
            temp['title'] = movie['title']
            temp['url'] = movie['url']
            # 将数据放到列表中
            data_list.append(temp)
        return data_list

    def save_data(self,data_list):
        with open('douban1.json','w') as f:
            for data in data_list:
                # 字典数据转换成字符串
                str_data = json.dumps(data,ensure_ascii=False) + ',\n'
                f.write(str_data)

    def run(self):
        # url
        # headers
        # 发起请求，获取响应
        data = self.get_data()
        # 解析数据
        data_list = self.parse_data(data)
        # 保存数据
        self.save_data(data_list)



if __name__ == '__main__':
    douban = Douban()
    douban.run()