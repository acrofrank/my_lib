#coding:utf-8

1.1 redis数据库的配置启动
    配置文件 bind 127.0.0.1
    redis-server redis.conf
    linux
        sudo
    windows
        管理员权限
    配置环境变量
        window
        linux   /usr/bin

        # 查看linux环境变量
        $PATH

1.2 分布式的概念
    多台机器协同完成一个任务

1.3 使用分布式的优点
    加快整个项目的速度
    单个节点的不稳定性不会影响整体

1.4 为什么使用scrapy_redis实现分布式爬虫
    scrapy不能共享任务队列

1.5 scrapy_redis的设计逻辑
    将scrapy与redis粘合起来

2.1 分布式爬虫如何实现
    1.先完成普通爬虫
    2.修改成分布式


2.2 将普通爬虫修改成分布式爬虫的步骤
    1 修改爬虫文件
        1.1 倒包
        1.2 修改继承
        1.3 注销起始的url和允许的域
        1.4 动态获取允许的域
        1.5 redis_key



3.1 为什么要对scrapy_redis分布式爬虫做数据持久化
    redis数据库容量小
    reids数据库内存型，断点数据消失
    数据并不重要
