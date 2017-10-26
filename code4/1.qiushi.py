#coding:utf-8

import requests
from lxml import etree
import json

class Qiushi(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.url_list = None
        self.host = 'https://www.qiushibaike.com'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }

    def generate_url(self):
        # for i in range(1,14):
        #     url = self.base_url.format(i)
        #     self.url_list.append(url)
        self.url_list = [self.base_url.format(i) for i in range(1,14)]


    def get_page(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content.decode()

    def parse_data(self,str_data):
        # 将响应数据转换成element对象
        html = etree.HTML(str_data)

        # 获取所有的帖子节点
        node_list = html.xpath('//*[@id="content-left"]/div')
        # print (len(node_list))

        data_list = []
        # 遍历节点列表，从节点中抽取数据
        for node in node_list:
            temp = {}
            try:
                temp['user'] = node.xpath('./div[1]/a[2]/h2/text()')[0].strip()
                temp['link'] = self.host + node.xpath('./div[1]/a[2]/@href')[0]
                temp['age'] = node.xpath('./div[1]/div/text()')[0]
                temp['gender'] = node.xpath('./div[1]/div/@class')[0].split(' ')[-1].replace('Icon','')
            except:
                temp['user'] = '匿名用户'
                temp['link'] = None
                temp['age'] = None
                temp['gender'] = None
            temp['content'] = node.xpath('./a[1]/div/span/text()')[0].strip()
            temp['url'] = self.host + node.xpath('./a[1]/@href')[0]

            data_list.append(temp)

        # 返回数据
        return data_list

    def save_data(self,data_list):
        with open('qiushi.json','a')as f:
            for data in data_list:
                str_data = json.dumps(data,ensure_ascii=False) + ',\n'
                f.write(str_data)


    def run(self):
        # 1 生成 url 列表
        self.generate_url()
        # print (self.url_list)

        # 2 构建请求头
        # 3 编列url表
        for url in self.url_list:
            # 3.1 发情请求，获取响应
            str_data = self.get_page(url)
            # 3.2 解析数据
            data_list = self.parse_data(str_data)
            # 3.3 保存
            self.save_data(data_list)


if __name__ == '__main__':
    qiushi = Qiushi()
    qiushi.run()