# coding=utf-8
import time
import unittest

from appium import webdriver

# define APPCenter test0827 class
class APPCenter(unittest.TestCase):
    # define setup method
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            #此处填写机器的android版本
            'platformVersion': '4.4.4',
            #填写adb devices -l 中显示的第一列的设备号
            'deviceName': '192.168.43.101:5555',
            'appPackage': 'com.huawei.appmarket',
            'appActivity': '.MainActivity',
            'appWaitActivity': '.MarketActivity',
            'noReset':True,
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []

    def test012(self):
        time.sleep(3)
        el1 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的"]')
        el1.click()


        e12 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="关于"]')
        e12.click()

        el3 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=4]/android.widget.RelativeLayout/android.widget.TextView[@index=1]')
        self.assertEqual(el3.text,"hiapps")
        print el3.text
        finname = 'D:\\tmp\\03.png'
        # 截图
        self.driver.get_screenshot_as_file(finname)


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
