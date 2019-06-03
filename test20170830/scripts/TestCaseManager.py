# encoding=utf-8
import DataManager,Common,MessageManager
global configInfoDic,preUrl,interfaceInfoDic
configInfoDic=None
preUrl=None
interfaceInfoDic=None

#初始化用例信息
def initTestCase(file):
    return Common.initTestCase(file)

#读取配置信息并保存
def getConfigInfo(testCaseFile):
    global configInfoDic,preUrl
    if configInfoDic == None:
        configInfoDic = DataManager.getConfigInfo(testCaseFile,0)
        preUrl = str(configInfoDic["protocolType"]) + "://" + str(configInfoDic["ip"]) + ":" + str(configInfoDic["port"])
#读取接口信息并保存
def getInterfaceInfo(testCaseFile):
    global interfaceInfoDic
    if interfaceInfoDic == None:
        interfaceInfoDic = DataManager.getInterfaceInfo(testCaseFile,1)

#用例执行完成后将用例信息
def getTestCaseInfo(testCaseFile):
     getConfigInfo(testCaseFile)
     getInterfaceInfo(testCaseFile)
     testCaseList = DataManager.readTestCase(testCaseFile=testCaseFile)
     return testCaseList
#执行用例
def run(testCaseList):
    testCaseList = MessageManager.run(testCaseList)
    return testCaseList