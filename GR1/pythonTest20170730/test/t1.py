# encoding=utf-8
from flask import Flask,request,jsonify,make_response
from  logic import  Common
import  time

#实例化应用
app = Flask(__name__)
#配置应用(接口)
#注册url：http://127.0.1.1:80/register?userName=test0827.txt&userPwd=test0827.txt
#注册的方法类型：POST
@app.route("/register",methods=["POST","PUT","GET","DETELE"])
def register():#注册方法
    header = request.headers
    if cmp(header["Content-Type"],"application/json") !=0:
        return jsonify({"message":"header is wrong","status":1})
    #获取注册的参数
    userName = request.args.get("userName")
    userPwd = request.args.get("userPwd")
    #处理注册的业务,并返回结果
    result = Common.regiger(userName,userPwd)
    #构造响应结果消息
    # mr = make_response(result)
    mr = make_response('{"message":"user register success","status":0}')
    mr.headers["Content-Type"] = "abc/abc"
    mr.headers["Server"] = "abc"
    # mr.cookies["cookiesName"] ="abcabc"
    #消息返回
    return mr
    # return  jsonify(result)
# 1）定义登录方法，并指定访问的接口类型(post)和路径
# 2）获取参数（手机号，密码）
# 3）生成随机数，作为一个token
# 4）将token保存在文件中，token需要加入到注册信息的后面(手机号,密码，token)
# 5）用户名和密码正确返回登录成功，错误返回提示

@app.route("/login",methods=["POST"])
def login():
    header = request.headers
    if cmp(header["Content-Type"],"application/json") !=0:
        return jsonify({"message":"header is wrong","status":1})
    userName = request.args.get("userName")
    userPwd = request.args.get("userPwd")
    #实现业务
    result = Common.login(userName,userPwd)
    #返回结果
    return jsonify(result)
#启动应用
if __name__ =='__main__':
   app.run(host='127.0.0.1',port=80,debug=True)
