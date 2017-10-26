#coding:utf-8
import redis
from pymongo import MongoClient
import json
# 链接redis数据库
redis_cli = redis.Redis(host='172.16.123.128', port=6379, db=0)

# 链接mongo
mongo_cli = MongoClient('127.0.0.1',27017)
db = mongo_cli['Tianqi']
col = db['tianqi']


while True:
    # 从redis中读取数据
    source,data = redis_cli.blpop(['tianqi:items'])

    # print (source)
    # print (data)
    dict_data = json.loads(data.decode())

    # 写入mongodb数据库
    print (dict_data)
    col.insert(dict_data)