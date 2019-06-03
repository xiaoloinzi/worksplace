# encoding=utf-8
from selenium import webdriver
import os

search_text = ['python','xpath','text']
file_path = 'file://'+os.path.abspath('html/frame.html')

for i in search_text:
    driver = webdriver.Firefox()
    driver.get(file_path)
    driver.switch_to_frame('if')
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys(i)
    driver.find_element_by_id('su').click()
    driver.get_screenshot_as_file('jpg\\'+i+'.jpg')
    driver.quit()








