# coding=utf-8
import time,os
import unittest,logging
from keywords.appmarket.HiApp import HiApp

from common import util

from appium import webdriver

logger = logging.getLogger('Download')
logger.setLevel(logging.DEBUG)

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
            hiapp = HiApp(self.driver)
            testData = util.getTestDataInput('Download',self._testMethodName)
            hiapp.remover_app(**testData)
            hiapp.download_app(**testData)
            hiapp.app_is_exist(**testData)
        except Exception as err:
            print 'exception:'+err.message
            path = os.getcwd()+'/tests/results/images/'
            fileName = path +self._testMethodName+time.strftime('_%Y%m%d%H%M%S')+'.png'
            self.driver.get_screenshot_as_file(fileName)
            self.assertFalse(True,'Run '+self._testMethodName+' failed')

    #下载不存在的APP，名字是“#()*”，需要断言
    def test_download_notexist1(self):
        try:
            hiapp = HiApp(self.driver)
            testData = util.getTestDataInput('Download',self._testMethodName)
            hiapp.download_app_notexist(**testData)
        except Exception as err:
            print 'exception:'+err.message
            path = os.getcwd()+'/tests/results/images/'
            fileName = path +self._testMethodName+time.strftime('_%Y%m%d%H%M%S')+'.png'
            self.driver.get_screenshot_as_file(fileName)
            self.assertFalse(True,'Run '+self._testMethodName+' failed')

    #下载不存在的APP，名字是“sfskdjfksdjfksjdkfjsdk2334kkdsfjhsjdhfjh3344”，需要断言
    def test_download_notexist2(self):
        try:
            logger.info('begin to run testcase test_download_notexist2')
            hiapp = HiApp(self.driver)
            testData = util.getTestDataInput('Download',self._testMethodName)
            hiapp.download_app_notexist(**testData)
        except Exception as err:
            print 'exception:'+err.message
            logger.error('run testcase test_download_notexist2 failed')
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
    t1 = testLoader.loadTestsFromName('Download.APPCenter.test_download_music')
    t2 = testLoader.loadTestsFromName('Download.APPCenter.test_download_notexist2')
    # ts.addTest(t1)
    ts.addTest(t2)
    unittest.TextTestRunner(verbosity=2).run(ts)








