#coding:utf-8

import requests

# 1 构建一个url
url = 'http://www.baidu.com'
# 2 构建一个请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
# 3 发送请求
response = requests.get(url,headers=headers)
print(len(response.content))

# 不带请求头
response1 = requests.get(url)
print(len(response1.content))