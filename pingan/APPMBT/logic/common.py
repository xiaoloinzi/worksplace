# encoding=utf-8
import time
from core import util

def homeEnterManage(self):
    time.sleep(1)
    # el = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="管理"]')
    el = util.find_element(self.driver,u'//android.widget.TextView[@text="管理"]')
    el.click()

def homeEnterRank(self):
    time.sleep(1)

    el = self.driver.find_element_by_xpath('//android.widget.RelativeLayout[@index=1]/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=2]')
    el.click()

def homeEnterSuggest(self):
    time.sleep(1)
    el = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="推荐"]')
    el.click()

def homeEnterMine(self):
    time.sleep(1)
    el = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="我的"]')
    el.click()

def walk(self):
    if self.methodName == 'homeEnterManage':
        homeEnterManage(self)
        self.assertEqual(self.driver.current_activity, '.MarketActivity')
    if self.methodName == 'homeEnterRank':
        homeEnterRank(self)
        self.assertEqual(self.driver.current_activity, '.MarketActivity')
    if self.methodName == 'homeEnterSuggest':
        homeEnterSuggest(self)
        self.assertEqual(self.driver.current_activity, '.MarketActivity')
    if self.methodName == 'homeEnterMine':
        homeEnterMine(self)
        self.assertEqual(self.driver.current_activity, '.MarketActivity')























