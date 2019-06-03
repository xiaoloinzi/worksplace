# encoding=utf-8
import os,logging,time,unittest,imp,ConfigParser

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

def getTestDataraw(moduleName):
    filepath = os.getcwd() + '/tests/testData/' + moduleName + '.csv'
    dataListtmp = []
    with open(filepath) as fp:
        infoList = fp.readlines()
    for i in xrange(1, len(infoList)):
        if infoList[i].strip() != '':
            dataListtmp.append(infoList[i].rstrip('\n').split(','))
    return dataListtmp


def getTestDataInput(moduleName,testCase):
    #1、用moduleName找到testData下的csv文件
    #2、用testCase找到输入，用dict 的形式报错
    filepath = os.getcwd() + '/tests/testData/'+moduleName+'.csv'
    retDict= {}
    dataListtmp = []
    dataLists = []
    with open(filepath) as fp:
        infoList = fp.readlines()
    for i in xrange(1,len(infoList)):
        if infoList[i].strip() != '':
            dataListtmp.append(infoList[i].rstrip('\n').split(','))
    # print dataList
    for i in range(len(dataListtmp)):
        if dataListtmp[i][1] == testCase:
            dataLists = dataListtmp[i][2].split('|')
    # print dataLists
    for j in xrange(len(dataLists)):
        index = dataLists[j].index('=')
        retDict[dataLists[j][:index]] = dataLists[j][index+1:].replace("'","").replace('，',',')
        # retDict[dataLists[j].split('=')[0]] = dataLists[j].split('=')[1].replace("'","")
    print retDict
    return retDict

def getScriptsList(path):
    files = os.listdir(path)
    moduleList = []
    for f in files:
        if f.endswith('.py') and f != '__init__.py':
            fileName = path+'/'+f
            moduleName = os.path.splitext(f)[0]
            scriptModule = imp.load_source(moduleName,fileName)
            moduleList.append([moduleName,scriptModule])
    return moduleList


def getConfig(sessionName,key):
    conf = ConfigParser.ConfigParser()
    path = os.getcwd()
    fileName = path+'/config/config.cfg'
    conf.read(fileName)
    value = conf.get(sessionName,key)
    return value

def loadTestScripts():
    curPath = os.getcwd()
    categoryList = []
    fileName = curPath + '/config/category.cfg'
    with open(fileName) as fp:
        resultList = fp.readlines()
    for i in xrange(len(resultList)):
        if resultList[i].startswith('#') is False and resultList[i].rstrip() != '':
            categoryList.append(resultList[i].rstrip().split('.'))

    print categoryList

    moduleList = getScriptsList(os.getcwd()+'/tests/scripts')
    print moduleList

    ts = unittest.TestSuite()
    loader = unittest.defaultTestLoader

    #格式：[['Wode','test_wode01'],['Wode']]
    #moduleList 的格式：[['Download', <module 'Download' from 'E:\workspace\GRStudy\AppTestGR2/tests/scripts/Download.pyc'>], ['Wode', <module 'Wode' from 'E:\workspace\GRStudy\AppTestGR2/tests/scripts/Wode.pyc'>]]
    for i in xrange(len(categoryList)):
        if categoryList[i][0] == '*':
            for k in xrange(len(moduleList)):
                tests = loader.loadTestsFromModule(moduleList[k][1])
                ts.addTests(tests)
        else:
            for j in xrange(len(moduleList)):
                #处理只带moduleName，则loadTestsFromModule
                if len(categoryList[i]) == 1 and moduleList[j][0] == categoryList[i][0]:
                    tests = loader.loadTestsFromModule(moduleList[j][1])
                    ts.addTests(tests)
                #处理
                elif moduleList[j][0] == categoryList[i][0] and len(categoryList[i]) == 2:
                    tests = loader.loadTestsFromName(categoryList[i][0]+'.'+categoryList[i][1],moduleList[j][1])
                    ts.addTests(tests)
    return ts






























