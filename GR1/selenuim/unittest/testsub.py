# encoding=utf-8
from calculator import Count
import unittest

class TestSub(unittest.TestCase):

    def setUp(self):
        print 'test0827.txt start'

    def tearDown(self):
        print 'test0827.txt end'

    def test_sub(self):
        j = Count(2,3)
        self.assertEqual(j.sub(),-1)

    def test_sub2(self):
        j = Count(71,46)
        self.assertEqual(j.sub(),25)

if __name__=='__main__':
    unittest.main
