# encoding=utf-8
from flask import Flask,request,jsonify
import requests
#运行过程中进行加载
app = Flask(__name__)


@app.route('/tradePrecreate',methods=["post"])
def tradePrecreate():
    url = "http://127.0.0.1:8001/gateway.do"
    biz_content = request.args.get("biz_content")
    params = {"biz_content":biz_content,"notify_url":"http://127.0.0.1:8002/notify","method":"alipay.trade.precreate"}
    r = requests.post(url,params=params)
    print "[send alipay.trade.precreate message to alipay]:", r.content
    print "[receive alipay.trade.precreate message from alipay]:", r.content
    return jsonify(r.json())


@app.route('/tradePay',methods=["post"])
def tradePay():
    url = "http://127.0.0.1:8001/gateway.do"
    biz_content = request.args.get("biz_content")
    params = {"biz_content":biz_content,"notify_url":"http://127.0.0.1:8002/notify","method":"alipay.trade.pay"}
    r = requests.post(url,params=params)
    print "[send alipay.trade.pay message to alipay]:", r.content
    print "[receive alipay.trade.pay message from alipay]:",r.content
    return jsonify(r.json())

@app.route('/notify',methods=["post"])
def notify():
    result = '{"notify":"success","status":0}'
    print "[recevice notify message from alipay]: ",request.url
    print "[send result to  alipay]: ",result
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True, threaded=True)
