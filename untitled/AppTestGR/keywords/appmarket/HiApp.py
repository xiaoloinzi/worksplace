# encoding=utf-8

import time
from lib.appopera import find_element

class HiApp(object):
    def __init__(self,driver):
        self.driver = driver

    def remover_app(self,**kwargs):
        #卸载APP，并校验卸载成功
        assert 'remover_app.appPkgName' in kwargs.keys()
        self.driver.remove_app(kwargs['remover_app.appPkgName'])
        time.sleep(2)
        assert self.driver.is_app_installed(kwargs['remover_app.appPkgName']) == False

    def download_app(self,**kwargs):
        #下载APP
        assert 'download_app.appName' in kwargs.keys()
        time.sleep(5)
        el1 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_edit_text')
        el1.click()

        time.sleep(1)

        el2 = self.driver.find_element_by_id('com.huawei.appmarket:id/searchText')
        el2.set_value(kwargs['download_app.appName'])
        time.sleep(2)
        el3 = self.driver.find_element_by_id('com.huawei.appmarket:id/search_title_icon')
        el3.click()
        time.sleep(1)
        el4 = self.driver.find_element_by_xpath('//android.widget.LinearLayout[@index=0]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.View[@index=1]')
        el4.click()

        time.sleep(10)

    def app_is_exist(self,**kwargs):
        #循环校验，没两秒一次，存在则退出，循环结束，还不存在，则断言失败.(10)
        assert 'app_is_exist.appPkgName' in kwargs.keys()
        for i in xrange(10):
            time.sleep(2)
            isInstalled = self.driver.is_app_installed(kwargs['app_is_exist.appPkgName'])
            if isInstalled is True:
                break
            if i == 9:
                assert False

    def download_app_notexist(self,**kwargs):
        #下载不存的app
        assert 'download_app_notexist.appName' in kwargs.keys()
        time.sleep(5)
        el1 = find_element(self.driver,'com.huawei.appmarket:id/search_edit_text')
        el1.click()

        time.sleep(1)

        el2 = find_element(self.driver,'com.huawei.appmarket:id/searchText')
        el2.clear()
        # el2.set_value(r'#()*')
        el2.set_text(unicode(kwargs['download_app_notexist.appName']))
        time.sleep(2)
        el3 = find_element(self.driver,'com.huawei.appmarket:id/search_title_icon')
        el3.click()
        time.sleep(1)

        el4 = find_element(self.driver,u'//android.widget.TextView[@text="没有符合条件的内容"]')
        assert el4.text == u'没有符合条件的内容'

    def enter_wode(self):
        #使用封装的find_element
        time.sleep(3)
        # el1 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的"]')
        el1 = find_element(self.driver,u'//android.widget.TextView[@text="我的"]')
        el1.click()
        time.sleep(1)

    def check_msg(self,**kwargs):
        #参考wode01
        assert 'check_msg.xpathList' in kwargs.keys()
        assert 'check_msg.checkedTextList' in kwargs.keys()
        print 'assert succ'
        time.sleep(2)
        el2 = self.driver.find_element_by_xpath('//android.widget.GridView/android.widget.RelativeLayout[@index=3]')
        el2.click()

        time.sleep(1)
        for i in xrange(len(kwargs['check_msg.xpathList'])):
            el3 = self.driver.find_element_by_xpath(kwargs['check_msg.xpathList'][i])
            assert el3.text == kwargs['check_msg.checkedTextList'][i]

    def open_switch(self,**kwargs):
        #参考wode02
        assert 'open_switch.xpath' in kwargs.keys()
        time.sleep(1)
        el2 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="设置"]')
        el2.click()

        time.sleep(1)
        el3 = self.driver.find_element_by_xpath(kwargs['open_switch.xpath'])
        if el3.get_attribute('checked') != u'true':
            el3.click()
            time.sleep(1)
        assert el3.get_attribute('checked') == u'true'














