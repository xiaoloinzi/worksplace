# encoding=utf-8
from selenium import webdriver



def login():
    driver.switch_to_frame('x-URS-iframe')
    # 登录
    driver.find_element_by_name('email').clear()
    driver.find_element_by_name('email').send_keys('username')
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys('password')
    driver.find_element_by_id('dologin').click()

def logout():
    driver.switch_to_frame('x-URS-iframe')
    driver.find_element_by_link_text('退出').click()
    driver.quit()


driver = webdriver.Firefox()
driver.get('http://www.126.com')


login()#调用登录模块

# 收信、写信、删除信等操作
# 。。。。。。。。。


logout()# 调用退出模块










