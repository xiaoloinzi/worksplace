# coding=utf-8
import time,os
import unittest

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
            time.sleep(3)
            # el1 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的"]')
            el1 = find_element(self.driver,u'//android.widget.TextView[@text="我的"]')
            el1.click()

            time.sleep(1)

            el2 = self.driver.find_element_by_xpath('//android.widget.GridView/android.widget.RelativeLayout[@index=3]')
            time.sleep(1)
            el2.click()

            el3 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="hiapps"]')
            self.assertTrue(el3.text == u'hiapps')
            #QQ 4008308300
            el4 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="QQ 4008308300"]')
            self.assertTrue(el4.text == u'QQ 4008308300')
            # self.assertTrue(1==2)
        except Exception as err:
            print 'exception:'+err.message
            path = os.getcwd()+'/tests/results/images/'
            fileName = path +self._testMethodName+time.strftime('_%Y%m%d%H%M%S')+'.png'
            self.driver.get_screenshot_as_file(fileName)
            self.assertFalse(True,'Run '+self._testMethodName+' failed')

    #设置中，打开消息提醒，并校验
    def test_wode02(self):
        try:
            time.sleep(3)
            el1 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的"]')
            el1.click()

            time.sleep(1)
            el2 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="设置"]')
            el2.click()

            time.sleep(1)
            el3 = self.driver.find_element_by_xpath('//android.widget.RelativeLayout[@index=9]/android.widget.Switch')
            if el3.get_attribute('checked') != u'true':
                el3.click()
                time.sleep(1)
            self.assertTrue(el3.get_attribute('checked') == u'true')
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




