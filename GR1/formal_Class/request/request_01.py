# encoding=utf-8

import flask
from flask import Flask,request,jsonify
import requests

# 实例化应用
app = Flask(__name__)
# 防止中文乱码
app.config["JSON_AS_ASCII"]=False
print __name__
# 配置应用(接口)

# 定义方法：
# 定义一个测试接口
@app.route("/login",methods=["GET"])#methods=可以有多个值
def test():

    userName = request.args.get("userName")
    userPwd = request.args.get("userPwd")
    # http://127.0.0.1/login?userName=test0827.txt&userpwd=123456
    # 手动在浏览器输入：?userName=test0827.txt&userpwd=123456。判断是否符合，
    # 符合输出，不符合输出另外的返回值
# 练习1：
# 1.启动一个flask服务，实现用户名和密码登录，判断用户名和密码
# 是否正确，正确返回登录成功，错误返回登录失败
#     老师的方法：
#     判断用户名和密码是否正确
    if userName=="test0827.txt"and userPwd=="123456":
        # 中文转码
        name = "用户名:".decode('utf-8')
        return "test0827.txt login success:"+ name+ userName+":"+userPwd
        return jsonify({"message":"login success","status":0})#返回接送格式

    else:
         return "test0827.txt login flail"

# 1、编写一个用户注册的场景
#     1.服务端：注册成功的返回响应（json）
#     2.客户端进行访问
#     3.将注册信息保存在文件中
@app.route("/zc",methods=["GET"])#methods=可以有多个值
def test1():

    userName = request.args.get("userName")
    userPwd = request.args.get("userPwd")
    if userName==""and userPwd=="":
        pass

    else:
        result = {"message":"login success","status":0,"username":userName,"userpwd":userPwd}
        return jsonify({"result":result})


# 启动应用
if __name__=='__main__':
    # app.run(host=ip地址,port=端口,debug=是否为调试模式)
    app.run(host='127.0.0.1',port=80,debug=True)



















