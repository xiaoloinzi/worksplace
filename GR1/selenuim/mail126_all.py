# encoding=utf-8
# 未封装的登录和退出模块
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.126.com')


driver.switch_to_frame('x-URS-iframe')
# 登录
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('username')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('password')
driver.find_element_by_id('dologin').click()


# 收信、写信、删除信等操作
# 。。。。。。。。。


# 退出
driver.find_element_by_link_text('退出').click()

driver.quit()