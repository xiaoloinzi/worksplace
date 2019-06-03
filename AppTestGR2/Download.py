# coding=utf-8
import time
import unittest
from lib import find_element

from appium import webdriver
from AppTestGR2.keyword.appmarket.HiApp import HiApp
from common import util
from common import util

# define APPCenter test class
class APPCenter(unittest.TestCase):
    # define setup method
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            #此处填写机器的android版本
            'platformVersion': '4.4.4',
            #填写adb devices -l 中显示的第一列的设备号
            'deviceName': '192.168.146.101:5555',
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
            # 数据驱动实现
            print self._testMethodName
            testdata = util.getTestDataInput("Download",self._testMethodName)
            print testdata["remover_app.appPkgName"]
            hiapp = HiApp(self.driver)
            hiapp.remover_app(**testdata)
            hiapp.download_app(**testdata)
            hiapp.app_is_exist(**testdata)
            # hiapp = HiApp(self.driver)
            # hiapp.remover_app(u'com.ezhoop.music')
            # hiapp.download_app(u'music')
            # hiapp.app_is_exist(u'com.ezhoop.music')
            # time.sleep(5)
            # el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
            # el1.click()
            #
            # time.sleep(1)
            #
            # el2 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
            # el2.set_value('music')
            # time.sleep(2)
            # el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
            # el3.click()
            # time.sleep(1)
            # el4 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=0]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.View[@index=1]')
            # el4.click()
            #
            # time.sleep(10)
            # # self.driver.is_app_installed('com.ezhoop.music')
            # print self.driver.is_app_installed('com.ezhoop.music')
            #
            # self.driver.remove_app('com.ezhoop.music')
            #
            # print self.driver.is_app_installed('com.ezhoop.music')
            #
            # time.sleep(1)
        except:
            time.sleep(3)
            path = 'E:\\worksplace\\AppTestGR2\\tests\\results\images\\'
            fileName = path+self._testMethodName+time.strftime('_%Y%m%d%H%M%S')+".png"
            self.driver.get_screenshot_as_file(fileName)
            self.assertFalse(True,'Run'+self._testMethodName+'failed')
            time.sleep(3)


    #下载不存在的APP，名字是“#()*”，需要断言
    def test_download_notexist1(self):
        try:
            logs = util.createMainLog('E:\\worksplace\\AppTestGR2\\tests\\results\\')
            logs.debug("test_download_notexist1----kaishi zgxing")
            print self._testMethodName
            testdata = util.getTestDataInput("Download",self._testMethodName)
            print testdata["remover_app.appPkgName"]
            hiapp = HiApp(self.driver)
            hiapp.download_app_notexist(**testdata)
            # hiapp = HiApp(self.driver)
            # hiapp.download_app_notexist(u'#()*')
            # time.sleep(5)
            # el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
            # el1.click()
            #
            # time.sleep(1)
            #
            # el2 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
            # el2.clear()
            # # el2.set_value(r'#()*')
            # el2.set_text(u'#()*')
            # time.sleep(2)
            # el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
            # el3.click()
            # time.sleep(1)

            # el4 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="没有符合条件的内容"]')
            # self.assertTrue(el4.text == u'没有符合条件的内容')
        except:
            logs.debug("test_download_notexist1----kaishi zgxing")
            time.sleep(3)
            path = 'E:\\worksplace\\AppTestGR2\\tests\\results\images\\'
            fileName = path+self._testMethodName+time.strftime('_%Y%m%d%H%M%S')+".png"
            self.driver.get_screenshot_as_file(fileName)
            self.assertFalse(True,'Run'+self._testMethodName+'failed')
            time.sleep(3)

    #下载不存在的APP，名字是“sfskdjfksdjfksjdkfjsdk2334kkdsfjhsjdhfjh3344”，需要断言
    # def test_download_notexist2(self):
    #     try:
    #         time.sleep(5)
    #         el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
    #         el1.click()
    #
    #         time.sleep(1)
    #
    #         el2 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
    #         el2.clear()
    #         el2.set_text('sfskdjfksdjfksjdkfjsdk2334kkdsfjhsjdhfjh3344')
    #         time.sleep(2)
    #         el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
    #         el3.click()
    #         time.sleep(1)
    #
    #         el4 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="没有符合条件的内容"]')
    #         self.assertTrue(el4.text == u'没有符合条件的内容')
    #     except:
    #         time.sleep(3)
    #         path = 'E:\\worksplace\\AppTestGR2\\tests\\results\images\\'
    #         fileName = path+self._testMethodName+time.strftime('_%Y%m%d%H%M%S')+".png"
    #         self.driver.get_screenshot_as_file(fileName)
    #         self.assertFalse(True,'Run'+self._testMethodName+'failed')
    #         time.sleep(3)
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








