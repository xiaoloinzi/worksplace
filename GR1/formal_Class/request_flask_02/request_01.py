# encoding=utf-8

from flask import Flask,json,jsonify,request,make_response
from flask.ext.httpauth import HTTPBasicAuth


# 安装pip install flask-httpauth

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
# 获取auth对象
auth = HTTPBasicAuth()

@auth.get_password
def getPassword(userName):
    if userName == "testUaerName":
        return  "testUserPwd"
    return None

@auth.error_handler
def authFailed():
    return make_response(jsonify({"error":"auth failed"}),401)




@app.route("/login",methods=["post","get"])
@auth.login_required
def login():
    cookie = request.cookies
    cookieValue = cookie.get("cookieValue")
    if cookieValue != "cookieValue":
        return  jsonify({"message":"get cookies wrong","status":0})
    # 获取header，判断header中的key为test，值为test
    re = request.headers["TEst"]
    if re == "test0827":
        return  jsonify({"message":"get header success","status":1})



    return  jsonify({"message":"get header failed","status":0})

if __name__=="__main__":
    app.run(host="127.0.0.1",port=80,debug=True)










































