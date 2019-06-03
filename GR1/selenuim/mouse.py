# encoding=utf-8
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get('http://youdao.com')

above = driver.find_element_by_id('more')

ActionChains(driver).move_to_element(above).perform()
















