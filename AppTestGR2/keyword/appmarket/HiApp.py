# encoding=utf-8
import time
from AppTestGR2.lib import find_element
class HiApp(object):
    def __init__(self,driver):
        self.driver = driver

    def remover_app(self,**kwargs):
#         卸载APP，并校验卸载成功
        if self.driver.is_app_installed(kwargs["remover_app.appPkgName"]):
            self.driver.remove_app(kwargs["remover_app.appPkgName"])
        return True

    def download_app(self,**kwargs):
        # 下载app
        e11 = find_element.find_element(self.driver,'com.huawei.appmarket:id/search_edit_text')
        e11.click()
        e12 = find_element.find_element(self.driver,'com.huawei.appmarket:id/searchText')
        e12.set_value(kwargs["download_app.appName"])
        e13 = find_element.find_element(self.driver,'com.huawei.appmarket:id/search_title_icon')
        e13.click()
        e14 = find_element.find_element(self.driver,'//android.widget.LinearLayout[@index=0]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.View[@index=1]')
        e14.click()

    def app_is_exist(self,**kwargs):
#         循环校验，每两秒一次，存在则退出，循环结束，还不存在，则断言失败（10）
        for i in xrange(10):
            if self.driver.is_app_installed(kwargs["app_is_exist.appName"]):
                return True
            time.sleep(2)
        assert True == self.driver.is_app_installed(kwargs["app_is_exist.appName"])


    def download_app_notexist(self,**kwargs):
        # 下载不存在的app
        e11 = find_element.find_element(self.driver,'com.huawei.appmarket:id/search_edit_text')
        e11.click()
        e12 = find_element.find_element(self.driver,'com.huawei.appmarket:id/searchText')
        e12.set_text(kwargs["download_app_notexist"])
        e13 = find_element.find_element(self.driver,'com.huawei.appmarket:id/search_title_icon')
        e13.click()
        el4 = find_element.find_element(self.driver,u'//android.widget.TextView[@text="没有符合条件的内容"]')
        assert el4.text == u'没有符合条件的内容'

    def enter_wode(self):
        # 使用封装的find_element
        # 1、进入我的
        e11 = find_element.find_element(self.driver,u'//android.widget.TextView[@text="我的"]')
        e11.click()


    def check_msg(self,**kwargs):
        # 校验信息（校验微信公众号和客服）
        # 把xpath和text做成一个列表的形式来检验两个参数，判断列表的长度要做好列表只有一个参数的情况
        find_element.find_element(self.driver,'//android.widget.TextView[@text="关于"]').click()
        e13 = find_element.find_element(self.driver,kwargs["check_msg.xpath"])
        assert e13.text == kwargs["check_msg.text"]

    def open_switch(self,**kwargs):
        find_element.find_element(self.driver,'//android.widget.TextView[@text="设置"]').click()
        el3 = find_element.find_element(self.driver,kwargs["open_switch.xpath"])
        if el3.get_attribute('checked') != u'true':
            el3.click()
        assert el3.get_attribute('checked') == u'true'
















