# encoding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()

# driver.get('http://www.baidu.com')#打开网页
#
# print u'设置浏览器的宽480、高800显示'
#
# driver.maximize_window()#全屏显示
# # driver.set_window_size(480,800)#设置网页的大小
# driver.quit()#关闭网页/退出网页
first_url = 'http://www.baidu.com'
print u'现在的网页是%s'%first_url
driver.get(first_url)

# second_url = 'http://news.baidu.com'
# print u'现在的网页是%s'%second_url
# driver.get(second_url)
#
# print u'后退到%s'%first_url

# driver.back()# 后退
#
# print u'前进到%s'%second_url
# driver.forward()#前进
# driver/quit()
driver.refresh()#刷新页面
print u'现1在的网页是%s'%first_url








