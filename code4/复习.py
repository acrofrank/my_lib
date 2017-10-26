#coding:utf-8

# 1 正则表达式

    # 1.0 什么是正则表达式
        使用规则字符串进行过滤，字符串
    # 1.1 使用re.compile()编译一个正则表达式对象进行匹配相对于直接调用的好处
        一次编译，多次使用
    # 1.2 在使用'.'进行匹配的时候，如何使之能够匹配换行符'\n'
        DOTALL模式
        re.DOTALL
        re.S
    # 1.3 如何进行非贪婪匹配
        在数量词(*,+)后面加？
    # 1.4 正则表达式如何进行分组
        使用()分组

# 2 xpath与lxml

    # 2.1 xpath是什么
        用于从html，xml中定位数据的语言
    # 2.2 xml与html的设计目的
        xml使用用来传输存储
        html用来展示
    # 2.3 如何使用标签属性值进行节点的获取
        /html/head/meta[@class=""]/a/@href
        /html/head/meta[@class=""]/a/@src
    # 2.4 如何进行多路径表达获取
        xpath1 | xpath2
        应对 网站结构不一样的情况
    # 2.5 lxml如何使用
        # 1 导入
            from lxml import etree
        # 2 生成element对象
            html = etree.HTML(响应)
            etree.tostring(html)
        # 3 获取数据
            html.xpath('路径表达式')
