# encoding=utf-8
from selenium import webdriver
import os,time

driver = webdriver.Firefox()

file_path = 'file:///'+ os.path.abspath('checkbox.html')

driver.get(file_path)
# 通过xpath找到type=CheckBox的元素
checkboxes =driver.find_elements_by_xpath("//input[@type='checkboa']")
# 通过css找到type=CheckBox的元素
checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')

for checkbox in checkboxes:
    print checkbox
    checkbox.click()
    time.sleep(1)

print len(checkboxes)

driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()

driver.quit()








