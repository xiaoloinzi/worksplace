# encoding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.youdao.com')

# 获得cookIC信息
cookic = driver.get_cookies()
print cookic
cookics = driver.get_cookie('domain')
print cookics
driver.quit()



















































