# encoding=utf-8
import unittest

class TestSuit(unittest.TestCase):
    def setUp(self):
        pass
    def testadd(self):
        self.assertEqual(2,4)
        print '1'
    def testadd1(self):
        print 'testadd1'

    def tearDown(self):
        pass
if __name__=="__main__":
    suit = unittest.TestSuite()
    suit.addTest(TestSuit('testadd1'))
    runer = unittest.TextTestRunner()
    runer.run(suit)





