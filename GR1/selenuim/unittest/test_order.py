# encoding=utf-8
import unittest

class TestBdd(unittest.TestCase):

    def setUp(self):
        print 'test0827.txt start'


    def test_ccc(self):
        print 'cccc'

    def test_aaa(self):
        print 'aaa'

    def tearDown(self):
        print 'test0827.txt end'

class TestAdd(unittest.TestCase):

    def setUp(self):
        print 'test0827.txt start'

    def test_bbb(self):
        print 'bbb'


    def tearDown(self):
        print 'test0827.txt end'

if __name__=='__main__':
    # unittest.main()#直接按照默认顺序执行，按照ASCII的顺序加载测试用例
    suite = unittest.TestSuite()
    suite.addTest(TestBdd('test_ccc'))
    suite.addTest(TestAdd('test_bbb'))
    suite.addTest(TestBdd('test_aaa'))
    runner = unittest.TextTestRunner()
    runner.run(suite)