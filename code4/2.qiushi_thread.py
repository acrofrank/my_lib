#coding:utf-8

import requests
from lxml import etree
import json
from queue import Queue
import threading

class Qiushi(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/8hr/page/{}/'
        # self.url_list = None
        self.host = 'https://www.qiushibaike.com'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }
        self.url_queue = Queue()
        self.str_data_queue = Queue()
        self.data_list_queue = Queue()

    def generate_url(self):
        # self.url_list = [self.base_url.format(i) for i in range(1,14)]
        print ("生成url，放到url队列中")
        for i in range(1,14):
            url = self.base_url.format(i)
            self.url_queue.put(url)


    def get_page(self):
        while True:
            url = self.url_queue.get()
            print("获取{}的响应".format(url))
            try:
                response = requests.get(url,headers=self.headers)
                print (response.status_code)
                str_data = response.content.decode()
            except:
                str_data = None
            self.str_data_queue.put(str_data)
            self.url_queue.task_done()


    def parse_data(self):
        while True:
            print ("解析数据")
            str_data = self.str_data_queue.get()
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
            self.data_list_queue.put(data_list)
            self.str_data_queue.task_done()

    def save_data(self):
        while True:
            print ('保存数据列表')
            data_list = self.data_list_queue.get()
            with open('qiushi.json','a')as f:
                for data in data_list:
                    str_data = json.dumps(data,ensure_ascii=False) + ',\n'
                    f.write(str_data)
            self.data_list_queue.task_done()


    def run(self):
        # # 1 生成 url 列表
        # self.generate_url()
        # # print (self.url_list)
        #
        # # 2 构建请求头
        # # 3 编列url表
        # for url in self.url_list:
        #     # 3.1 发情请求，获取响应
        #     str_data = self.get_page(url)
        #     # 3.2 解析数据
        #     data_list = self.parse_data(str_data)
        #     # 3.3 保存
        #     self.save_data(data_list)

        # 创建一个线程列表
        thread_list = []

        # 创建生成url的线程
        t_url_list = threading.Thread(target=self.generate_url)
        thread_list.append(t_url_list)

        # 创建请求线程
        for i in range(4):
            t = threading.Thread(target=self.get_page)
            thread_list.append(t)

        # 创建解析数据的线程
        for i in range(4):
            t = threading.Thread(target=self.parse_data)
            thread_list.append(t)

        # 创建数据存储线程
        t_save_data = threading.Thread(target=self.save_data)
        thread_list.append(t_save_data)

        # 遍历启动
        for t in thread_list:
            # 将线程设置为守护线程，线程将无条件跟从主线程的退出而退出
            t.setDaemon(True)

            t.start()

        # 设置主线程等待队列操作完毕
        for q in [self.url_queue,self.str_data_queue,self.data_list_queue]:
            q.join()




if __name__ == '__main__':
    qiushi = Qiushi()
    qiushi.run()