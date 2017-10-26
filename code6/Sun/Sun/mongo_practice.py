#coding:utf-8

# 倒包
from pymongo import MongoClient

# 链接数据库服务器
client = MongoClient('127.0.0.1',27017)

# 选择数据库
# db = client.chuanzhi
db = client['chuanzhi']

# 选择集合
# col = db.test
col = db['test']

# for i in range(1,13):
#     key = str(i)
#     col.insert({key:i*i+10})
data = col.find()
for d in data:
    print (d)

# 查询一条
# data= col.find_one()
# print (data)

# col.remove({"1":11})