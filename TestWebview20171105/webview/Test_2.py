# encoding=utf-8
import sys,unittest
import time
import Common
from appium import webdriver
default_encoding = "gb2312"
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding("gb2312")
class Test(unittest.TestCase):
    # define setup method
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '192.168.19.102:5555'
        desired_caps['appPackage'] = 'com.android.browser'
        desired_caps['appActivity'] = '.BrowserActivity'
        desired_caps['browserName']='browser'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print "setup"
    def testBaidu(self):
        self.driver.get("https://www.baidu.com")
        time.sleep(5)
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print "teardown"