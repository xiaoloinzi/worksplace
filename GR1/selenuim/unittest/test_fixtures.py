# encoding=utf-8
import unittest

def setUpModule():
    print 'test0827.txt modul start>>>>>>>>>>>'

def tearDownModule():
    print 'test0827.txt modul end>>>>>>>>>>>>>'

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print 'test0827.txt class start============>'


    @classmethod
    def tearDownClass(cls):
        print 'test0827.txt class end=============>'

    def setUp(self):
        print 'test0827.txt start -->'

    def tearDown(self):
        print 'test0827.txt end -->'

    def test_case(self):
        print 'test_case'

    def test_case2(self):
        print 'test0827.txt case2'


if __name__=='__main__':
    unittest.main()

