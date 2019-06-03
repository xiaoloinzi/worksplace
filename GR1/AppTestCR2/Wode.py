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

    #点击我的，校验微信公众号和客服
    def test_wode01(self):
        time.sleep(3)
        el1 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="我的"]')
        el1.click()

        self.driver.swipe(500,2400,500,2000,200)
        time.sleep(4)
        e12 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="关于"]')
        e12.click()

        el3 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=4]/android.widget.RelativeLayout/android.widget.TextView[@index=1]')
        self.assertEqual(el3.text,"hiapps")
        print el3.text
        el4 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=6]/android.widget.RelativeLayout/android.widget.TextView[@index=1]')
        self.assertEqual(el3.text,"QQ 4008308300")
        print el4.text

        # finname = 'D:\\tmp\\04.png'
        # # 截图
        # self.driver.get_screenshot_as_file(finname)

    #设置中，打开消息提醒，并校验
    def test_wode02(self):
        pass


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    ts = unittest.TestSuite()
    testLoader = unittest.defaultTestLoader
    t1 = testLoader.loadTestsFromName('t1.APPCenter.test041')
    ts.addTest(t1)
    unittest.TextTestRunner(verbosity=2).run(ts)











