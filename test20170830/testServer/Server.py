# encoding=utf-8
from flask import Flask,request
import time

app = Flask(__name__)


@app.route('/login',methods=["get"])
def login():
    userName = request.args.get("userName")
    userPwd = request.args.get("userPwd")
    if userName == "test" and userPwd == "test":
        time.sleep(2)
        return '{"errorCode":0,"token":"test","status":0,"errorCode":0,"errorCode":0}'
    else:
        time.sleep(2)
        return '{"message":"login failed","status":1}'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8888,debug=True)