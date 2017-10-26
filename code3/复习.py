#coding:utf-8

# 1 reuqests深入

    # 1.1 post的用法
        reqests.post(url,data)
    # 1.2 post的使用场景
        登录注册
        发送数据
    # 1.3 requests如何使用代理
        proxies= [
            'ip:port',
            'ip2:por2'
        ]
        proxy = random.choice(proxies)
        n = {
            "http":"http://"+proxy
            "https"："http://"+proxy
        }
        request.get(url,proxies=n)
    # 1.4 为什么使用代理
        降低每个ip的请求次数
    # 1.5 cookie的使用方法
        1 headers中添加
        2 传参，cookies，格式字典
    # 1.6 session的使用方法
        session = requests.session()
        session.get/post
# 2 数据抽取
    # 2.1 什么是数据抽取
        从响应中抽取目标数
    # 2.2 数据的分类并举例
        结构化
            json,xml
        非结构化
            html(re,xpath),文本(re)
# 3 json
    # 3.1 什么是json
        数据交互
    # json与python字典的转换
        #json字符串 ----> python字典
            json.loads(str_data)
        #python字典 ----> json字符串
            jsonl.dumps(json.loads(str_data),en)
