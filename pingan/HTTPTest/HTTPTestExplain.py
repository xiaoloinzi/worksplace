# coding=utf-8
import xlrd
import os
import imp
import unittest

#依据excle中的接口信息，生成接口的字典数据
#我们期望读取文件之后的数据结构是如下的：
# {
#     'interfaceName':{
#                     'interfacetype':'post',
#                     'url':'xx.xx.xx.xx'
#                     'normalparams':[{'key1':v1,'key2':v2},{xxx}],
#                     'faultparmas':[{'key1':v11,'key2':v22},{xxx}}],
#                     'mormalResult':[str1,str2],
#                     'faultResult':[str1,str2],
#                     'normalState':xx,
#                     'faultState':xx
#                     }
#     'interfaceName2':{
#                     xxx
#                     }
# }
def genSourceData(file):
    #打开excle
    wBook = xlrd.open_workbook(file)
    sheetName = wBook.sheet_names()[0]
    sheet = wBook.sheet_by_name(sheetName)
    interfaceList = []

    #首先，我们需要知道excle文件中，有多少个接口，以及每个接口信息的行数，那我们构造如下的数据结构来表示上述信息：
    #[接口名称,[接口在第几行],[接口信息总共有多少行]]
    #例如：[['getip', 1, 1], ['postIntf', 2, 2]]
    nrows = sheet.nrows
    #遍历每一行，第一列非空，则是接口名称，把接口名称，以及接口行数，加入到列表interfaceList,得到如下信息：[['getip', 1], ['postIntf', 2]]
    for i in range(1, nrows):
        if sheet.cell(i, 0).value != '':
            interfaceName = str(sheet.cell(i,0).value)
            interfaceRow = i
            interfaceList.append([interfaceName, interfaceRow])
    #把每个接口的行数，存入lenList
    lenList = []
    for i in range(len(interfaceList)-1):
        lenList.append(interfaceList[i+1][1]-interfaceList[i][1])
    lenList.append(nrows-interfaceList[len(interfaceList)-1][1])
    #合并成最终的数据结构：[['getip', 1, 1], ['postIntf', 2, 2]]
    for i in range(len(interfaceList)):
        interfaceList[i].append(lenList[i])

    print interfaceList

    #对于自动化生成测试用例，难点在于构造测试用例 body 的key value，所以专门定义了方法getParams来生成测试用例的body
    #我们期望的返回值是如下的：[[{key1:v1},{key1:v11}],[{key2:v2},{key2:v22}]],其中，列表的每一个元素是一个用例
    #入参interfaceL 是我们上面获取的接口信息，即：['getip', 1, 1]；normalParams 表示是生成正常用例还是异常用例
    def getParams(interfaceL, normalParams=True):
        pList = []
        resultList = []
        #依据normalParams 的值,表示要生成正常用例还是异常用例
        if normalParams == True:
            colNum = 4
        else:
            colNum = 5
        #获取所有的key value值，生成如下的数据结构：[[{key1:v1},{key1:v11}], [{key2:v2},{key2:v22}], [{key3:v3},{key3:v33},{key3:v333}]]
        #列表中的每一个元素，是对应的key value 的所有取值
        #结果存放在pList中
        for j in range(interfaceL[1],interfaceL[1]+interfaceL[2]):
            keyName = str(sheet.cell(j,3).value)
            keyVarList = str(sheet.cell(j,colNum).value).split(',')

            pList.append([{keyName:x} for x in keyVarList])

        if pList == []:
            return pList
        #生成resultList，其结构是[{key1:v1,key2:v2}]，作为一个基础列表
        aLen = len(pList)
        baseDict = {}
        resultList = []
        for i in range(aLen):
            baseDict = dict(baseDict.items() + pList[i][0].items())

        resultList.append(baseDict)
        print baseDict
        print resultList

        #从key1到key2到keyn，替换resultList中对应的value值，保证遍历所有的value值，之后把新元素附加到resultList中，这样得到了所有的测试用例
        #最终的数据结构如下：[[{key1:v1},{key1:v11}],[{key2:v2},{key2:v22}]],其中，列表的每一个元素是一个用例
        for i in range(0, len(pList)):
            for j in range(1, len(pList[i])):
                tmpDict = baseDict.copy()
                print 'tmpDict is ' + str(tmpDict)
                tmpDict.pop(pList[i][j].keys()[0])
                tmpDict = dict(tmpDict.items() + pList[i][j].items())
                resultList.append(tmpDict)
        return resultList

    #获取消息体中的key:value
    sourceDataDict = {}
    for i in range(len(interfaceList)):
        interfaceType = str(sheet.cell(interfaceList[i][1],1).value)
        url = str(sheet.cell(interfaceList[i][1],2).value)
        mormalResult = str(sheet.cell(interfaceList[i][1],6).value)
        faultResult = str(sheet.cell(interfaceList[i][1],7).value)
        normalState = str(sheet.cell(interfaceList[i][1],8).value)
        faultState = str(sheet.cell(interfaceList[i][1],9).value)
        normalParams = getParams(interfaceList[i],True)
        faultParams = getParams(interfaceList[i],False)
        sourceDataDict[interfaceList[i][0]] = {'interfaceType':interfaceType,
                                               'url':url,
                                               'normalResult':mormalResult,
                                               'faultResult':faultResult,
                                               'normalState':normalState,
                                               'faultState':faultState,
                                               'normalParams':normalParams,
                                               'faultParams':faultParams
                                               }
    return sourceDataDict

def makeTestcase(dictData):
    keys = dictData.keys()
    for key in keys:
        #针对没一个接口，生成一个文件，写文件头信息
        filePath = os.getcwd() + '\\testcase\\' + key + '.py'
        fh = open(filePath, 'w')
        fh.write('# coding=utf-8\n'
                 'import unittest\n'
                 'import os\n'
                 'import requests\n'
                 '\n'
                 'class ' + key + 'Test' + '(unittest.TestCase):\n'
                 )
        #遍历正常的列表，生成正常测试用例
        i=0
        for param in dictData[key]['normalParams']:
            if dictData[key]['interfaceType'] == 'get':
                fh.write('    def test_'+key+'_normal'+str(i)+'(self):\n'
                         "        url = '"+dictData[key]['url']+"'\n"
                         "        r = requests.get(url,params="+str(param)+")\n\n"
                         "        #assert here\n"
                         "        self.assertTrue(r.status_code=="+str(int(dictData[key]['normalState'].split('.')[0]))+")\n"
                         "        self.assertTrue('"+str(dictData[key]['normalResult'])+"' in r.text)\n"
                        )
            elif dictData[key]['interfaceType'] == 'post':
                fh.write('    def test_' + key + '_normal' + str(i) + '(self):\n'
                         "        url = '"+dictData[key]['url']+"'\n"
                         "        r = requests.post(url,data="+str(param)+")\n\n"
                         "        #assert here\n"
                         "        self.assertTrue(r.status_code=="+str(int(dictData[key]['normalState'].split('.')[0]))+")\n"
                         "        self.assertTrue('"+str(dictData[key]['normalResult'])+"' in r.text)\n"
                         )
            else:
                continue
            i+=1

        # 遍历异常的列表，生成异常测试用例
        j = 0
        for param in dictData[key]['faultParams']:
            if dictData[key]['interfaceType'] == 'get':
                fh.write('    def test_' + key + '_fault' + str(j) + '(self):\n'
                         "        url = '"+dictData[key]['url']+"'\n"
                         "        r = requests.get(url,params="+str(param)+")\n\n"
                         "        #assert here\n"
                         "        self.assertTrue(r.status_code=="+str(int(dictData[key]['faultState'].split('.')[0]))+")\n"
                         "        self.assertTrue('"+str(dictData[key]['faultResult'])+"' in r.text)\n"
                        )
            elif dictData[key]['interfaceType'] == 'post':
                fh.write('    def test_' + key + '_fault' + str(j) + '(self):\n'
                         "        url = '"+dictData[key]['url']+"'\n"
                         "        r = requests.post(url,data="+str(param)+")\n\n"
                         "        #assert here\n"
                         "        self.assertTrue(r.status_code=="+str(int(dictData[key]['faultState'].split('.')[0]))+")\n"
                         "        self.assertTrue('"+str(dictData[key]['faultResult'])+"' in r.text)\n"
                        )
            else:
                continue
            j += 1

        fh.close()

#执行测试用例
def executeTestcase():
    #获取所有的测试文件
    path = os.getcwd() + '\\testcase'
    fileList = os.listdir(path)

    moduleList = [x.split('.')[0] for x in fileList]
    moduleList = list(set(moduleList))
    if '__init__' in moduleList:
        moduleList.remove('__init__')

    #导入所有测试模块
    mObj = []
    for mName in moduleList:
        mObj.append(imp.load_source(mName, os.getcwd() + '\\testcase\\' + mName + '.py'))

    #将所有的测试模块加载到TestSuite中
    testSuite = unittest.TestSuite()
    loader = unittest.defaultTestLoader
    for m in mObj:
        tests = loader.loadTestsFromModule(m)
        testSuite.addTests(tests)
    #执行测试套中的用例
    unittest.TextTestRunner().run(testSuite)


if __name__ == "__main__":
    fileName = os.getcwd()+"\\interfaceData.xlsx"
    dictData = genSourceData(fileName)
    makeTestcase(dictData)
    executeTestcase()


