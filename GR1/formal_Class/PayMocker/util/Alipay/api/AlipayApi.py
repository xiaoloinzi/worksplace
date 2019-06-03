# encoding=utf-8
import json

from flask import Flask,request,jsonify

from GR1.formal_Class.PayMocker.util.Alipay.logic import AlipayLogic


app = Flask(__name__)


# 在alipay_trade_precreate中完成消息的调用，
# 以及app的启动在alipay_trade_precreate中完成消息的调用，
# 以及app的启动
# @app.route("/gateway.do/alipay.trade.precreate",methods=["post"])
def alipay_trade_precreate():
    resposennum = json.loads(request.args.get("biz_content"))
    resposen = AlipayLogic.alipay_trade_precreate()
    print resposennum
    if cmp(resposennum['body'],"Iphone6 16G") != 0:
        return jsonify({"message":"fail","status":0})
    return json.dumps(resposen,indent=2)

# @app.route("/gateway.do/alipay.trade.pay",methods=["post"])
def alipay_trade_pay():
    resposennum = json.loads(request.args.get("biz_content"))
    resposen = AlipayLogic.alipay_trade_precreate()
    print resposennum
    if cmp(resposennum['seller_id'],"2088102146225135") != 0:
        return jsonify({"message":"fail","status":0})
    return json.dumps(resposen,indent=2)

@app.route("/gateway.do/<func>",methods=["post"])
def getfunc(func):
    try:
        if func=="alipay.trade.pay":
            result = alipay_trade_pay()
        if func == "alipay.trade.precreate":
            result = alipay_trade_precreate()
        return result
    except Exception as e:
        return {"massage":e}

if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)












