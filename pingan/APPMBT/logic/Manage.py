# encoding=utf-8
import time

def mgrEnterPkgmgr(self):
    time.sleep(1)
    el = self.driver.find_element_by_xpath(u'//android.widget.TextView[@text="安装包管理"]')
    el.click()

def walk(self):
    if self.methodName == 'mgrEnterPkgmgr':
        mgrEnterPkgmgr(self)
        #习题修改下面的第2个参数，为实际的activity
        self.assertEqual(self.driver.current_activity, self.driver.current_activity)



