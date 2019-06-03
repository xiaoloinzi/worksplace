# encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver  = webdriver.Chrome()
driver.get('http://www.youdao.com')

right_click = driver.find_element_by_id('keyfrom')

ActionChains(driver).double_click(right_click).perform()


























