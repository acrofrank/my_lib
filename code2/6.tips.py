#coding:utf-8
import requests


######################## 演示cookiejar与Python字典之间的转换
# url = "http://www.baidu.com"
# response = requests.get(url)
# jar_data = response.cookies
# print (jar_data)
#
# 将cookiesjar数据转化成字典数据
# dict_data= requests.utils.dict_from_cookiejar(jar_data)
# print (dict_data)
# print (type(dict_data))
#
# jar_data2 = requests.utils.cookiejar_from_dict(dict_data)
# print (jar_data2)
# print (type(jar_data2))

######################## 演示关闭ssl认证
# url= 'https://www.12306.cn/mormhweb/'
# try:
#     response = requests.get(url)
# except Exception as e:
#     print (e)
#     response = requests.get(url,verify=False)
# print (response.content)

######################## timeout
# url = 'http://www.youtube.com'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
#     }
# requests.get(url, headers=headers, timeout=3)






