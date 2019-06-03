# encoding=utf-8
import requests,json,TestCaseManager,Common
#发送消息的方法
def sendMessge(type,url,params):
    r = None
    if str(type).strip().lower() == "get":
        r = requests.get(url, params=params)
    if str(type).strip().lower() == "post":
        r = requests.post(url, params=params)
    if str(type).strip().lower() == "delete":
        r = requests.delete(url, params=params)
    if str(type).strip().lower() == "put":
        r = requests.put(url, params=params)
    # print r.content
    return  r
#执行用例
def testCaseRun(testCaseId,preContdtion,preContdtionOutput,testStep,testStepOutput,endCondition,espectResult):
    # print preContdtion,preContdtionOutput,testStep,testStepOutput,endCondition,espectResult,row
    result = "" #定义操作结果
    isSuccess = "pass" #初始化用例执行结果为pass
    failedReason=""     #记录失败的可能原因
    preContdtionOutputDic = {}
    testStepOutputDic = {}
    # 参数需要使用集合隔开,如下
    # ["login":{"userName": "$userName", "userPwd": "test"},"login":{"userName": "$userName", "userPwd": "test"}]
    #前置条件
    try:
        if preContdtion != None:
            params = json.loads(str(preContdtion).strip())
            for param in params:
                interfaceName_preContdtion = param.keys()[0]
                params_preContdtion = param.get(param.keys()[0])
                url = TestCaseManager.preUrl + str(TestCaseManager.interfaceInfoDic[interfaceName_preContdtion]["path"])
                type = TestCaseManager.interfaceInfoDic[interfaceName_preContdtion]["interfaceType"]
                result = sendMessge(type,url,params_preContdtion).content
                if preContdtionOutput != None:
                    keys = preContdtionOutput.split(",")
                    jsonResult = json.loads(result)
                    for key in keys:
                        subKeys = key.split(".")
                        keyValue = jsonResult.get(subKeys[0])
                        for i in range(1, len(subKeys)):
                            keyValue = keyValue[subKeys[i]]
                        # 取出值后加入到字典中
                        preContdtionOutputDic[key] = keyValue
    except AssertionError, e:
        isSuccess = "failed"
        failedReason = "preContdtion failed"+str(e)
    except Exception, e:
        isSuccess = "failed"
        failedReason = "preContdtion failed"+str(e)
    # 返回执行结果，失败直接返回
    if isSuccess == "failed":
        return result, isSuccess, failedReason
    # 执行用例
    try:
        if testStep != None:
            params = json.loads(str(testStep).strip())
            for param in params:
                interfaceName_testStep = param.keys()[0]
                params_testStep = param.get(param.keys()[0])
                url = TestCaseManager.preUrl + str(TestCaseManager.interfaceInfoDic[interfaceName_testStep]["path"])
                for k, v in preContdtionOutputDic.items():
                    params_testStep = Common.updateJsonObjByKey(params_testStep, k, v)
                type = TestCaseManager.interfaceInfoDic[interfaceName_testStep]["interfaceType"]
                result = sendMessge(type,url,params_testStep).content
                # 验证结果
                assert cmp(result,str(espectResult)) == 0
                #如果测试过程中需要获取输出结果，则将结果从返回消息中取出，并保存json格式
                if testStepOutput != None:
                    keys = testStepOutput.split(",")
                    jsonResult = json.loads(result)
                    for key in keys:
                        subKeys = key.split(".")
                        keyValue = jsonResult.get(subKeys[0])
                        for i in range(1,len(subKeys)):
                            keyValue =keyValue[subKeys[i]]
                        #取出值后加入到字典中
                        testStepOutputDic[key] = keyValue
    except AssertionError,e:
        isSuccess = "failed"
        failedReason = "result is not equal to espectResult"
    except Exception,e:
        isSuccess = "failed"
        failedReason =  "send message failed," +str(e)
    # 返回执行结果，失败直接返回
    if isSuccess == "failed":
        return result, isSuccess, failedReason
    #后置条件（清理环境)
    # 将输出结果填入到后置条件中
    try:
        if endCondition != None:
            params = json.loads(str(endCondition).strip())
            for param in params:
                interfaceName_endCondition = param.keys()[0]
                params_endCondition = param.get(param.keys()[0])
                url = TestCaseManager.preUrl + str(TestCaseManager.interfaceInfoDic[interfaceName_endCondition]["path"])
                for k, v in testStepOutputDic.items():
                    params_endCondition = Common.updateJsonObjByKey(params_endCondition, k, v)
                # 在后置条件中进行消息发送
                type = TestCaseManager.interfaceInfoDic[interfaceName_endCondition]["interfaceType"]
                result = sendMessge(type,url,params_endCondition).content
    except Exception,e:
        isSuccess="failed"
        failedReason="endCondition failed"
    #返回执行结果
    return result,isSuccess,failedReason

#启动执行用例
def run(testCaseList):
    for testCaseDic in testCaseList:
        testCaseId =  testCaseDic["testCaseId"]
        preContdtion =testCaseDic["preContdtion"]
        preContdtionOutput = testCaseDic["preContdtionOutput"]
        testStep = testCaseDic["testStep"]
        testStepOutput =testCaseDic["testStepOutput"]
        endCondition =testCaseDic["endCondition"]
        espectResult = testCaseDic["espectResult"]
        result, isSuccess, failedReason = testCaseRun(testCaseId,preContdtion,preContdtionOutput,testStep,testStepOutput,endCondition,espectResult)
        print result,isSuccess,failedReason
    return testCaseList