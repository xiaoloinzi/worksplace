# encoding=utf-8

import time
from lib.appopera import find_element

class HiApp(object):
    def __init__(self,driver):
        self.driver = driver

    def remover_app(self,appPkgName):
        #卸载APP，并校验卸载成功
        self.driver.remove_app(appPkgName)
        time.sleep(2)
        assert self.driver.is_app_installed(appPkgName) == False

    def download_app(self,appName):
        #下载APP
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
        pass

    def app_is_exist(self,appPkgName):
        #循环校验，没两秒一次，存在则退出，循环结束，还不存在，则断言失败.(10)
        pass

    def download_app_notexist(self,appName):
        #下载不存的app
        pass

    def enter_wode(self):
        #使用封装的find_element
        pass

    def check_msg(self,xpath,checkedText):
        #参考wode01
        pass

    def open_switch(self,xpath):
        #参考wode02
        pass













