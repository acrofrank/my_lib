#coding:utf-8
from __future__ import unicode_literals
import requests
from lxml import etree
import sys,os
import json

class Tieba_picture(object):
    def __init__(self,tieba_name):
        self.url = "https://tieba.baidu.com/f?kw=%s"%(tieba_name)
        self.headers = {
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0) "
        }
        self.file = open('baidu.josn','w')

    def get_page(self,url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def parse_data(self,str_data):
        # 将html源码转化成element对象
        html = etree.HTML(str_data)

        node_list = html.xpath('//li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')
        # print (len(node_list))
        detail_list = []
        for node in node_list:
            temp = {}
            temp['title'] = node.xpath('./text()')[0]
            temp['link'] = 'https://tieba.baidu.com' + node.xpath('./@href')[0]
            detail_list.append(temp)

        # 获取下一页url链接
        try:
            next_url = 'https:' + html.xpath('//a[@class="next pagination-item"]/@href')[0]
        except:
            next_url = None

        return detail_list,next_url

    def parse_detail(self,str_data):
        # 将html源码转化成element对象
        html = etree.HTML(str_data)
        # 将图片链接提取出来
        image_list = html.xpath('//cc/div/img[1]/@src')

        return image_list


    def download(self,image_list):
        # 判断存放图片的目录是否存在，不存在则创建
        if not os.path.exists("images"):
            os.makedirs("images")

        for url in image_list:
            # 拼接文件名
            filename = 'images' + os.sep + url.split('/')[-1]
            # 下载图片数据
            bytes_data = self.get_page(url)
            # 写文件，图片，电影，安装包等必须以二进制的形式写入
            with open(filename,'wb') as f:
                f.write(bytes_data)

    def save_data(self,data):
        # 将字典数据转换为字符串数据
        str_data = json.dumps(data,ensure_ascii=False) + ",\n"
        # 写入文件
        self.file.write(str_data)


    def __del__(self):
        self.file.close()

    def run(self):
        # 1 起始的url
        # 2 构建请求头
        next_url = self.url

        while next_url:
            # 3 发起请求获取(列表页面)响应
            str_data = self.get_page(next_url)

            # 4 从响应中解析出 详细页面数据列表，下一页url
            detail_list,next_url = self.parse_data(str_data)
            # 5 获取详细页面的源码，需要遍历
            for detail in detail_list:
                url = detail['link']
                # 获取详细页面响应
                detail_data = self.get_page(url)
                # 从详情页面响应中抽取图片地址列表
                image_list = self.parse_detail(detail_data)
                # 下载图片
                self.download(image_list)
                # 保存数据
                detail['images'] = image_list
                self.save_data(detail)


if __name__ == '__main__':
    tieba = Tieba_picture("美女")
    tieba.run()