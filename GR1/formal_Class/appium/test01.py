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

    # def test_simple(self):
    #     el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/tab_name')
    #     el1.click()
    #     time.sleep(5)
    #     print 'abc'
# 习题：通过xpath定位到“我的”，并且点击我的，之后在我的里面定位控件“设置”
#     def test01(self):
#         print 'abc'
#         time.sleep(3)
#         # e11 = self.driver.find_element_by_id('com.huawei.appmarket:id/tab_name')
#         e11 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="我的"]')
#         print e11.text
#         e11.click()
#
#         e12 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="设置"]')
#         print e12.text
#         e12.click()
# 习题5：在我的中查看关于，并且校验微信公众号是否是hiapps，之后截图

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

    #     老师的方法：
    # def test015(self):
    #     time.sleep(3)
    #     el1 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的"]')
    #     el1.click()
    #
    #     time.sleep(1)
    #
    #     el2 = self.driver.find_element_by_xpath('//android.widget.GridView/android.widget.RelativeLayout[@index=3]')
    #     time.sleep(1)
    #     el2.click()
    #
    #     el3 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="hiapps"]')
    #     self.assertTrue(el3.text == 'hiapps')
    #
    #     time.sleep(3)
    #     fileName = 'e:\\tmp\\t05.png'
    #     self.driver.get_screenshot_as_file(fileName)
    #     time.sleep(3)

    # 值的输入
    # def test012(self):
    #     time.sleep(3)
    #     el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
    #     el1.click()
    #
    #     time.sleep(1)
    #     e12 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
    #     # 使用set_value进行值的传输
    #     e12.set_value('muisc')
    #
    #     time.sleep(1)
    #     el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
    #     el3.click()
    #     time.sleep(3)
    #     finname = 'D:\\tmp\\01.png'
    #     # 截图
    #     self.driver.get_screenshot_as_file(finname)



# 习题4：在我的中，进入设置，关闭消息提示，并且校验
#     def test01(self):
#         print 'abc'
#         time.sleep(3)
#         e11 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="我的"]')
#         print e11.text
#         e11.click()
#
#         e12 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="设置"]')
#         e12.click()
#         print e12.text
#         e13 = self.driver.find_element_by_xpath(u'//android.widget.RelativeLayout[@index=8]/android.widget.Switch')
#         print e13.get_attribute("checked")
#         e13.click()
#         print e13.get_attribute("checked")
#         print e13.text



 # 习题1：在排行中找到排行前5的APP，并且校验和预期的是否一致
 #    def test01(self):
 #        print 'abc'
 #        time.sleep(3)
 #        e11 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="排行"]')
 #        print e11.text
 #        e11.click()
 #        self.driver.swipe(100,575,100,175)
 #        time.sleep(3)
 #        e12 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[@index=0]')
 #        print e12.text
 #        self.assertEqual(e12.text,u"优酷")
 #
 #        e13 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[@index=0]')
 #        self.assertEqual(e13.text,u"快手")
 #        print e13.text
 #        e14 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=3]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[@index=0]')
 #        self.assertEqual(e14.text,u"手机百度")
 #        print e14.text
 #        e15 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=4]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[@index=0]')
 #        self.assertEqual(e15.text,u"手机淘宝")
 #        print e15.text
 #        e16 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=5]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[@index=0]')
 #        self.assertEqual(e16.text,u"美团")
 #        print e16.text
    #
    # 老师的方法：
    # def test01(self):
    #     #获取机型
    #     #判断机型，调用swipe接口
    #     #获取对应的控件，操作
    #     time.sleep(3)
    #     el1 = self.driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.TextView[@index=2]')
    #     el1.click()
    #     time.sleep(1)
    #
    #     # el2 = self.driver.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[@index=0]')
    #     # print el2.text
    #     els = self.driver.find_elements_by_xpath('//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=0]')
    #     for el in els:
    #         print el.text
    #     els[-1]
    #     self.assertTrue(els[0].text==u'优酷')
    #     self.assertTrue(els[1].text==u'快手')
    #     self.assertTrue(els[2].text==u'手机百度')
    #     self.assertTrue(els[3].text==u'手机淘宝')
    #     self.assertTrue(els[4].text==u'美团')
    #
    #     self.driver.swipe(100,675,100,175)
    #     time.sleep(5)
    #
    #     e16 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=8]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[@index=0]')
    #     self.assertEqual(e16.text,u"美团")
    #     print e16.text

        # e12 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="设置"]')
        # print e12.text
        # e12.click()


    # def test01(self):
    #     print 'abc'
    #     time.sleep(3)
    #     # e11 = self.driver.find_element_by_id('com.huawei.appmarket:id/tab_name')
    #     e11 = self.driver.find_element_by_xpath(u'//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@text="管理"]')
    #     e11.click()
    #     time.sleep(3)
    # def test01(self):
    #     print 'abc'
    #     time.sleep(5)
    #     # e11 = self.driver.find_element_by_id('com.huawei.appmarket:id/tab_name')
    #     e11 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="管理"]')
    #     e11.click()
    #     time.sleep(3)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
