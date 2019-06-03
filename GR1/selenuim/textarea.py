# encoding=utf-8

from selenium import webdriver
import os ,time

driver = webdriver.Firefox()
file_path = 'file://'+os.path.abspath('html/textarea.html')

text = 'input text'

js = "var sum = document.getElementById('id'); sum.value='"+text+"';"

driver.execute_script(js)


time.sleep(3)

driver.quit()

























