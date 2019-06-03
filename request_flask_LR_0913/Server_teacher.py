# encoding=utf-8
from flask import Flask,request
import time
import thread


app = Flask(__name__)

@app.route("/login",methods=["post"])
def login():
    time.sleep(3)
    userName = request.args.get("userName")
    userPwd = request.args.get("userPwd")
    if str(userName).startswith( "test") and str(userPwd).startswith( "test"):
        return '{"token":"myToken","status":0}'
    else:
        return '{"status":1,"msg":"username or userpwd is wrong"}'


@app.route("/createResource",methods=["post"])
def createResource():
    time.sleep(3)
    token = request.args.get("token")
    if token == "myToken":
        return '{"resourceId":1,"status":0}'
    else:
        return '{"status":1,"msg":"token is wrong"}'


@app.route("/deleteResource",methods=["delete"])
def deleteResource():
    time.sleep(1)
    resourceId = request.args.get("resourceId")
    token = request.args.get("token")
    if token == "myToken":
        if int(resourceId) == 1:
            return '{"status":0,"msg":"delete success"}'
        else:
            return '{"status":1,"msg":"the resource not success"}'
    else:
        return '{"status":1,"msg":"token is wrong"}'



if __name__=="__main__":
    app.run(host="0.0.0.0",port=8888,debug=True,threaded=True)





















