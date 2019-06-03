# encoding=utf-8
import unittest
# 习题1：在一个文件中，写4个测试用例，之后全量运行
#
# 习题2：在一个文件中，写4个测试用例，只运行其中两个


class C13(unittest.TestCase):
    def setUp(self):
        print 'setup now'

    def test1(self):
        print 'test1 start'
        self.assertEqual(1+1,2)

    def test2(self):
        print 'test2 start'
        self.assertEqual(4,4)
    def test3(self):
        print 'test3 start'
    def test4(self):
        print 'test4 start'
    def tearDown(self):
        print 'tearDown'

if __name__=="__main__":
    # 最简单的执行逻辑
    # unittest.main
    # 最有在cmd中运行才会执行addtest的用例，否则都是执行unittest.main
    testSuite = unittest.TestSuite()
    testLoader = unittest.defaultTestLoader
    test2 = testLoader.loadTestsFromName('appium_02.C13.test2')
    test3 = testLoader.loadTestsFromName('appium_02.C13.test3')
    testSuite.addTests(test2)
    testSuite.addTests(test3)
    unittest.TextTestRunner(verbosity=2).run(testSuite)

















