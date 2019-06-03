# encoding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.youdao.com/')



size = driver.find_element_by_id('border').size
print size

text = driver.find_element_by_id('footer').text
print text
# driver.find_element_by_id('translateContent').send_keys('hello')

# driver.find_element_by_id('translateContent').submit()
# 两种方法都可以
# driver.find_element_by_xpath("//input[@name='q']").send_keys('hello')

# driver.find_element_by_xpath("//input[@name='q']").submit()











