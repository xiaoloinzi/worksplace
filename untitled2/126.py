# encoding=utf-8
import selenium
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.126.com/')

driver.switch_to.frame(driver.find_element_by_xpath("//input[@class='j-inputtext dlemail']")).clear()
driver.switch_to.frame(driver.find_element_by_xpath("//input[@class='j-inputtext dlemail']")).send_keys('username')
driver.switch_to.frame(driver.find_element_by_xpath("//input[@class='j-inputtext dlpwd']")).clear()
driver.switch_to.frame(driver.find_element_by_xpath("//input[@class='j-inputtext dlpwd']")).send_keys('passwoed')
driver.find_element_by_xpath("dologin").click()



