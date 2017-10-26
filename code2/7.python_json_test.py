#coding:utf-8
import json

data= '{"class":"python11"}'
print (type(data))
dict_data = json.loads(data)
print (type(dict_data))
data2 = json.dumps(dict_data)
print (type(data2))

# json.load与json.dump的应用
f = open('temp.txt','w')
json.dump(dict_data,f)
f.close()

fr = open("temp.txt",'r')
dict_data2 = json.load(fr)
print (dict_data2)
print (type(dict_data2))
