# encoding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.126.com')

driver.switch_to_frame('x-URS-iframe')
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('username')
print 'sccuess'
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('passwoed')
print 'dd'
driver.find_element_by_id('dologin').click()
