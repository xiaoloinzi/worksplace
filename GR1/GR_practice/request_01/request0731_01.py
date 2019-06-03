# encoding=utf-8
# 1.在flask服务端，将字典格式的数据转换成功自定义消息返回
# 2.实现cookis的判断，客户端传入cookies，服务端校验cookies正确性
# 3.自己实现一个put方法，修改用注册信息，修改密码
# 4.自己实现一个delete方法，注销用户信息
# 注意：put和delete方法的实现参考get和post，实现原理一样

from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/put",methods=["PUT"])
def put():
    pass


















