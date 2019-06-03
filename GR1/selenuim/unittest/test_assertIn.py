# encoding=utf-8
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        print 'test0827.txt start'

    def test_case(self):
        a = 'hello'
        b = 'hello world'
        self.assertIn(a,b,msg='a is not b')

    def tearDown(self):
        print 'test0827.txt end'

if __name__=='__main__':
    unittest.main


