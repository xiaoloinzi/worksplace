# encoding=utf-8
import unittest
import testadd
import testsub

suite = unittest.TestSuite()

suite.addTest(testadd.Testadd('test_add2'))
suite.addTest(testsub.TestSub('test_sub2'))

if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)

