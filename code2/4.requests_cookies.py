#coding:utf-8
import requests
import re

url = 'http://www.renren.com/923768535'
# 构建请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    }

temp = "anonymid=j6c96snx6i82ml; _r01_=1; depovince=BJ; JSESSIONID=abcuKWLdqxTjJbjrR9X7v; jebe_key=2b511d4c-0b0e-4e77-bcbd-28616d344a3d%7Ceda913e449d4d8cd6ac80727da63a1fe%7C1507298042637%7C1%7C1507298042328; _ga=GA1.2.1361939841.1504226199; _gid=GA1.2.1639587085.1507300736; ch_id=10016; jebecookies=01f29853-5d04-48d0-a2d4-0ef2bfa1657e|||||; ick_login=044f4772-831d-4a9d-9f7d-29b6051ee4b6; _de=4F1FF60C280AA48B2CD1201DB4C6DF4A; p=c3148efff984658f83e0ccb5b36598b75; first_login_flag=1; ln_uact=17173805860; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=1f694eb301b54924d148c04eca6da9b35; societyguester=1f694eb301b54924d148c04eca6da9b35; id=923768535; xnsid=b77fd1e; ver=7.0; loginfrom=null; wp_fold=0"

temp_dict = {}
for data in temp.split("; "):
    temp_dict[data.split('=')[0]] = data.split('=')[1]

# 发送请求获取响应
response = requests.get(url, headers=headers, cookies=temp_dict)
# print (response.content.decode())

print (re.findall('迷途',response.content.decode()))