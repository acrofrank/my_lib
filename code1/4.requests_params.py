#coding:utf-8
import requests

# 构建url
url = 'https://www.baidu.com/s?'
# 构建请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}

# 构建发送数据
params = {
    "wd": "长城"
}

# 发送请求获取响应
response = requests.get(url, headers=headers, params=params)

# 将数据写入到文件
with open('baidu.html','w') as f:
    f.write(response.content.decode())

# 源码保存
with open('baidu2.html','wb') as f:
    f.write(response.content)
