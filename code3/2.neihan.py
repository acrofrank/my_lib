#coding:utf-8
from api import get_page
import re
import json

class Neihan(object):
    def __init__(self):
        self.url = 'http://neihanshequ.com/'
        self.pattern = re.compile('<a target="_blank" class="image share_url" href="(.*?)".*?<p>(.*?)</p>',re.S)
        """
        <a target="_blank" class="image share_url" href="(.*?)".*?<p>(.*?)</p>
        """

    def parse_data(self,str_data):
        # 正则匹配出数据
        result_list = self.pattern.findall(str_data)

        data_list = []

        for url,content in result_list:
            temp = {}
            temp['url'] = url
            temp['content'] = content
            data_list.append(temp)
        # 返回数据
        return data_list

    def save_data(self,data_list):
        with open('neihan.json','w')as f:
            for data in data_list:
                str_data = json.dumps(data,ensure_ascii=False) + ",\n"
                f.write(str_data)



    def run(self):
        # 1 构建url
        # 2 构建请求头
        # 3 发送请求获取响应
        str_data = get_page(self.url)
        # 4 从响应中抽取数据
        data_list = self.parse_data(str_data)
        # 5 保存
        self.save_data(data_list)

if __name__ == '__main__':
    neihan = Neihan()
    neihan.run()