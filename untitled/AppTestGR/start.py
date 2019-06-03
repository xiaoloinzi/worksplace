# encoding=utf-8
import unittest,logging,os
from common import util
import Download,Wode

logger = logging.getLogger('start')
logger.setLevel(logging.DEBUG)

path = os.getcwd() + '/tests/results/'
log = util.createMainLog(path)

logger.info('begin to generate testcase')
ts = unittest.TestSuite()
testLoader = unittest.defaultTestLoader
t1 = testLoader.loadTestsFromName('Download.APPCenter.test_download_music')
t2 = testLoader.loadTestsFromName('Download.APPCenter.test_download_notexist2')
# ts.addTest(t1)
ts.addTest(t2)
unittest.TextTestRunner(verbosity=2).run(ts)







