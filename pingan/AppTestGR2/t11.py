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
    def test012(self):
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

    #习题2：在管理中的安装包管理中删除一个安装包，并且校验是否已成功删除（挑战：删除所有）
    def test_simple3(self):
        time.sleep(3)
        el1 = self.driver.find_element_by_xpath(u'//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@text="管理"]')
        el1.click()
        time.sleep(1)
        el2 = self.driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[@index=1]')
        el2.click()
        time.sleep(2)
        el3 = self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[@index=2]')
        el3.click()
        time.sleep(3)

        el4 = self.driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.Button[@index=1]')
        txt1 = el4.text
        el4.click()
        time.sleep(10)
        #for el in els:

        #el5 = xxx
        #txt2 = el5.text
        #assert txt1!= txt2

    #习题3：在排行中，校验口碑最佳的5个APP是否和预期一致。
    def test011(self):
        #获取机型
        #判断机型，调用swipe接口
        #获取对应的控件，操作
        time.sleep(3)
        el1 = self.driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.TextView[@index=2]')
        el1.click()
        time.sleep(1)
        #swipe(sx,sy,ex,ey,dur)
        self.driver.swipe(100,1752,100,216,2000)
        time.sleep(2)
        self.driver.swipe(100,1552,100,310,2000)
        time.sleep(10)
        # els = self.driver.find_elements_by_id('com.huawei.appmarket:id/ItemTitle')
        els = self.driver.find_elements_by_xpath('//android.widget.LinearLayout/android.widget.RelativeLayout[@index=0]/android.widget.RelativeLayout[@index=2]/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=0]')
        textList = []
        for el in els:
            print el.text
            textList.append(el.text)
        print textList
        for i in textList:
            print i
        self.assertTrue(textList[3]==u'即刻')
        self.assertTrue(textList[1] == u'铁友火车票12306抢票')
        self.assertTrue(textList[2] == u'YY')
        self.assertTrue(textList[0] == u'有道翻译官')
        self.assertTrue(textList[4] == u'车轮驾考通')
        time.sleep(5)


    #习题4：查找如下的APP：光荣之路，校验前10个APP是否有名称是光荣之路的，如果没有，则断言失败
    def test041(self):
        try:
            time.sleep(5)
            el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
            el1.click()

            time.sleep(1)

            el2 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
            el2.clear()
            el2.send_keys(u'光荣之路')
            time.sleep(7)
            el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
            el3.click()
            time.sleep(3)
            # els = self.driver.find_elements_by_xpath('')
            els = self.driver.find_elements_by_id('com.huawei.appmarket:id/ItemTitle')
            textList = []
            for el in els:
                print el.text
                textList.append(el.text)
            self.driver.swipe(100, 1500, 100, 400,2000)
            time.sleep(5)
            els2 = self.driver.find_elements_by_id('com.huawei.appmarket:id/ItemTitle')
            for el in els2:
                print el.text
                textList.append(el.text)
            print textList
            self.assertTrue(u'光荣之路' in textList)
        except Exception as err:
            print err.message


    def test051(self):
        try:
            raise ValueError('fdsf')
        except Exception as e:
            print e.message
            self.driver

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    ts = unittest.TestSuite()
    testLoader = unittest.defaultTestLoader
    t1 = testLoader.loadTestsFromName('t1.APPCenter.test041')
    ts.addTest(t1)
    unittest.TextTestRunner(verbosity=2).run(ts)





