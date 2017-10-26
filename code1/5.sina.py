#coding:utf-8

import requests

# 构建url
url = 'http://www.sina.com.cn/'
# 构建请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
# 发送请求
response = requests.get(url,headers=headers)
response.encoding='utf-8'
# print(response.text)
# print(type(response.text))

print(response.content.decode())