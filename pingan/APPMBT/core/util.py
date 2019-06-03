# encoding=utf-8

import os,imp,time
import graph.Graph as gra
from graph import PathDict

currentNode = None

def initGraph():
    gra.addEdge('Suggest','Manage')
    gra.addEdge('Suggest','Rank')
    gra.addEdge('Rank','Manage')
    gra.addEdge('Rank','Suggest')
    gra.addEdge('Manage','Suggest')
    gra.addEdge('Manage','Rank')
    gra.addEdge('Manage','PkgManage')
    gra.addEdge('PkgManage','Manage')
    gra.addEdge('Mine','Manage')
    gra.addEdge('Mine','Suggest')
    gra.addEdge('Mine','Rank')
    gra.addEdge('Manage','Mine')
    gra.addEdge('Suggest','Mine')
    gra.addEdge('Rank','Mine')


#自动随机运行函数
def randomPathWalk(self):
    gra.genAllShortestPath()
    sourceNode = 'Suggest'

    for i in xrange(10):
        #获得以sourceNode开头的随机路径
        path = gra.randomPath(sourceNode)
        try:
            #从src_node走到dst_node，即走该路径
            callAction(self,path)
        except Exception as err:
            print 'error msg:',err.message
            break
        sourceNode = path[len(path)-1]
        print i

#无差异化的走a走到b点
def callAction(self,path):
    print u'执行路径：',str(path)
    pathLen = len(path)
    for i in xrange(pathLen-1):
        global currentNode
        currentNode = path[i]
        actionKey = path[i]+'-'+path[i+1]
        actionValue = PathDict.actionsDict.get(actionKey)
        print 'actionKey:',actionKey,' actionValue:',actionValue

        actionItems = actionValue.split(':')
        classFile = actionItems[0]
        classFile = PathDict.pageDict.get(classFile)
        classMethod = actionItems[1]

        #动态加载
        self.methodName = classMethod
        moduleName = os.path.basename(classFile)
        moduleName = os.path.splitext(moduleName)[0]

        moduleObj = imp.load_source(moduleName,classFile)
        moduleObj.walk(self)

#按照指定的路径执行用例
def spefiedPathWalk(self):
    gra.genAllShortestPath()
    path = os.getcwd()
    file = path + '/testData/' + 'specifiedPath.csv'

    fh = open(file, 'r')
    lines = fh.readlines()
    curNode = 'Suggest'

    #读取文件中的每一行，并且运行该路径
    for i in range(1, len(lines)):
        nodeList = lines[i].rstrip('\n').split(',')
        sNode = nodeList[1]
        dNode = nodeList[2]
        try:
            if curNode != sNode:
                adjustPath = gra.getPath(curNode, sNode)
                callAction(self, adjustPath)
            walkPath = gra.getPath(sNode, dNode)
            callAction(self, walkPath)
        except Exception as err:
            print err.message
            break
        curNode = dNode


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























