# encoding=utf-8
from calculator import Count
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        print 'test0827.txt start'

    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)

    def test_add2(self):
        j = Count(41,76)
        self.assertEqual(j.add(),117)

    def tearDown(self):
        print 'test0827.txt stop'

    def setUp(self):
        print 'test0827.txt start'

    def test_sub(self):
        j = Count(2,3)
        self.assertEqual(j.sub(),-1)

    def test_sub2(self):
        j = Count(41,76)
        self.assertEqual(j.sub(),-35)

    def tearDown(self):
        print 'test0827.txt stop'

if __name__=='__main__':
#     构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add2"))
    suite.addTest(TestCount("test_sub"))
    suite.addTest(TestCount("test_sub2"))
#     执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.main

