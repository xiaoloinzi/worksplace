# encoding=utf-8
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    @unittest.skip('直接跳过测试')
    def test_skip(self):
        print 'test_aaa'

    @unittest.skipIf(3>2,'当条件为TRUE时，跳过测试')
    def test_skipif(self):
        print 'test_bbb'

    @unittest.skipUnless(3>2,'当条件为True时，执行测试')
    def test_skipUnless(self):
        print 'test_ccc'

    @unittest.expectedFailure
    def test_expectedfailure(self):
        self.assertEqual(2,3)

if __name__=='__main__':
    unittest.main()