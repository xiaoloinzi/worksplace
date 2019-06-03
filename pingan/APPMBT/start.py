# encoding=utf-8

import unittest,time
from appium import webdriver
from core import util
from graph import Graph as gra

class APPMBT(unittest.TestCase):
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
        util.initGraph()

    # def test_randomPath(self):
    #     try:
    #         print 3
    #         util.randomPathWalk(self)
    #     except Exception as err:
    #         print err.message
    #         self.assertTrue(False)

    def test_specifiedPath(self):
        try:
            print 3
            util.spefiedPathWalk(self)
            time.sleep(5)
        except Exception as err:
            print err.message
            self.assertTrue(False)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



# util.initGraph()
# gra.printGraph()
# gra.genAllShortestPath()
# print gra.randomPath()


