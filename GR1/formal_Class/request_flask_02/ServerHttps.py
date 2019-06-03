# encoding=utf-8
from flask import Flask,jsonify,request,make_response
import os
from flask.ext.httpauth import HTTPBasicAuth
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#获取auth对象
auth = HTTPBasicAuth()
@auth.get_password
def getPasswrod(userName):#用户名
    if userName == "testUserName":
        return "testUserPwd" #对应的密码
    return None
@auth.error_handler
def authFailed():
    return make_response(jsonify({"error":"auth failed ,username or password is wrong"}),401)

@app.route("/login",methods=["post","get"])
@auth.login_required #登录前进行验证
def login():
    cookies = request.cookies
    cookiesValue = cookies.get("cookiesValue")
    if cookiesValue != "cookiesValue":
        return jsonify({"message":"login failed cookies is wrong ","status":0})
    #获取header，判断header中的key为test，值为test，如果不等返回header失败
    value = request.headers.get("test0827")
    if value == "test0827":
        #获取data
        data = request.get_data()#获取数据
        with open(os.getcwd()+"\\testNew.png","wb") as f :
            f.write(data)
        return jsonify({"message":"login success","status":1})
    return jsonify({"message":"login failed header is wrong ","status":0})

@app.route("/testCert",methods=["get"])
def testCert():
    return jsonify({"message":"testCert is success","status":1})

if __name__ == '__main__':
    cert = os.getcwd()+"\\cert\\server.crt"
    key = os.getcwd()+"\\cert\\server.key"

    app.run(host='test0827.com',port=8889,debug=True, threaded = True,ssl_context = (cert,key))