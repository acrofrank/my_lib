#coding:utf-8
from __future__ import unicode_literals
import requests

# url
dsfasdfasd
url = "http://www.163.com"
# headers
headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        }
# 构建代理
# 使用免费代理,不好吃
# proxies = {
#     "http":"http://105.235.201.250:8080",
#     "https":"https://105.235.201.250:8080",
# }
# 是费用付费代理，人民币玩家，花钱太多
proxies = {
    "http":"http://morganna_mode_g:ggc22qxp@121.41.8.23:16816",
    "https":"https://morganna_mode_g:ggc22qxp@121.41.8.23:16816",
}


# 发送请求
response = requests.get(url, headers=headers, proxies=proxies)
print(response.content)



# 如何验证代理是否成功使用
    # 只要使用成功，就能拿到响应