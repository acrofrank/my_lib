#coding:utf-8

import requests
import json
import sys
class Trans(object):
    def __init__(self,word):
        self.word = word
        self.url = 'http://fanyi.baidu.com/v2transapi'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }
        self.post_data = {
            "from": "zh",
            "to": "en",
            "query": word,
            "transtype": "translang",
            "simple_means_flag": 3
        }

    def get_data(self):
        # 发送post请求
        response = requests.post(self.url,data=self.post_data,headers=self.headers)
        return response.content.decode()

    def parse_data(self,data):
        # 将json字符串转换成Python字典
        dict_data = json.loads(data)
        # print (type(dict_data))
        # 使用字典键值索引的方式获取数据
        dst = dict_data['trans_result']['data'][0]['dst']
        print (self.word + ' -----> ' +dst)

    def run(self):
        # 1 构建url
        # 2 构建请求头
        # 3 构建请求数据
        # 4 发送求求获取响应
        data = self.get_data()
        # print (data)
        # 5 提取结果
        self.parse_data(data)

if __name__ == '__main__':
    trans = Trans(sys.argv[1])
    trans.run()