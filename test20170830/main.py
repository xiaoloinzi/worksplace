# encoding=utf-8
from  scripts import TestCaseManager
import os

if __name__ == '__main__':
    initFile = os.getcwd()+"\\data\\testCase.xlsx"
    #初始化用例信息
    file = TestCaseManager.initTestCase(initFile)
    #获取用例执行数据
    testCaseList = TestCaseManager.getTestCaseInfo(file)
    print testCaseList
    #启动用例执行
    testCaseList = TestCaseManager.run(testCaseList)