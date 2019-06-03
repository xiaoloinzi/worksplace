# encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('http://www.youdao.com')

# 输入框输入内容
driver.find_element_by_id('translateContent').send_keys('selenium')

#删除输入框中的一个m
driver.find_element_by_id('translateContent').send_keys(Keys.BACK_SPACE)

# 输入空格+‘教程’
driver.find_element_by_id('translateContent').send_keys(Keys.SPACE)

# driver.find_element_by_id('translateContent').send_keys('教程')

# 全选输入框中的内容
driver.find_element_by_id('translateContent').send_keys(Keys.CONTROL,'a')

# 剪切输入框中的内容
driver.find_element_by_id('translateContent').send_keys(Keys.CONTROL,'x')

# 粘贴输入框中的内容
driver.find_element_by_id('translateContent').send_keys(Keys.CONTROL,'v')

# 通过回车键代替单击操作
driver.find_element_by_id('translateContent').send_keys(Keys.ENTER)

driver.quit()




























