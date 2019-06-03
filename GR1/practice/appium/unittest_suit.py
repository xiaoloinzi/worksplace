# encoding=utf-8
import unittest
import t2

class c13(unittest.TestCase):
    def setUp(self):
        print 'setup now'

    def test1(self):
        print 't3 testcase 1'
        self.assertEqual(1+1,2)

    def test2(self):
        self.skipTest("强制跳过示例2")
        print 't3 testcase 2'
        self.assertEqual('abc','ab'+'c')

    @unittest.skip('暂时跳过用例3的测试')
    def test3(self):
        print 't3 testcase 3'
        self.assertEqual('abc','ab'+'c')

    def tearDown(self):
        print 'teardown now'

if __name__=="__main__":
    testSuit = unittest.TestSuite()
    # testLoader = unittest.defaultTestLoader
    # test2 = testLoader.loadTestsFromName('unittest_suit.c13.test1')
    # unittest.TextTestRunner(verbosity=2).run(test2)
    testSuit.addTest(c13('test3'))
    runner = unittest.TextTestRunner()
    runner.run(testSuit)















