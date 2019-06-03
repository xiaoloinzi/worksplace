# encoding=utf-8

import GR1.APPMBT.graph.Graph as gra
from GR1.APPMBT.graph import PathDict
import os,imp
import time
import logging

currentNode = None
def initGraph():
    gra.addEdge('Suggest','Manage')
    gra.addEdge('Suggest','Rank')
    gra.addEdge('Suggest','Mine')
    gra.addEdge('Rank','Manage')
    gra.addEdge('Rank','Suggest')
    gra.addEdge('Rank','Mine')
    gra.addEdge('Manage','Suggest')
    gra.addEdge('Manage','Rank')
    gra.addEdge('Manage','Mine')
    gra.addEdge('Mine','Suggest')
    gra.addEdge('Mine','Rank')
    gra.addEdge('Mine','Manage')
    gra.addEdge('Manage','PkgManage')
    gra.addEdge('PkgManage','Manage')

def getTestDataraw():
    # filepath = os.getcwd() + '/testData/specifiedPath.csv'
    filepath = 'E:\\worksplace\\GR1\APPMBT\\testData\\specifiedPath.csv'
    list1 = []
    with open(filepath,'r') as fp:
        line = fp.readlines()
    for i in line:
        stri = i.strip('\n').split(',')
        list1.append(stri)
    return list1

# 自动随机运行函数
def randomPathWalk(self):
    gra.genAllShortPath()
    sourceNode = 'Suggest'
    for i in xrange(10):
        # 获得以sourceNode开头的随机路径
        path = gra.randomPath(sourceNode)
        try:
            # 从srcnode 到dsc_node，即走该路径
            callAction(self,path)
        except Exception as err:
            print 'error msg:',err.message
            break
        sourceNode = path[len(path)-1]
        print i
        print sourceNode

# 指定路径运行函数
def getPathWalk(self):
    gra.genAllShortPath()
    lista = getTestDataraw()
    if len(lista) > 1:
        for i in xrange(1,len(lista)):
            print lista[i][1],lista[i][2]
            path = gra.getPath(lista[i][1],lista[i][2])
            try:
                callAction(self,path)
            except Exception as err:
                print 'error msg:',err.message
                break
    else:
        print 'specifiedPath.csv is null'

# 无差异化的走a走到b点
def callAction(self,path):
    print u'执行路径：',str(path)
    pathLen = len(path)
    for i in xrange(pathLen-1):
        global currentNode
        currentNode = path[i]
        actionKey = path[i]+"-"+path[i+1]
        actionValue = PathDict.actionsDict.get(actionKey)
        print 'actionKey:',actionKey,'actionValue:',actionValue

        actionItems = actionValue.split(':')
        classFile = actionItems[0]
        # 指向文件
        classFile = PathDict.pageDict.get(classFile)
        # 指向方法名称
        classMethod = actionItems[1]
        # 动态加载
        self.methodName = classMethod
        moduleName = os.path.basename(classFile)
        moduleName = os.path.splitext(moduleName)[0]

        moduleObj = imp.load_source(moduleName,classFile)
        moduleObj.walk(self)


def find_element(driver,idOrXpath,n=10):
    for i in xrange(n):
        try:
            if idOrXpath.startswith('/'):
                ret = driver.find_element_by_xpath(idOrXpath)
            else:
                ret = driver.find_element_by_id(idOrXpath)
            return ret
        except Exception as err:
            print err.message
            time.sleep(2)
    raise Exception('element %s could not be found'%idOrXpath)


def createMainLog(path):
    #1、首先判断path是否存，不存在则创建
    if  not os.path.exists(path):
        os.makedirs(path)

    #获取根日志
    logRoot = logging.getLogger()
    logRoot.setLevel(logging.DEBUG)
    # 写入文件
    logHandleRoot = logging.FileHandler(path+time.strftime('%Y%m%d%H%M%S')+'_Mainlog.csv')
    logHandleRoot.setLevel(logging.DEBUG)
    logRoot.addHandler(logHandleRoot)
    logRoot.info('Time,Level,Logger Name,Message')
    fileFormater = logging.Formatter('%(asctime)s","%(levelname)s","%(name)s","%(message)s')
    logHandleRoot.setFormatter(fileFormater)

    # 控制台输出
    logHandle = logging.StreamHandler()
    logHandle.setLevel(logging.DEBUG)
    streamFormter = logging.Formatter('%(asctime)s","%(levelname)s","%(name)s","%(message)s')
    logHandle.setFormatter(streamFormter)
    logRoot.addHandler(logHandle)
    return logRoot








