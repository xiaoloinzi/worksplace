# encoding=utf-8
import os,json
#获取普通响应
def getResponse(fileName):
    resultDict = {}
    fileNameDir = str(fileName).split("_response")[0]
    with open(os.getcwd()+"\\data\\"+fileNameDir+"\\"+fileName,"r") as f:
            resultDict = json.load(f)
    return resultDict
#获取通知结果
def getNotify(fileName):
    resultDict = {}
    fileNameDir = str(fileName).split("_notify")[0]
    with open(os.getcwd()+"\\data\\"+fileNameDir+"\\"+fileName,"r") as f:
            resultDict = json.load(f)
    return resultDict
