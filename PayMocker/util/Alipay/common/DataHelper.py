#encoding=utf-8
import json
global dataFileAliPay,dataJsonAliPay
dataFileAliPay = None
dataJsonAliPay = None

def loadConfigFile(configFile):
    global dataFileAliPay
    dataFileAliPay = configFile.replace('\n','')
    with open(dataFileAliPay,'r') as f:
        global dataJsonAliPay
        dataJsonAliPay = json.load(f)


def getPayResult():
    global dataJsonAliPay
    return dataJsonAliPay['payResult']

def getNotifyDelay():
    global dataJsonAliPay
    return int(dataJsonAliPay['notifyDelay'])

def getValue(itemName):
    global dataJsonAliPay
    if itemName not in dataJsonAliPay:
        return None
    return dataJsonAliPay[itemName]






