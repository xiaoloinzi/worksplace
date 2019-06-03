# encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

driver = webdriver.Firefox()


driver.implicitly_wait(10)
driver.get('http://www.youdao.com')

try:
    print ctime()
    driver.find_element_by_id('kw22').send_keys('selenium')
except NoSuchElementException as e:
    print e
finally:
    print ctime()
    driver.quit()

















































