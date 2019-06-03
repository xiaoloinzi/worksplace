# -*- coding: utf-8 -*-
import Queue,time,threading,json,requests,traceback,random,os
from util.Alipay.common import ConifgHelper,Validate
from util.Alipay.common import DataHelper
from util.Alipay.common import SignHelper

#初始化信息
def init(configFile,dataFile):
       ConifgHelper.initConfig(configFile)
       DataHelper.loadConfigFile(dataFile)

def notifyPayResult(notifyRequestDict):
    # 下单后需等待的时长
    delaySeconds = notifyRequestDict["notify_delay_time"]
    # -1时不通知
    if delaySeconds == -1:
        return
    time.sleep(delaySeconds)
    notify_type = notifyRequestDict["notify_type"]
    notify_url =  notifyRequestDict["notify_url"]
    del notifyRequestDict["notify_delay_time"]
    del notifyRequestDict["notify_url"]
    del notifyRequestDict["notify_type"]
    notifyRequestDict["sign"] = SignHelper.SignHelper().BuildDataSign(notifyRequestDict)
    if str(notify_type).lower() == "get":
        r = requests.get(notify_url,params=notifyRequestDict)
    if str(notify_type).lower() == "post":
        r = requests.post(notify_url,params=notifyRequestDict)
    if str(notify_type).lower() == "put":
        r = requests.put(notify_url,params=notifyRequestDict)
    if str(notify_type).lower() == "delete":
        r = requests.delete(notify_url,params=notifyRequestDict)
    print r.content
    return r
def alipay_trade_precreate(contentDict,responsecolumn):
    # 必填字段校验，没有时直接异常返回
    keys = ["out_trade_no","total_amount","subject"]
    Validate.validate(contentDict,keys)
    # 组装返回的消息
    if ConifgHelper.aliPayConfigInfo["responseFromFile"] != True:
        resultDict = {}
        # resultDict['code'] = '40004'
        # resultDict['msg'] = 'Business Failed'
        resultDict['code'] = '10000'
        resultDict['msg'] = 'SUCCESS'
        # resultDict['sub_code'] = 'ACQ.SYSTEM_ERROR'
        # resultDict['sub_msg'] = 'Business Failed'
        resultDict['out_trade_no'] = contentDict['out_trade_no']
        resultDict['qr_code'] = 'https://qr.alipay.com/bavh4wjlxf12tper3a'
    else:
        with open(os.getcwd()+"\\util\\Alipay\\data\\response\\"+responsecolumn+"_response.json","r") as f:
            resultDict = json.load(f)
    #返回消息
    return resultDict
def alipay_trade_pay(contentDict,responsecolumn):
    # 必填字段校验，没有时直接异常返回
    keys = ["out_trade_no","scene","auth_code","subject"]
    Validate.validate(contentDict,keys)
    # 组装返回消息
    if ConifgHelper.aliPayConfigInfo["responseFromFile"] != True:
        resultDict = {}
        resultDict['code'] = '10003'
        resultDict['trade_no'] = str(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))) + str(
            random.randint(0, 99999999999999)).zfill(14)  # 支付宝服务生成的订单号
        resultDict['msg'] = 'Success'
        resultDict['out_trade_no'] = contentDict['out_trade_no']
        resultDict['total_amount'] = contentDict['total_amount']
        resultDict['receipt_amount'] = contentDict['total_amount']
        fund_bill_list = {}
        fund_bill_list['buyer_user_id'] = '2088' + str(random.randint(1, 999999999999))
        fund_bill_list['discount_goods_detail'] = None
        resultDict['fund_bill_list'] = fund_bill_list
    else:
        with open(os.getcwd()+"\\util\\Alipay\\data\\response\\"+responsecolumn+"_response.json","r") as f:
            resultDict = json.load(f)
     # 异步通知
    with open(os.getcwd() + "\\util\\Alipay\\data\\response\\" + responsecolumn + "_request.json", "r") as f:
        notifyRequestDict = json.load(f)
    r = notifyPayResult(notifyRequestDict)
    #可处理请求
    return  resultDict