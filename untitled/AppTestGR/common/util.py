# encoding=utf-8
import os,logging,time



def createMainLog(path):
    #1、首先判断path是否存，不存在则创建
    if  not os.path.exists(path):
        os.makedirs(path)
    logsDir = path

    #获取根日志
    logRoot = logging.getLogger()
    logRoot.setLevel(logging.DEBUG)

    #创建一个filehandle，其日志格式是：
    #且文件的第一行是：'Time,Level,Logger Name,Message'
    #文件规则是tests/results/%Y%m%d%H%M%S_Mainlog.csv
    #（%(asctime)s","%(levelname)s","%(name)s","%(message)s"）
    logHandleRoot = logging.FileHandler(path+time.strftime('%Y%m%d%H%M%S')+'_Mainlog.csv')
    logHandleRoot.setLevel(logging.DEBUG)
    logRoot.addHandler(logHandleRoot)
    logRoot.info('Time,Level,Logger Name,Message')
    fileFormater = logging.Formatter('%(asctime)s","%(levelname)s","%(name)s","%(message)s')
    logHandleRoot.setFormatter(fileFormater)


    #创建一个streamhandle，其日志格式是：
    #%(asctime)s","%(levelname)s","%(name)s","%(message)s"
    logHandle = logging.StreamHandler()
    logHandle.setLevel(logging.INFO)
    streamFormter = logging.Formatter('%(asctime)s","%(levelname)s","%(name)s","%(message)s')
    logHandle.setFormatter(streamFormter)
    logRoot.addHandler(logHandle)

    return logRoot












def getTestDataInput(moduleName,testCase):
    #1、用moduleName找到testData下的csv文件
    #2、用testCase找到输入，用dict 的形式报错
    filepath = os.getcwd() + '/tests/testData/'+moduleName+'.csv'
    retDict= {}
    dataList = []
    dataLists = []
    with open(filepath) as fp:
        infoList = fp.readlines()
    for i in xrange(1,len(infoList)):
        dataList.append(infoList[i].rstrip('\n').split(','))
    for i in range(len(dataList)):
        if dataList[i][1] == testCase:
            dataLists = dataList[i][2].split('|')
    for j in xrange(len(dataLists)):
        index = dataLists[j].index('=')
        # retDict[dataLists[j][:index]] = dataList[j][index+1:].replace("'","")
        retDict[dataLists[j].split('=')[0]] = dataLists[j].split('=')[1].replace("'","")
    return retDict























