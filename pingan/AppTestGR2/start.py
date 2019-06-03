# encoding=utf-8
import unittest,logging,os
from common import util
from tests.scripts import Wode


logger = logging.getLogger('start')
logger.setLevel(logging.DEBUG)

path = os.getcwd() + '/tests/results/'
log = util.createMainLog(path)


logger.info('begin to generate testcase')

ts = util.loadTestScripts()
unittest.TextTestRunner(verbosity=2).run(ts)

# ts = unittest.TestSuite()
# testLoader = unittest.defaultTestLoader
# t1 = testLoader.loadTestsFromName('Wode.test_wode01',Wode)
# t2 = testLoader.loadTestsFromName('Wode.test_wode02',Wode)
# t2 = testLoader.loadTestsFromModule(Wode)
# t1 = testLoader.loadTestsFromModule(Wode)
# ts.addTest(t1)
# ts.addTest(t2)
# unittest.TextTestRunner(verbosity=2).run(ts)




# path = os.getcwd()+'/tests/scripts'
# moduleList = util.getScriptsList2(path)
# print moduleList
























