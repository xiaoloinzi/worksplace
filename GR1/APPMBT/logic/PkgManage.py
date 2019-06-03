# encoding=utf-8
import time

def PkgmgrEnterMgr(self):
    time.sleep(3)
    self.driver.press_keycode('4')

def walk(self):
    if self.methodName == 'PkgmgrEnterMgr':
        PkgmgrEnterMgr(self)
        # 取得当前的Activity和另外的Activity进行判断
        self.assertEqual(self.driver.current_activity,'.MarketActivity')


