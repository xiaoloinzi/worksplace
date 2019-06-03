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

    #习题1：在首页中下载music 这个app，之后校验这个app是否已下载
    # def test_download_music(self):
    #     time.sleep(5)
    #     el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
    #     el1.click()
    #
    #     time.sleep(1)
    #
    #     el2 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
    #     el2.set_value('music')
    #     time.sleep(2)
    #     el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
    #     el3.click()
    #     time.sleep(1)
    #     el4 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=0]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.View[@index=1]')
    #     el4.click()
    #
    #     time.sleep(10)
    #     # self.driver.is_app_installed('com.ezhoop.music')
    #     print self.driver.is_app_installed('com.ezhoop.music')
    #
    #     self.driver.remove_app('com.ezhoop.music')
    #
    #     print self.driver.is_app_installed('com.ezhoop.music')
    #
    #     time.sleep(1)

    #下载不存在的APP，名字是“#()*”，需要断言
    # def test_download_notexist1(self):
    #     time.sleep(5)
    #     el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
    #     el1.click()
    #
    #     time.sleep(1)
    #
    #     el2 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
    #     el2.clear()
    #     el2.set_text('#()*')
    #     time.sleep(2)
    #     el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
    #     el3.click()
    #     time.sleep(1)
    #     el4 = self.driver.find_elements_by_xpath('//android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView')
    #     for i in el4:
    #         print i.text
    #         self.assertTrue(i.text!='#()*')

    #下载不存在的APP，名字是“sfskdjfksdjfksjdkfjsdk2334kkdsfjhsjdhfjh3344”，需要断言
    def test_download_notexist2(self):
        time.sleep(5)
        el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
        el1.click()

        time.sleep(1)

        el2 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
        el2.clear()
        el2.set_text('sfskdjfksdjfksjdkfjsdk2334kkdsfjhsjdhfjh3344')
        time.sleep(2)
        el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
        el3.click()
        time.sleep(1)
        el4 = self.driver.find_elements_by_xpath('//android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView')
        for i in el4:
            print i.text
            self.assertTrue(i.text!='sfskdjfksdjfksjdkfjsdk2334kkdsfjhsjdhfjh3344')


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








