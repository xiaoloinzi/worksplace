# encoding=utf-8
import time

def pkgmgrEnterMgr(self):
    time.sleep(3)
    self.driver.press_keycode('4')

def walk(self):
    if self.methodName == 'pkgmgrEnterMgr':
        pkgmgrEnterMgr(self)
        #习题修改下面的第2个参数，为实际的activity
        self.assertEqual(self.driver.current_activity, '.MarketActivity')
