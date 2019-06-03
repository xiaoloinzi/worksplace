# encoding=utf-8
from selenium import webdriver
from public import Login

driver = webdriver.Firefox()
driver.get('http://www.126.com')

# 调用登录模块
Login.user_login()


# 写信，删除信，收信
# .................


# 调用退出模块
Login.user_logout()




