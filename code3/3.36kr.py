#coding:utf-8

from api import get_page
import re
import json

class Kr36(object):
    def __init__(self):
        self.url = 'http://36kr.com/'
        self.pattern = re.compile('<script>var props=({.*?}}})</script>',re.S)
        """
        <script>var props=({.*?}}}</script>
        """

    def parse_data(self,str_data):
        # 使用正则匹配数据
        str_data = self.pattern.findall(str_data)[0]
        # 转换出错，说明数据格式不符合json格式，保存一下，查看问题所在
        # with open('temp.json','w')as f:
        #     f.write(str_data)

        # 将有问题的地方去掉，用空字符串进行替换
        str_data2 = re.sub(',locationnal=.*',"",str_data)
        with open('temp2.json','w')as f:
            f.write(str_data2)

        # 转换成功，提取数据
        data_list = json.loads(str_data2)['feedPostsLatest|post']
        return data_list
        # for data in data_list:
        #     print(data)

    def save_data(self,data_list):
        with open('36kr.json','w')as f:
            for data in data_list:
                str_data = json.dumps(data,ensure_ascii=False) + ",\n"
                f.write(str_data)

    def run(self):
        # url
        # 发送请求获取响应
        str_data = get_page(self.url)
        # 解析数据
        data_list = self.parse_data(str_data)
        # 保存
        self.save_data(data_list)

if __name__ == '__main__':
    kr36 = Kr36()
    kr36.run()