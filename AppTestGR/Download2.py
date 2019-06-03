# coding=utf-8
import time,os
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
    def test_download_music(self):
        try:
            time.sleep(5)
            el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
            el1.click()

            time.sleep(1)

            el2 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
            el2.set_value('music')
            time.sleep(2)
            el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
            el3.click()
            time.sleep(1)
            el4 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=0]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.View[@index=1]')
            el4.click()

            time.sleep(10)
            # self.driver.is_app_installed('com.ezhoop.music')
            print self.driver.is_app_installed('com.ezhoop.music')

            self.driver.remove_app('com.ezhoop.music')
            print self.driver.is_app_installed('com.ezhoop.music')

            time.sleep(1)
        except Exception as err:
            print 'exception:'+err.message
            path = os.getcwd()+'/tests/results/images/'
            fileName = path +self._testMethodName+time.strftime('_%Y%m%d%H%M%S')+'.png'
            self.driver.get_screenshot_as_file(fileName)
            self.assertFalse(True,'Run '+self._testMethodName+' failed')


    #下载不存在的APP，名字是“#()*”，需要断言
    def test_download_notexist1(self):
        try:
            time.sleep(5)
            el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
            el1.click()

            time.sleep(1)

            el2 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
            el2.clear()
            # el2.set_value(r'#()*')
            el2.set_text(u'#()*')
            time.sleep(2)
            el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
            el3.click()
            time.sleep(1)

            el4 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="没有符合条件的内容"]')
            self.assertTrue(el4.text == u'没有符合条件的内容')
        except Exception as err:
            print 'exception:'+err.message
            path = os.getcwd()+'/tests/results/images/'
            fileName = path +self._testMethodName+time.strftime('_%Y%m%d%H%M%S')+'.png'
            self.driver.get_screenshot_as_file(fileName)
            self.assertFalse(True,'Run '+self._testMethodName+' failed')

    #下载不存在的APP，名字是“sfskdjfksdjfksjdkfjsdk2334kkdsfjhsjdhfjh3344”，需要断言
    def test_download_notexist2(self):
        try:
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

            el4 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="没有符合条件的内容"]')
            self.assertTrue(el4.text == u'没有符合条件的内容')
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
    t1 = testLoader.loadTestsFromName('Download.APPCenter.test_download_notexist1')
    t2 = testLoader.loadTestsFromName('Download.APPCenter.test_download_notexist2')
    ts.addTest(t1)
    # ts.addTest(t2)
    unittest.TextTestRunner(verbosity=2).run(ts)








