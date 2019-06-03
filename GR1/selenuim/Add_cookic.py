# encoding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.youdao.com')

# 向cookies的name和value中添加会话信息
cookic = driver.add_cookie({'name':'key-aaaa','value':'value-bbbb'})

# 遍历cookies中的name和value信息并打印，当然还有上面添加的信息

for cookie in driver.get_cookies():
    print cookie
    print '%s->%s'%(cookie['name'],cookie['value'])

driver.quit()


























