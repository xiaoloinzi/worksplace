# coding=utf-8
import time
import unittest

from appium import webdriver

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

    def test_simple3(self):
        time.sleep(3)
        el1 = self.driver.find_element_by_xpath(u'//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@text="管理"]')
        el1.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_activity,'.MarketActivity')

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    # ts = unittest.TestSuite()
    # testLoader = unittest.defaultTestLoader
    # t1 = testLoader.loadTestsFromName('t1.APPCenter.test041')
    # ts.addTest(t1)
    # unittest.TextTestRunner(verbosity=2).run(ts)





