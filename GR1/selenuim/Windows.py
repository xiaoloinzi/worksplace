# encoding=utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
time.sleep(2)
driver.get('http://www.baidu.com')

sreach_windows = driver.current_window_handle

driver.find_element_by_link_text('登录')
driver.find_element_by_link_text('注册')

all_windows = driver.window_handles


for handle in all_windows:
    if handle == sreach_windows:
        driver.switch_to_window(handle)
        print 'now register window'
        driver.find_element_by_name('account').send_keys('username')
        driver.find_element_by_name('password').send_keys('password')
        time.sleep(3)


for handle in all_windows:
    if handle == sreach_windows:
        driver.switch_to_window(handle)
        print 'now sreach window'
        driver.find_element_by_id('TANGRAM_PSP_2_closeBtn').click()
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
        time.sleep(3)

driver.quit()



































