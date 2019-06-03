# encoding=utf-8
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath('html/frame.html')
driver.get(file_path)

driver.switch_to_frame('if')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

# 截取当前窗口，并指定截图图片的位置
driver.get_screenshot_as_file('baidu_img.jpg')

driver.quit()