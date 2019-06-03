# -*- coding: utf-8 -*-
# 1.在flask服务端，将字典格式的数据转换成功自定义消息返回
# 2.实现cookis的判断，客户端传入cookies，服务端校验cookies正确性
# 3.自己实现一个put方法，修改用注册信息，修改密码
# 4.自己实现一个delete方法，注销用户信息
# 注意：put和delete方法的实现参考get和post，实现原理一样

from flask import Flask,request,jsonify
import model_01
import requests
import Cookie

app = Flask(__name__)

@app.route("/login",methods=["GET"])
def login():
    # 2.实现cookis的判断，客户端传入cookies，服务端校验cookies正确性
    print request.cookies
    if  request.cookies["name"] != "lin":
        return str({"massage":"cookies failed"})
    username = request.args.get("userName")
    userpwd = request.args.get("userPwd")
    result = model_01.login(username,userpwd)
    #自定义为字符串形式返回
    return str(result)

@app.route("/resigter",methods=["GET"])
def resigter():
    username = request.args.get("userName")
    userpwd = request.args.get("userPwd")
    result = model_01.resiger(username,userpwd)
    return str(result)

# 3.自己实现一个put方法，修改用注册信息，修改密码
@app.route("/updeta",methods=["PUT"])
def updata():
    username = request.args.get("userName")
    userpwd = request.args.get("userPwd")
    newpwd = request.args.get("newPwd")
    result = model_01.updata(username,userpwd,newpwd)
    return str(result)

# 4.自己实现一个delete方法，注销用户信息
@app.route("/delete",methods=["DELETE"])
def delete():
    username = request.args.get("userName")
    userpwd = request.args.get("userPwd")
    result = model_01.delete(username,userpwd)
    return str(result)



if __name__=="__main__":
    app.run(host="127.0.0.1",port=8080,debug=True)










