# encoding=utf-8
import time
import unittest

from appium import webdriver
# APP自动化测试框架课后作业
# 习题1：在首页中下载music 这个app，之后校验这个app是否已下载
#
# 习题2：在管理中的安装包管理中删除一个安装包，并且校验是否已成功删除（挑战：删除所有）
#
# 习题3：在排行中，校验口碑最佳的5个APP是否和预期一致。
#
# 习题4：查找如下的APP：光荣之路，校验前10个APP是否有名称是光荣之路的，如果没有，则断言失败
# define APPCenter test0827 class
class APPCenter(unittest.TestCase):
    # define setup method
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            #此处填写机器的android版本
            'platformVersion': '7.0',
            # 'platformVersion': '4.4.4',
            #填写adb devices -l 中显示的第一列的设备号
            # 'deviceName': '192.168.43.101:5555',
            'deviceName': 'TWGDU16905000717',
            'appPackage': 'com.huawei.appmarket',
            'appActivity': '.MainActivity',
            'appWaitActivity': '.MarketActivity',
            'noReset':True,
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []


    def test04(self):
        list1 = []
        time.sleep(3)
        el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
        el1.click()
        time.sleep(1)
        e12 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
        e12.set_text(u"光荣之路")
        time.sleep(2)
        el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
        el3.click()
        time.sleep(3)
        e14 = self.driver.find_elements_by_xpath('//android.widget.ListView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index =0]')
        for i in e14:
            print i.text
            list1.append(i.text)
        self.driver.swipe(1430,1204,1430,220)
        e15 = self.driver.find_elements_by_xpath('//android.widget.ListView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index =0]')
        for i in e15:
            print i.text
            list1.append(i.text)
        self.assertTrue(u'光荣之路' in list1)
        time.sleep(2)

    def test02(self):
        time.sleep(2)
        e10 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="管理"]')
        e10.click()
        e11 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="安装包管理"]')
        e11.click()

        e12 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="微信"]')
        if e12.text == u"微信":
            e13 = e11 = self.driver.find_element_by_xpath(u'//android.widget.Button[@text="删除"]')
            e13.click()
            e14 = e11 = self.driver.find_element_by_xpath(u'//android.widget.Button[@text="删除"]')
            e14.click()
        e = self.driver.find_elements_by_xpath(u'//android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@index=0]')
        for i in e:
            print i.text
            self.assertTrue(i.text != u"微信")
        # e15 = e11 = self.driver.find_element_by_xpath(u'//android.widget.Button[@text="全部删除"]')
        # e15.click()
        # e16 = e11 = self.driver.find_element_by_xpath(u'//android.widget.Button[@text="确定"]')
        # e16.click()


    def test01(self):
        time.sleep(1)
        el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
        el1.click()
        time.sleep(1)
        e12 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
        # 使用set_value进行值的传输
        e12.set_value('music')
        time.sleep(2)
        el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
        el3.click()
        time.sleep(5)
        el4 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="Music"]')
        el4.click()
        time.sleep(1)
        el5 = self.driver.find_element_by_id('com.huawei.appmarket:id/detail_download_button')
        el5.click()
        time.sleep(30)
        e16 = self.driver.find_element_by_xpath(u'//android.widget.Button[@text="下一步"]')
        e16.click()
        e17 = self.driver.find_element_by_xpath(u'//android.widget.Button[@text="安装"]')
        e17.click()
        time.sleep(6)
        el8 = self.driver.find_element_by_id('com.huawei.appmarket:id/detail_download_button')
        el8.click()
        el9 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="我的音乐"]')
        self.assertEqual(el9.text,u"我的音乐")



    def test03(self):
        time.sleep(1)
        el1 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="排行"]')
        el1.click()
        time.sleep(3)
        self.driver.swipe(100,251,100,90,duration=10)
        list1 = [u'即刻',u'铁友火车票12306抢票',u'YY',u'有道翻译官',u'车轮驾考通']
        for i in xrange(1,6):
            time.sleep(2)
            el2 = self.driver.find_element_by_xpath(u'//android.widget.LinearLayout[@index=%d]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[@index=0]'%i)
            self.assertEqual(el2.text,list1[i-1])
            print el2.text

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
