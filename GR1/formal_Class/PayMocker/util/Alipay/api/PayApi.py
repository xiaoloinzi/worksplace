# -*- coding: utf-8 -*-
import json
import traceback
from flask import request
from common.FlaskHelper import *
from util.Alipay.logic import PayLogic

#运行过程中进行加载
app = FlaskHelper().app


@app.route('/gateway.do/<method>',methods=["post"])
def gateway(method):
    try:
        #接收请求消息
        responseDict = {}
        responsecolumn = method.replace('.', '_')
        charset = request.args.get('charset')
        sign = request.args.get('sign')
        sign_type = request.args.get('sign_type')
        timestamp = request.args.get('timestamp')
        app_id = request.args.get('app_id')
        version = request.args.get('version')
        biz_content = request.args.get('biz_content')
        #将消息内容转换成字典类型
        contentDict = json.loads(biz_content)
        if method == 'alipay.trade.precreate': #统一收单线下交易预创建（扫码支付）
            resultDic = PayLogic.alipay_trade_precreate(contentDict,responsecolumn)
        elif method == 'alipay.trade.pay':#条码支付
            resultDic = PayLogic.alipay_trade_pay(contentDict,responsecolumn)
        else:
            raise Exception("url Wrong!!")
        responseDict[responsecolumn] = resultDic
        responseJson = json.dumps(responseDict)
        return responseJson
    except Exception:#有必要参数未填
        resultDic = {}
        resultDic['code'] = '40001'
        errmsg = traceback.format_exc()
        sub_msg = errmsg[errmsg.find("\nException: missing")+ 12 : len(errmsg) -1]
        resultDic['sub_msg'] = sub_msg
        resultDic['msg'] = 'request parameter error'
        #responsecolumn = method.replace('.','_') + '_response'
        responseDict[responsecolumn] = resultDic
        responseJson = json.dumps(responseDict)
        print(responseJson)
        return responseJson