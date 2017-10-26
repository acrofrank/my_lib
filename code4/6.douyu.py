#coding:utf-8

from selenium import webdriver
import json
import time

class Douyu(object):
    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        # 创建浏览器对象
        self.driver = webdriver.Chrome()

    def parse_data(self):
        node_list = self.driver.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li')


        data_list = []
        # 遍历节点列表，从节点中抽取数据
        for node in node_list:
            temp = {}
            temp['title'] = node.find_element_by_xpath('./a/div/div/h3').text
            temp['type'] = node.find_element_by_xpath('./a/div/div/span').text
            temp['user'] = node.find_element_by_xpath('./a/div/p/span[1]').text
            temp['num'] = node.find_element_by_xpath('./a/div/p/span[2]').text
            temp['cover'] = node.find_element_by_xpath('./a/span/img').get_attribute('data-original')
            temp['url'] = node.find_element_by_xpath('./a').get_attribute('href')
            data_list.append(temp)
            print (temp)
        return data_list

    def save_data(self,data_list):
        with open('douyu.json','a')as f:
            for data in data_list:
                str_data = json.dumps(data,ensure_ascii=False) + ',\n'
                f.write(str_data)

    def __del__(self):
        self.driver.close()

    def run(self):
        # 1 url
        # 2 发起请求获取响应
        self.driver.get(self.url)
        while True:
            # 3 解析数据
            data_list = self.parse_data()
            # 4 保存数据
            self.save_data(data_list)
            # 5 翻页
            try:
                el_next = self.driver.find_element_by_xpath('//a[@class="shark-pager-next"]')
                el_next.click()
                time.sleep(3)
            except:
                break

if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()