# coding=utf-8
import time
import unittest

from appium import webdriver
from lib import appopera
from GR1.AppTestGR.keywords.appmarket.HiApp import HiApp
from GR1.AppTestGR.common import util

# define APPCenter test class
class APPCenter(unittest.TestCase):
    # define setup method
    def setUp(self):
        desired_caps = {
            'platformName': util.getConfig('Basic','platformName'),
            #此处填写机器的android版本
            'platformVersion': util.getConfig('Basic','platformVersion'),
            #填写adb devices -l 中显示的第一列的设备号
            'deviceName': util.getConfig('Basic','deviceName'),
            'appPackage': util.getConfig('Basic','appPackage'),
            'appActivity': util.getConfig('Basic','appActivity'),
            'appWaitActivity': util.getConfig('Basic','appWaitActivity'),
            'noReset':True,
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []

    #点击我的，校验微信公众号和客服
    def test_wode01(self):
        try:
            logs = util.createMainLog('E:\\worksplace\\AppTestGR2\\tests\\results\\')
            logs.debug("test_wode01----kaishi zgxing")
            testdata = util.getTestDataInput("Wode",self._testMethodName)
            hiapp = HiApp(self.driver)
            hiapp.enter_wode()
            hiapp.check_msg(**testdata)
            logs = util.createMainLog('E:\\worksplace\\AppTestGR2\\tests\\results\\')

            # hiapp = HiApp(self.driver)
            # hiapp.enter_wode()
            # hiapp.check_msg('//android.widget.TextView[@text="hiapps"]','hiapps')

            # time.sleep(3)
            # el1 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的"]')
            # el1.click()
            #
            # time.sleep(1)
            #
            # e12 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="关于"]')
            # time.sleep(1)
            # e12.click()
            #
            # el3 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="hiapps"]')
            # self.assertTrue(el3.text == 'hiapps')
            # print el3.text
            # # 获取当前方法的名字
            # print self._testMethodName
            # #QQ 4008308300
            # el4 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="QQ 4008308300"]')
            # self.assertTrue(el4.text == 'QQ 40083083')
            # print el4.text

        except:
            logs.debug("test_wode01----jieshu zgxing")
            time.sleep(3)
            path = 'E:\\worksplace\\AppTestGR2\\tests\\results\images\\'
            fileName = path+self._testMethodName+time.strftime('_%Y%m%d%H%M%S')+".png"
            self.driver.get_screenshot_as_file(fileName)
            self.assertFalse(True,'Run'+self._testMethodName+'failed')
            time.sleep(3)

    #设置中，打开消息提醒，并校验
    def test_wode02(self):
        try:
            logs = util.createMainLog('E:\\worksplace\\AppTestGR2\\tests\\results\\')
            logs.debug("test_wode0----kaishi zgxing")
            testdata = util.getTestDataInput("Wode",self._testMethodName)
            hiapp = HiApp(self.driver)
            hiapp.enter_wode()
            hiapp.open_switch(**testdata)
            # keyword封装后的代码
            # hiapp = HiApp(self.driver)
            # hiapp.enter_wode()
            # hiapp.open_switch('//android.widget.RelativeLayout[@index=8]/android.widget.Switch')
            # # time.sleep(3)
            # # el1 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的"]')
            # # el1.click()
            # e11 = find_element.find_element(self.driver,'//android.widget.TextView[@text="我的"]')
            # e11.click()
            #
            # time.sleep(1)
            # el2 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="设置"]')
            # el2.click()
            #
            # time.sleep(1)
            # el3 = self.driver.find_element_by_xpath('//android.widget.RelativeLayout[@index=8]/android.widget.Switch')
            # if el3.get_attribute('checked') != u'true':
            #     el3.click()
            #     time.sleep(1)
            # self.assertTrue(el3.get_attribute('checked') == u'true')
            # print el3.text
        except:
            logs.debug("test_wode02----kaishi zgxing")
            time.sleep(3)
            path = 'E:\\worksplace\\AppTestGR2\\tests\\results\images\\'
            fileName = path+self._testMethodName+time.strftime('_%Y%m%d%H%M%S')+".png"
            self.driver.get_screenshot_as_file(fileName)
            self.assertFalse(True,'Run'+self._testMethodName+'failed')
            time.sleep(3)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    # ts = unittest.TestSuite()
    # testLoader = unittest.defaultTestLoader
    # t1 = testLoader.loadTestsFromName('Wode.APPCenter.test_wode02')
    # ts.addTest(t1)
    # unittest.TextTestRunner(verbosity=2).run(ts)











