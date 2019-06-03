# encoding=utf-8
from selenium import webdriver
from pubic_1 import Login

class LoginTest():
    '''
    创建LoginTest（）类，并在__init__()方法中初始化浏览器驱动、等待时长
    和URL等，这样test_admin_login()与test_guest_login()两个测试
    方法只需关注登录的用户名和密码，通过调用Login（）类的user_login()方法并
    传入具体参数来测试不同用户的登录
    '''

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.126.com')

    #admin用户登录
    def test_admin_login(self):
        username = 'admin'
        password = '123'
        Login.user_login(self.driver,username,password)
        self.driver.quit()

    #guest用户登录
    def test_guest_login(self):
        username = 'guest'
        password = '321'
        Login.user_login(self.driver,username,password)
        self.driver.quit()

LoginTest.test_admin_login()
LoginTest.test_guest_login()


