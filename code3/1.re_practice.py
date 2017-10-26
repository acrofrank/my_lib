#coding:utf-8
import re

# 字符串本身
data = "abcd,bc"

# print (re.findall('bc',data))

# .匹配所有，除了\n，开启dotall匹配\n

data1 = "a\nb"

# print (data1)
# print (re.findall('a.b',data1,re.DOTALL))
# print (re.findall('a.b',data1,re.S))

# \转义

data2 = "a|b"
# print(re.findall("a\|b",data2))

# 范围
data3 = "abc——adc"
# print (re.findall("abc|adc",data3))


# 预定义字符集
#\d

data4 = '1234sdjhfg2354346dfg'
# print(re.findall('\d+',data4))


data5 = "123dsfgsg"
# print(re.findall('\d{3}',data5))


# 原始字符串
data6 = r"a\nb"
# print (len(data6))
# print (data6)


pattern= re.compile('正则表达式')


print (re.findall(r"a.*bc","a\nbc",re.DOTALL))
print (re.findall(r"a(.*)b(c)de(f)","a\nbcdef",re.DOTALL))










