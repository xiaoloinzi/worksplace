# encoding=utf-8
import time
from GR1.APPMBT.core import util

def homeEnterManage(self):
    time.sleep(1)
    e1 = util.find_element(self.driver,u'//android.widget.TextView[@text="管理"]')
    e1.click()

def homeEnterRank(self):
    time.sleep(1)
    e1 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="排行"]')
    e1.click()
    # el = util.find_element(self.driver,'//android.widget.RelativeLayout[@index=1]/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=2]')
    # el.click()
def homeEnterMine(self):
    time.sleep(1)
    e1 = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="我的"]')
    e1.click()


def homeEnterSuggest(self):
    time.sleep(1)
    e1 = util.find_element(self.driver,u'//android.widget.TextView[@text="推荐"]')
    e1.click()

def walk(self):
    if self.methodName == 'homeEnterManage':
        homeEnterManage(self)
        # 取得当前的Activity和另外的Activity进行判断
        self.assertEqual(self.driver.current_activity,'.MarketActivity')
    if self.methodName == 'homeEnterRank':
        homeEnterRank(self)
        # 取得当前的Activity和另外的Activity进行判断
        self.assertEqual(self.driver.current_activity,'.MarketActivity')
    if self.methodName == 'homeEnterSuggest':
        homeEnterSuggest(self)
        # 取得当前的Activity和另外的Activity进行判断
        self.assertEqual(self.driver.current_activity,'.MarketActivity')
    if self.methodName == 'homeEnterMine':
        homeEnterMine(self)
        # 取得当前的Activity和另外的Activity进行判断
        self.assertEqual(self.driver.current_activity,'.MarketActivity')








