# encoding=utf-8
from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_path = 'file://'+os.path.abspath('html/checkbox.html')
driver.get(file_path)

# 选择页面上的所有tag name为input的元素
inputs = driver.find_elements_by_tag_name('input')

# 然后从中过滤出type为CheckBox的元素，单击勾选

for i in inputs:
    if i.get_attribute('type') == 'checkbox':
        print i
        i.click()
        time.sleep(1)
driver.quit()








