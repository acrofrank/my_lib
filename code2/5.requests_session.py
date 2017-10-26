#coding:utf-8
from __future__ import unicode_literals
import requests
import re


# 1 构建一个url
url = 'http://www.renren.com/PLogin.do'
# 2 构建请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    }
# 3 构建表单数据
post_data = {
    "email": "17173805860",
    "password": "1qaz@WSX3edc"
}
# 4 发送请求，获取响应,session自动管理状态，保持会话
session = requests.session()
session.post(url, headers=headers, data=post_data)

# 5 跳转
# 并没有cookies，headers，但是依然跳转成功，说明session自动保持会话
response = session.get('http://www.renren.com/923768535')

# 6 验证
print (re.findall('迷途',response.content.decode()))