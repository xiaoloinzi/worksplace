#encoding=utf-8
import json
import traceback
from flask import request
from common.FlaskHelper import *
from util.Alipay.logic import PayLogic

#运行过程中进行加载
app = FlaskHelper().app


@app.route('/notify',methods=["post"])
def notify():
    return '{"notify":"success","status":0}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8889, debug=True, threaded=True)