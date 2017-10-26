#coding:utf-8

# 导入webdriver
from selenium import webdriver
import time

# 创建一个浏览器对象
# driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

# 发起请求
# driver.get('http://www.baidu.com')

# 保存快照
# driver.save_screenshot("baidu.png")

# 定位到节点
# el = driver.find_element_by_id('kw')
# el = driver.find_element_by_xpath('//*[@id="kw"]')
# el = driver.find_element_by_css_selector('#kw')
# el = driver.find_element_by_link_text('新闻')
#
# print (el)
# 模拟点击
# el.click()
#
# 节点输入,能使用send_keys的必须是input，text
# el.send_keys('python11期')

# 变量信息展示
# print (driver.page_source)
#
# print (driver.current_url)
#
# print (driver.get_cookies())
#


# 获取复数个元素
driver.get('http://bj.58.com/chuzu/')

el_list = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div[5]/div[2]/ul/li/div[2]/h2/a')
for el in el_list:
    print (el.text,el.get_attribute('href'))





time.sleep(10)


# 退出浏览器
driver.close()
driver.quit()