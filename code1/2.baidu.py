#coding:utf-8

# 导入requests库
import requests

# 构建url(url必须带有协议)
url = "http://www.baidu.com"
# 发送请求，获取响应
response = requests.get(url)

# 打印状态码
# print(response.status_code)

# 打印请求头
# print(response.request.headers)

# 打印响应头
# print(response.headers)

# 打印响应对应的url
# print(response.url)

# 打印二进制源码
# print (response.content.decode())


# 打印字符串类型
# print (response.encoding)
response.encoding='utf-8'
print (response.text)

