# encoding=utf-8
import os
import logging
import time


def getTestDataInput(moduleName,testCase):
#     1、用moduleName找到testData下的cvs文件
# 2、用testcase找到输入，用dict的形式存储
    filepath = 'E:\\worksplace\\AppTestGR2\\tests\\testData\\'+moduleName+'.csv'
    list1 = []
    list2 = []
    dicts = {}
    with open(filepath) as fp:
        line = fp.readlines()
    for i in xrange(1,len(line)):
        list1.append(line[i].rstrip('\n').split(','))
    # print list1

    for i in xrange(len(list1)):
        if list1[i][1]==testCase:
            list2.append(list1[i][2].split('|'))
            print list2[0]
            for i in xrange(len(list2[0])):
                if list2[0][i] != "":
                    dicts[list2[0][i].split('=',1)[0]]=list2[0][i].split('=',1)[1]
    return dicts
print getTestDataInput("Wode","test_wode02")



def createMainLog(path):
    # path = 'E:\\worksplace\\AppTestGR2\\tests\\results\\'
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
    console = logging.StreamHandler()
    confile = logging.FileHandler(path+time.strftime('%Y%m%d%H%M%S_Mainlog',time.localtime())+'.csv')
    logRoot.info('Time,Level,Logger Name,Message')
    formatter = logging.Formatter(
        '%(asctime)2s | %(levelname)-5s |%(name)s| %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    console.setFormatter(formatter)
    confile.setFormatter(formatter)
    logRoot.addHandler(console)
    logRoot.addHandler(confile)
    #创建一个streamhandle，其日志格式是：
    #%(asctime)s","%(levelname)s","%(name)s","%(message)s"
    return logRoot












