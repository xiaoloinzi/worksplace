# encoding=utf-8
# encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime
import re

# driver = webdriver.Firefox()
#
# driver.implicitly_wait(10)
# driver.get('http://www.youdao.com')
#
# try:
#     print (ctime())
#     driver.find_element_by_id('kw22').send_keys('selenium')
# except NoSuchElementException as e:
#     print (e)
# finally:
#     print (ctime())
#     driver.quit()

s = '22s321Ad22221'
a = '1882413113049'
if re.match('^(?=.*?[A-Za-z]+)(?=.*?[0-9]+)(?=.*?[A-Z]).*$',s):
    print 1
if re.match('^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$',a):
    print 3
else:
    print 2























































