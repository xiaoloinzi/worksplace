# encoding=utf-8
from selenium import webdriver
import time,os

driver = webdriver.Firefox()
file_path = 'file://'+os.path.abspath('frame.html')
driver.get(file_path)

# 设置浏览窗口的大小
driver.set_window_size(600,600)

# 切换到iframe(id='if')
driver.switch_to_frame('if')

# ss
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(3)

# 通过JavaScript设置窗口的滚动条
js = 'window.scrollTo(100,500)'
driver.execute_script(js)
time.sleep(3)

driver.quit()


































