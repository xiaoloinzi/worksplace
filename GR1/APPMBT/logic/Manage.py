# encoding=utf-8
import time
from GR1.APPMBT.core import util

def mgrEnterPkgmgr(self):
    time.sleep(1)
    e1 = util.find_element(self.driver,u'//android.widget.TextView[@text="安装包管理"]')
    e1.click()

def walk(self):
    if self.methodName == 'mgrEnterPkgmgr':
        mgrEnterPkgmgr(self)
        # 取得当前的Activity和另外的Activity进行判断
        self.assertEqual(self.driver.current_activity,'.service.appmgr.apkmanagement.activity.ApkManagementActivity')



