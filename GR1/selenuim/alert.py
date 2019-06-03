# encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 鼠标悬停至设置连接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

# 打开搜索位置
driver.find_element_by_link_text('搜索设置').click()

# 保存位置
driver.find_element_by_name('prefpanelgo').click()
time.sleep(3)

# 接受警告框
driver.switch_to_alert().accept()

driver.quit()












































