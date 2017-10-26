#coding:utf-8


#1 什么是爬虫
    #模拟客户端发送请求获取响应数据，从响应中提取数据，自动运行的程序
#2 爬虫分类
    通用
    聚焦
#3 http与https的区别
    速度
    安全性
#4 url结构
    http://ip:port/path[?参数名=参数值&...]#detail
#5 dns服务器的功能
    解析域名，返回对应的IP地址
#6 get与post区别
    参数的位置   url      实体数据
    数据的大小   get小    post大
    安全性      get不安全 post相对安全

#7 状态码
    1   略
    2   200 ok
    3   302 临时重定向
    4   403 forbidden
        404 not found
    5   服务器错误
        500
        503
#8 字符串转化
    str     bytes
    str.encode() ---->bytes
    bytes.decode() ---->str

#9 requests的使用
    get post
    # 发送一个简单的请求
    requests.get(url)
    # 发送一个带用户头的请求
    requests.get(url,headers=headers)
    headers格式是字典
    # 发送一个带参数的请求
    requests.get(url,headers=headers,params=params)
