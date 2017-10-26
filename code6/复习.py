#coding:utf-8

1 scrapy框架结构

2 scrapy各模块功能
    引擎
        负责各模块之间的通信，数据交互
    爬虫
        1.发起起始的请求
            start_request
        2.从响应中提取数据和跟进url
    调度器
        1.将请求去重之后放到请求队列中
        2.返回请求给引擎
    下载器
        接受请求，返回响应
    item管道
        定义对数据的操作
        写文件
        写数据库

3 scrapy开发流程
    3.0 开发流程
        创建项目----项目文件
        明确目标----建模
        创建爬虫----创建爬虫(命令&手动)
                    编写爬虫
    3.1 如何创建一个项目
        scrapy startproject project_name
    3.2 明确目标需要做什么，这么做有什么好处
        字段检查
    3.3 创建项目需要用到的参数，需要关注的事情
        scrapy genspider name domain
    3.4 如何保存内容
        1.编写pipeline文件
            process_item(self, item, spider)
            return item
            open_spider
            close_spider
4 scrapy shell调试
    4.1 主要用来干什么
        调试xpath，css
    4.2 如何加载请求头
        scrapy shell -s USER_AGENT=""
