# encoding=utf-8
# 【20170813课后练习】
# 1.请设计一下接口测试用例，用边界值和等价类划分方法进行设计
# 接口名称 login
# 参数 类型 长度 是否为空 约束 备注
# userName String 11 not null 必须为手机号码 
# userPwd String 8-12 not null 至少包含一个大写字母，数字 
# 2.使用flask实现服务端的接口，要求在接口中实现上面的接口验证以及功能
# 3.使用resfulclient对接口进行测试和验证
from flask import Flask,jsonify,request,make_response
import os
from comm import logic
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/login",methods=["post","get"])
def login():
    username = request.args.get("username")
    userpwd = request.args.get("userpwd")
    result = logic.login('18834133049',"21111s2A12112192")
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=80,debug=True, threaded = True)