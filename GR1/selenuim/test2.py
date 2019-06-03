# encoding=utf-8
from selenium import webdriver
from time import sleep,ctime

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

print ctime()
for i in xrange(10):
    try:
        el = driver.find_element_by_id('kw22')
        if el.is_displayed():
            break
    except:
        pass
else:
    print 'time out'
driver.close()
print ctime()















