#coding:utf-8

# 1 多线程
    # 1.1 如何创建一个线程threading
        t = threading.Thread(target=fun,)
    # 1.2 守护线程是否跟随主线程的退出而退出
        跟随主线程退出而退出
    # 1.3 如何设置守护线程
        t.setDaemon(True)
    # 1.4 如何使主线程等待子线程结束
        t.join()
    # 1.5 queue的使用使为了什么？
        线程安全
# 2 动态html
    # 2.1 如何导入selenium
        from selenium import webdriver
    # 2.2 如何使用selenium
        driver = webdriver.XXXX
    #     8种定位方式
        el = driver.find_element_by_xxxxx
        el_list = driver.find_elements_by_xxxxx

    # 已经定位到节点了，通过什么方法拿数据
        el.text
        el.get_attribute(属性名)

    # iframe框架
    el_frame = driver.find_elements_by_xxxxx()
    driver.switch_to.frame(el_frame)

# 3 图片识别
    # pytesseract库的使用
    from PIL import Image
    pytesseract.image_to_string()

    Appium

# 补充知识
    #验证码的处理
        # 1.图片识别
            pytesseract
        # 2.打码平台
            money
        # 3.selenium高阶模拟鼠标操作

        # 4.多平台测试绕过
