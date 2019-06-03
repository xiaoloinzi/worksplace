# coding=utf-8
import time,os
import unittest
from keywords.appmarket.HiApp import HiApp

from common import util
from appium import webdriver
from lib.appopera import find_element

# define APPCenter test class
class APPCenter(unittest.TestCase):
    # define setup method
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            #此处填写机器的android版本
            'platformVersion': '7.0',
            #填写adb devices -l 中显示的第一列的设备号
            'deviceName': 'QVM0215B25001650',
            'appPackage': 'com.huawei.appmarket',
            'appActivity': '.MainActivity',
            'appWaitActivity': '.MarketActivity',
            'noReset':True,
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []

    #点击我的，校验微信公众号和客服
    def test_wode01(self):
        try:
            testData = util.getTestDataInput('Wode',self._testMethodName)
            hiapp = HiApp(self.driver)
            hiapp.enter_wode()
            hiapp.check_msg(**testData)

        except Exception as err:
            print 'exception:'+err.message
            path = os.getcwd()+'/tests/results/images/'
            fileName = path +self._testMethodName+time.strftime('_%Y%m%d%H%M%S')+'.png'
            self.driver.get_screenshot_as_file(fileName)
            self.assertFalse(True,'Run '+self._testMethodName+' failed')

    #设置中，打开消息提醒，并校验
    def test_wode02(self):
        try:
            hiapp = HiApp(self.driver)
            hiapp.enter_wode()
            hiapp.open_switch(u'//android.widget.RelativeLayout[@index=9]/android.widget.Switch')
        except Exception as err:
            print 'exception:'+err.message
            path = os.getcwd()+'/tests/results/images/'
            fileName = path +self._testMethodName+time.strftime('_%Y%m%d%H%M%S')+'.png'
            self.driver.get_screenshot_as_file(fileName)
            self.assertFalse(True,'Run '+self._testMethodName+' failed')

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    ts = unittest.TestSuite()
    testLoader = unittest.defaultTestLoader
    t1 = testLoader.loadTestsFromName('Wode.APPCenter.test_wode01')
    ts.addTest(t1)
    unittest.TextTestRunner(verbosity=3).run(ts)




