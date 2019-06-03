# encoding=utf-8
import sys,unittest,time
from appium import webdriver
from TestWebview20171105.webview import Common

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
        desired_caps['deviceName'] = '192.168.19.101:5555'
        # desired_caps['appPackage'] = 'com.example.testWebview'
        desired_caps['appPackage'] = 'com.android.browser'
        # desired_caps['appActivity'] = 'com.my.activity.MainActivity'
        desired_caps['appActivity'] = 'BrowserActivity'
        # desired_caps['browserName'] = 'browser'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print "setup"
    # dumpsys  activity |grep browser----查找浏览器的Activity
    def testBaidu(self):
        self.driver.get('https://www.baidu.com')
        time.sleep(5)
        # 注意原生的Activity的转换驱动是‘NATIVE_APP’
        # 网页版的转换驱动：‘WEBVIEW_包名’
        # 怎么区分是webdriver还是原生的app，使用ui automator view进行抓取，
        # 查看是否能选择页面内部的控件名，不能定位到内部控件名称的就是webview
        # 包名的获取可以通过chrome的争取工具查看
        self.driver.switch_to.context(u'WEBVIEW_com.android.browser')
        time.sleep(5)
        bdtext = Common.find_elements_by_xpath(self,'//*[@id="index-kw"]')
        # bdtext = Common.find_element_by_id(self,"index-kw")
        bdtext.send_keys('test')
        time.sleep(3)
        Common.find_elements_by_xpath(self,'//*[@id="index-bn"]').click()
        # Common.find_element_by_id(self,"index-bn").click()

        time.sleep(10)
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print "teardown"