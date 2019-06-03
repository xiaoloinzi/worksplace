# encoding=utf-8
from count import is_prime
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        print 'test0827.txt start'

    def test_case(self):
        self.assertTrue(is_prime(7),msg='Is not prime')

    def tearDown(self):
        print 'test0827.txt end'

if __name__=='__main__':
    unittest.main