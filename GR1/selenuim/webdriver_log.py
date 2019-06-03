# encoding=utf-8
from selenium import webdriver
import logging,os,time

logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Firefox()
file_path = 'file://'+os.path.abspath('html/frame.html')
driver.get(file_path)

driver.switch_to_frame('if')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(3)

driver.quit()






































