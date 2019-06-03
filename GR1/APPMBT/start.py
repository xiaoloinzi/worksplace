# encoding=utf-8

from GR1.APPMBT.core import util
from graph import Graph as gra
from appium import webdriver
import unittest

class APPMBT(unittest.TestCase):
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
        util.initGraph()
    # def test_randomPath(self):
    #     try:
    #         # util.randomPathWalk(self)
    #     except Exception as err:
    #         print err.message
    #         self.assertTrue(False)
    def test_getPath(self):
        try:
            logs = util.createMainLog('E:\\worksplace\\GR1\APPMBT\\tests\\results\\')
            logs.debug("test_getPath----start!!!!!!!")
            util.getPathWalk(self)
            print util.getTestDataraw()
        except Exception as err:
            logs = util.createMainLog('E:\\worksplace\\GR1\APPMBT\\tests\\results\\')
            logs.debug("test_getPath----error!!!!!!!")
            print err.message
            self.assertTrue(False)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()


# util.initGraph()
# gra.printGraph()
#
# gra.genAllShortPath()
# print gra.randomPath()
# print gra.getPath('Manger', 'Suggest')
#
# util.randomPathWalk("")

















