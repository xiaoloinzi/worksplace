# -*- coding: utf-8 -*-
from Common import ConfigHelper,DataHelper,Common
from Common.SignHelper import *
import traceback
import string
import json
import random
import time
import Queue
import threading
import urllib
from Common.FlaskHelper import *
from flask import request
import requests
from flask.ctx import _request_ctx_stack


app = FlaskHelper().app
unifiedorderuQueue = Queue.Queue(maxsize=0)

def StartNotifyTask():
    while True:
        if unifiedorderuQueue.empty():
            time.sleep(0.5)
            continue
        unifiedorderRequest = unifiedorderuQueue.get()
        #payResult = BuildPayResult(unifiedorderRequest)
        # 异步通知支付结果
        #task = threading.Thread(target=NotifyPayResult, args=(unifiedorderRequest.POST['notify_url'], payResult))
        task = threading.Thread(target=NotifyPayResult, args=(unifiedorderRequest,))
        task.setDaemon(True)
        task.start()

#def NotifyPayResult(url,payResult):
def NotifyPayResult(unifiedorderRequest):
    # 下单后需等待的时长
    # delaySeconds = random.uniform(5, 30)
    delaySeconds = ConfigHelper.GetNotifyDelay()
    # -1时不通知
    if delaySeconds == -1:
        return
    time.sleep(delaySeconds)
    reTryCount = 5
    while reTryCount > 0:
        try:
            #isReturn在configjson中如果为1表示返回，如果为其它值不返回
            if int(ConfigHelper.GetValue("isReturn")) == 1:
                notifyTimeoutIsReturn=1
                print("----------------------------------")
                print("begin to notify the message")
                method = unifiedorderRequest.args.get('method')
                responsecolumn = method.replace('.', '_') + '_response'
                notify_url = unifiedorderRequest.args.get('notify_url')
                sign_type = unifiedorderRequest.args.get('sign_type')
                appid = unifiedorderRequest.args.get('app_id')
                biz_content = unifiedorderRequest.args.get('biz_content')
                contentDict = json.loads(biz_content)
                out_trade_no = contentDict.get('out_trade_no')
                seller_id = contentDict.get('seller_id')
                total_amount = str(contentDict.get('total_amount'))
                subject = contentDict.get('subject')
                body = contentDict.get('body')
                serverTime = str(time.strftime("%Y-%m-%d+%H:%M:%S", time.localtime(time.time())))
                trade_no = str(time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))) + str(random.randint(0,99999999999999)).zfill(14)
                #获取返回的响应类型
                if str(responsecolumn) == "alipay_trade_precreate_response":
                    out_trade_no_success_begin = int(str(ConfigHelper.GetValue("out_trade_no_success")).split("-")[0])
                    out_trade_no_success_end = int(str(ConfigHelper.GetValue("out_trade_no_success")).split("-")[1])
                    out_trade_no_fail_begin = int(str(ConfigHelper.GetValue("out_trade_no_fail")).split("-")[0])
                    out_trade_no_fail_end = int(str(ConfigHelper.GetValue("out_trade_no_fail")).split("-")[1])
                    out_trade_no_timeout_begin = int(str(ConfigHelper.GetValue("out_trade_no_timeout")).split("-")[0])
                    out_trade_no_timeout_end = int(str(ConfigHelper.GetValue("out_trade_no_timeout")).split("-")[1])
                    precreateDict = {}
                    out_trade_no = int(out_trade_no)
                    if out_trade_no >= out_trade_no_success_begin and out_trade_no <= out_trade_no_success_end:
                        fileName = responsecolumn + "_notify_success.json"
                        precreateDict = DataHelper.getResponse(fileName)
                    elif out_trade_no >= out_trade_no_fail_begin and out_trade_no <= out_trade_no_fail_end:
                        fileName = responsecolumn + "_notify_fail.json"
                        precreateDict = DataHelper.getResponse(fileName)
                    elif out_trade_no >= out_trade_no_timeout_begin and out_trade_no <= out_trade_no_timeout_end:
                        fileName = responsecolumn + "_notify_timeout.json"
                        precreateDict = DataHelper.getResponse(fileName)
                        notifyTimeout = int(ConfigHelper.GetValue("notifyTimeout"))
                        time.sleep(notifyTimeout)
                        notifyTimeoutIsReturn =  int(ConfigHelper.GetValue("notifyTimeoutIsReturn"))
                    else:
                        print "out_trade_no is wrong"
                    if notifyTimeoutIsReturn == 1:
                        r = requests.post(notify_url, params=precreateDict)
                        print "alipay_trade_precreate [notify] request:",r.url
                        print "alipay_trade_precreate [notify] response:", r.content
                    else:
                        print "not [notify alipay_trade_precreate "
                else:
                    notifyResponse = DataHelper.getNotify("alipay_trade_pay_notify.json")
                    notifyResponse = Common.updateJsonObjByKey(notifyResponse, "out_trade_no", out_trade_no)
                    notifyResponse = Common.updateJsonObjByKey(notifyResponse, "notify_url", notify_url)
                    r = requests.post(notify_url,params=notifyResponse)
                    print "alipay_trade_pay [notify] request:", r.url
                    print "alipay_trade_pay [notify] response:",r.content
                print("end  notify the message")
                print("----------------------------------")
            return
        except Exception :
            errorMsg = traceback.format_exc()
            print(errorMsg)
            time.sleep(15)
            reTryCount -=1
            continue

@app.route('/gateway.do', methods=['POST'])
def Gateway():
    try:
        responseDict = {}
        method = request.args.get('method')
        responsecolumn = method.replace('.', '_') + '_response'
        charset = request.args.get('charset')
        sign = request.args.get('sign')
        sign_type = request.args.get('sign_type')
        timestamp = request.args.get('timestamp')
        app_id = request.args.get('app_id')
        version = request.args.get('version')
        biz_content = request.args.get('biz_content')
        contentDict = json.loads(biz_content)
        precreateDict = {}
        #复制请求
        ctx = _request_ctx_stack.top.copy()
        newRequest = ctx.request
        if method == 'alipay.trade.precreate': #统一收单线下交易预创建（扫码支付）
            #必填字段校验，没有时直接异常返回
            if(contentDict.get('out_trade_no') == None):
                raise Exception("missing an argument: \"out_trade_no\"")
            if(contentDict.get('total_amount')==None):
                raise Exception("missing an argument: \"total_amount\"")
            if(contentDict.get('subject') == None):
                raise Exception("missing an argument: \"subject\"")
            # 组装返回消息
            # h获取商户订单id
            out_trade_no = int(contentDict.get('out_trade_no'))
            fileName = responsecolumn + "_success.json"
            precreateDict = DataHelper.getResponse(fileName)
            # 将商务订单id替换成传入的值
            precreateDict = Common.updateJsonObjByKey(precreateDict, "out_trade_no", out_trade_no)
            unifiedorderuQueue.put(newRequest)
            #responseDict[responsecolumn] = precreateDict
        elif method == 'alipay.trade.pay':#条码支付
            #必填字段校验，没有时直接异常返回
            if (contentDict.get('out_trade_no') == None):
                raise Exception("missing an argument: \"out_trade_no\"")
            if (contentDict.get('scene') == None):
                raise Exception("missing an argument: \"scene\"")
            if (contentDict.get('auth_code') == None):
                raise Exception("missing an argument: \"auth_code\"")
            if (contentDict.get('subject') == None):
                raise Exception("missing an argument: \"subject\"")
            if (contentDict.get('total_amount') != None):
                total_amount = contentDict['total_amount']
            elif (contentDict.get('discountable_amount') != None):
                total_amount = contentDict['discountable_amount']
                if(contentDict.get('undiscountable_amount')!= None):
                    total_amount += contentDict['undiscountable_amount']
            elif (contentDict.get('undiscountable_amount') != None):
                total_amount = contentDict['undiscountable_amount']
            else:
                raise Exception("missing an argument: \"total_amount\" or \"discountable_amount\" or \"undiscountable_amount\"")
            #组装返回消息
            #h获取商户订单id
            out_trade_no = int(contentDict.get('out_trade_no'))
            out_trade_no_success_begin = int(str(ConfigHelper.GetValue("out_trade_no_success")).split("-")[0])
            out_trade_no_success_end = int(str(ConfigHelper.GetValue("out_trade_no_success")).split("-")[1])
            out_trade_no_fail_begin = int(str(ConfigHelper.GetValue("out_trade_no_fail")).split("-")[0])
            out_trade_no_fail_end = int(str(ConfigHelper.GetValue("out_trade_no_fail")).split("-")[1])
            out_trade_no_timeout_begin = int(str(ConfigHelper.GetValue("out_trade_no_timeout")).split("-")[0])
            out_trade_no_timeout_end = int(str(ConfigHelper.GetValue("out_trade_no_timeout")).split("-")[1])
            if out_trade_no >= out_trade_no_success_begin and out_trade_no <=out_trade_no_success_end:
                fileName = responsecolumn+"_success.json"
                precreateDict = DataHelper.getResponse(fileName)
                #将商务订单id替换成传入的值
                precreateDict = Common.updateJsonObjByKey(precreateDict,"out_trade_no",out_trade_no)
                # unifiedorderuQueue.put(newRequest)
            elif out_trade_no >=out_trade_no_fail_begin and out_trade_no <=out_trade_no_fail_end:
                fileName = responsecolumn+"_fail.json"
                precreateDict = DataHelper.getResponse(fileName)
            elif out_trade_no >=out_trade_no_timeout_begin and out_trade_no<= out_trade_no_timeout_end:
                fileName = responsecolumn+"_timeout.json"
                precreateDict = DataHelper.getResponse(fileName)
                timeout=int(ConfigHelper.GetValue("timeout"))
                time.sleep(timeout)
            else:
                raise Exception("out_trad_no not exist,the out_trade_no is: \"out_trade_no\"")
            print request.args.get("notify_url")
        elif method == 'alipay.trade.query':#统一收单线下交易查询
            #必填字段校验
            out_trade_no = contentDict.get('out_trade_no')
            trade_no = contentDict.get('trade_no')
            if(out_trade_no == None and trade_no == None):
                raise Exception("missing an argument: \"trade_no\" or \"out_trade_no\"")
            if(trade_no == None):#生成支付交易号
                trade_no = str(time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))) + str(random.randint(0,99999999999999)).zfill(14)
            if(out_trade_no == None):
                out_trade_no = str(random.randint(6000000000000000,6999999999999999))
            #组装返回消息
            precreateDict = {}
            precreateDict['code'] = '10000'
            precreateDict['msg'] = 'Success'
            precreateDict['out_trade_no'] = out_trade_no
            precreateDict['trade_no'] = trade_no
            precreateDict['buyer_logon_id'] = '159****5620'
            #i = random.randint(1,30)
            #if(i == 30):#1/30 closed
            #    precreateDict['trade_status'] = 'TRADE_CLOSED'
            #elif(i == 29 ):#1/30 finished
            #    precreateDict['trade_status'] = 'TRADE_FINISHED'
           # elif(i % 3 < 2):
            #    precreateDict['trade_status'] = 'WAIT_BUYER_PAY'
            #else:
            precreateDict['trade_status'] = 'TRADE_SUCCESS'
            send_pay_date= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            precreateDict['send_pay_date'] = send_pay_date
            precreateDict['total_amount'] = 13.00
            precreateDict['receipt_amount'] = '13.00'
            fund_bill_list = {}
            fund_bill_list['fund_channel'] = 'ALIPAYACCOUNT'
            fund_bill_list['amount'] = 13.00
            precreateDict['fund_bill_list'] = fund_bill_list
            precreateDict['buyer_user_id'] = '2088' + str(random.randint(1,999999999999))
            precreateDict['discount_goods_detail'] = None
        elif method == 'alipay.trade.cancel	':#统一收单交易撤销接口
            #必填参数校验
            out_trade_no = contentDict.get('out_trade_no')
            trade_no = contentDict.get('trade_no')
            if (out_trade_no == None and trade_no == None):
                raise Exception("missing an argument: \"trade_no\" or \"out_trade_no\"")
            if (trade_no == None):  # 生成支付交易号
                trade_no = str(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))) + str(
                    random.randint(0, 99999999999999)).zfill(14)
            if (out_trade_no == None):
                out_trade_no = str(random.randint(6000000000000000, 6999999999999999))
            #组装返回消息
            precreateDict = {}
            precreateDict['trade_no'] = trade_no
            precreateDict['out_trade_no'] = out_trade_no
            i = random.randint(1,10)
            if(i == 10):
                precreateDict['code'] = '40004'
                precreateDict['retry_flag'] = 'Y'
                precreateDict['msg'] = 'transaction process failed'
            else:
                precreateDict['code'] = '10000'
                precreateDict['retry_flag'] = 'N'
                precreateDict['msg'] = 'Success'
                if(i % 3 < 2):
                    precreateDict['action'] = 'close'
                else:
                    precreateDict['action'] = 'refund'
            #responseDict[responsecolumn] = precreateDict
        elif method == 'alipay.trade.refund':#统一收单交易退款接口
            #参数校验
            out_trade_no = contentDict.get('out_trade_no')
            trade_no = contentDict.get('trade_no')
            if (out_trade_no == None and trade_no == None):
                raise Exception("missing an argument: \"trade_no\" or \"out_trade_no\"")
            if (trade_no == None):  # 生成支付交易号
                trade_no = str(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))) + str(
                    random.randint(0, 99999999999999)).zfill(14)
            if (out_trade_no == None):
                out_trade_no = str(random.randint(6000000000000000, 6999999999999999))
            refund_amount = contentDict.get('refund_amount') #退款金额
            if(refund_amount == None):
                raise Exception("missing an argument: \"refund_amount\"")
            #组装返回消息
            precreateDict = {}
            precreateDict['trade_no'] = trade_no
            precreateDict['out_trade_no'] = out_trade_no
            # i = random.randint(1,20)
            # if(i == 20 ):#失败
            #     precreateDict['code'] = '40004'
            #     precreateDict['msg'] = 'transaction process failed'
            #     precreateDict['fund_change'] = 'N'
            # else:
            precreateDict['code'] = '10000'
            precreateDict['msg'] = 'Success'
            precreateDict['fund_change'] = 'Y'
            precreateDict['refund_fee'] = refund_amount
            precreateDict['gmt_refund_pay'] = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
            precreateDict['buyer_user_id'] = '2088' + str(random.randint(1,999999999999))

            #precreateDict['qr_code'] = 'https://qr.alipay.com/bavh4wjlxf12tper3a'
            #responseDict[responsecolumn] = precreateDict
        elif method == 'alipay.data.dataservice.bill.downloadurl.query':#查询对账单下载地址
            #参数校验
            if(contentDict.get('bill_type') == None):
                raise Exception("missing an argument: \"bill_type\"")
            if(contentDict.get('bill_date') == None):
                raise Exception("missing an argument: \"bill_date\"")
            #组装返回消息
            precreateDict = {}
            precreateDict['code'] = '10000'
            precreateDict['msg'] = 'Success'
            precreateDict['bill_download_url'] = 'http://dwbillcenter.alipay.com/downloadBillFile.resource?bizType=X&userId=X&fileType=X&bizDates=X&downloadFileName=X&fileId=X'

        elif method == 'monitor.heartbeat.syn':
            #参数校验
            if (contentDict.get('product') == None):
                raise Exception("missing an argument: \"product\"")
            if (contentDict.get('type') == None):
                raise Exception("missing an argument: \"type\"")
            if (contentDict.get('equipment_id') == None):
                raise Exception("missing an argument: \"equipment_id\"")
            if (contentDict.get('time') == None):
                raise Exception("missing an argument: \"time\"")
            if (contentDict.get('store_id') == None):
                raise Exception("missing an argument: \"store_id\"")
            if (contentDict.get('network_type') == None):
                raise Exception("missing an argument: \"network_type\"")
            if (contentDict.get('trade_info') == None):
                raise Exception("missing an argument: \"trade_info\"")
            #组装返回消息
            precreateDict = {}
            precreateDict['code'] = '10000'
            precreateDict['msg'] = 'Heart beat Synchronize Success'
        else:
            raise Exception("url Wrong!!")
        responseJson = json.dumps(precreateDict)
        if int(ConfigHelper.GetValue("isReturn")) == 1:
            return responseJson
        else:
            time.sleep(120)#停止120秒
    except Exception:#有必要参数未填
        precreateDict = {}
        precreateDict['code'] = '40001'
        errmsg = traceback.format_exc()
        sub_msg = errmsg[errmsg.find("\nException: missing")+ 12 : len(errmsg) -1]
        precreateDict['sub_msg'] = sub_msg
        precreateDict['msg'] = 'request parameter error'
        responseJson = json.dumps(precreateDict)
        print(responseJson)
        return responseJson