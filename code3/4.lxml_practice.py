#coding:utf-8
# 导入
from lxml import etree

# 获取数据
text = ''' 
<div> 
    <ul> 
        <li class="item-1"><a href="link1.html"></a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul> 
</div> 
'''
# 将响应数据转换为element文档，可以传bytes类型，会自动补全
html = etree.HTML(text)
# print (dir(html))

print (html.xpath('//li[@class="item-1"]/a/text()'))
print (html.xpath('//li[@class="item-1"]/a/@href'))

# 提取数据
text_list = html.xpath('//li[@class="item-1"]/a/text()')
link_list = html.xpath('//li[@class="item-1"]/a/@href')

print ("$"*100000)
# zip对列表文件进行一一对应，需要注意的是木桶原理
for data in zip(text_list,link_list):
    print (data)
print("$" * 100000)
# 获取接节点，从节点中抽取数据，避免数据混乱
node_list = html.xpath('//li[@class="item-1"]/a')
for node in node_list:
    temp = {}
    temp['text'] = node.xpath('./text()')[0] if len(node.xpath('./text()')) > 0 else None
    temp['link'] = node.xpath('./@href')[0] if len(node.xpath('./@href')) > 0 else None
    print (temp)



# print (type(html))
# print (html)

# etree.tostring将element对象转换为字符串
# print (etree.tostring(html))