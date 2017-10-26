#coding:utf-8

# data = 'python11'
data = "传智"

print(type(data))
print(data)

# 字符串类型转换成bytes类型
print("*"*50)
b_data = data.encode("utf-8")
print(type(b_data))
print(b_data)

#bytes类型转换成字符串类型
#####编码格式必须一样，不一样，可能会乱码或者报错
str_data = b_data.decode("gbk")
print(type(str_data))
print(str_data)