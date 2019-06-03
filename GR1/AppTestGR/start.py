# encoding=utf-8
import unittest,logging,os
from GR1.AppTestGR.common import util
from GR1.AppTestGR.tests.scripts import Wode

logger = logging.getLogger('start')
logger.setLevel(logging.DEBUG)

path = os.getcwd() + '/tests/results/'
log = util.createMainLog(path)

# logger.info('begin to generate testcase')
# ts = unittest.TestSuite()
# testLoader = unittest.defaultTestLoader
# t1 = testLoader.loadTestsFromName('Download.APPCenter.test_download_music')
# t2 = testLoader.loadTestsFromName('Download.APPCenter.test_download_notexist2')
# # ts.addTest(t1)
# ts.addTest(t2)
# unittest.TextTestRunner(verbosity=2).run(ts)

# ts = util.loadTestScripts()
# unittest.TextTestRunner(verbosity=2).run(ts)

# path = os.getcwd()+'/tests/scripts'
# moduleList = util.getScriptsList2(path)
# print moduleList
#
# print util.getConfig('Basic','deviceName')
#
# ts = unittest.TestSuite()
# testLoader = unittest.defaultTestLoader
# t1 = testLoader.loadTestsFromName('Wode.APPCenter.test_wode01')
# t2 = testLoader.loadTestsFromName('Wode.APPCenter.test_wode02')
# ts.addTest(t1)
# ts.addTest(t2)
# unittest.TextTestRunner(verbosity=2).run(ts)
# 框架结构化之后的代码
ts = util.loadTestScripts()
unittest.TextTestRunner(verbosity=2).run(ts)





















