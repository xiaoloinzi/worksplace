# encoding=utf-8
import unittest
import appium_01,appium_02


# 习题3： 在2个文件中， 分别写4个测试用例， 每个运行两个测试用例
# 习题3：在2个文件中，分别写超过2个测试用例，
# 运行另外一个模块的所有测试用例，和本模块的两个测试用例


testsuit = unittest.TestSuite()
testload = unittest.defaultTestLoader
test1 = testload.loadTestsFromModule(appium_01)
test2 = testload.loadTestsFromModule(appium_02)
testsuit.addTests([test1,test2])
unittest.TextTestRunner(verbosity=2).run(testsuit)










