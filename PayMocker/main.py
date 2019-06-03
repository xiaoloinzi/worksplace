#encoding=utf-8
import threading,os

import util.Alipay.logic.PayLogic
from common.FlaskHelper import *
from util.Alipay.common import ConifgHelper
from  util.Alipay.api import PayApi
from  util.Alipay.logic import PayLogic

if __name__ == "__main__":

    dataFile = os.getcwd()+"\\util\\Alipay\\data\\data.json"
    configFile = os.getcwd() + "\\util\\Alipay\\config\\config.json"
    PayLogic.init(configFile,dataFile)
   #启动服务
    PayApi.app.run(host='0.0.0.0', port=8888,debug=True,threaded=True)
