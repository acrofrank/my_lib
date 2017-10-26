#coding:utf-8
from selenium import webdriver

driver = webdriver.Chrome()
# 请求网站
driver.get('http://qzone.qq.com')
# 找到框架元素，进入框架
el_iframe = driver.find_element_by_xpath('//*[@id="login_frame"]')
driver.switch_to.frame(el_iframe)

# 在框架中点击账号密码登录
el = driver.find_element_by_xpath('//*[@id="switcher_plogin"]')
print (el.text)
el.click()

# 定位到账号输入处，输入账号
el_user = driver.find_element_by_xpath('//*[@id="u"]')
el_user.send_keys('2634809316')

# 输入密码
el_user = driver.find_element_by_xpath('//*[@id="p"]')
el_user.send_keys('461324karura')

# 点击登录
el_su = driver.find_element_by_xpath('//*[@id="login_button"]')
el_su.click()

