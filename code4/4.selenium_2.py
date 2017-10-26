#coding:utf-8

from selenium import webdriver


driver = webdriver.Chrome()
# 请求网站
driver.get('http://bj.58.com/')
# 定位元素
el = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/em[1]/a')
# 模拟点击
el.click()
# 查看当前url
print (driver.current_url)
print (driver.window_handles)

driver.switch_to.window(driver.window_handles[1])
print (driver.current_url)


# 关闭
