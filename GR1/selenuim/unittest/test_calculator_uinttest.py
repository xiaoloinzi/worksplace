# encoding=utf-8
from calculator import Count
import unittest#引入unittest模块

class TestCount(unittest.TestCase):#TestCount继承unittest的Testcase类


    def setUp(self):
        # setUp方法用于测试用例执行的初始化
        print 'test0827.txt start'

    def test_add(self):
        '''
        在test_add中首先调用Count类并传入要计算的数，通过add（）方法得到两数相加
        的返回值，这里不再使用繁琐的异常处理，而是调用unittest框架所提供的assertEqual（）
        方法对add（）的返回值进行断言，判断两者是否相等，

        '''
        j = Count(2,3)
        self.assertEqual(j.add(),5)

    def tearDown(self):
        print 'test0827.txt end'

if __name__=='__main__':
    '''
    unittest 提供了全局的main（）方法，使用它们可以方便的将一个单元测试模块变成可以直接运行
    的测试脚本，main（）方法使用TestLoader类来搜索所有包含在该模块中以“test0827.txt”
    命名开头的测试方法，并主动执行它们
    '''
    unittest.main