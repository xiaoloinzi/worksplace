# encoding=utf-8
import random
from flask import Flask,request,jsonify,make_response
import os
import requests
from logic import Common

app = Flask(__name__)

# 登陆的url:htt://127.0.1.1:80/register?userName=test0827.txt&userPwd=test0827.txt
@app.route("/register",methods=["POST"])
def register():#注册方法
    # 获取注册的参数
    header = request.headers
    print header
    if cmp(header["Content-Type"],"application/json") !=0:
        return jsonify({"message":"header is wrong to register","status":1})
    userName = request.args.get("userName")
    userPwd = request.args.get("userPwd")
#     处理业务逻辑，注册的业务
#     with open(os.getcwd()+"\\data\\register.txt","a+") as fp:
#         fp.write(userName+","+userPwd)
    result = Common.regiger(userName,userPwd)
#     构造响应结果消息：
    mr = make_response('{"message":"user registered success ","status":0}')
    mr.headers['Content-Type'] ='abc/asd'

#     消息返回
    return mr

@app.route("/login",methods=["POST"])
def login():
    header = request.headers
    print header
    if cmp(header["Content-Type"],"application/json") !=0:
        return jsonify({"message":"header is wrong to login","status":1})
    userName = request.args.get("userName")
    userPwd = request.args.get("userPwd")
    result = Common.login(userName,userPwd)
    ms = make_response(str(result))
    ms.headers["Server"]='abc/23'
    return  ms

if __name__=="__main__":
    app.run(host='127.0.0.1',port=80,debug=True)
















