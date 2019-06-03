# encoding=utf-8
from flask import Flask,request,jsonify,make_response
from  logic import  Common
import  time

#实例化应用
app = Flask(__name__)
#测试cookies

@app.route("/testCookies",methods=["GET"])
def testCookies():
    #获取cookies
    cookies = request.cookies
    if cookies is None:
        return  '{"message":"cookies is None"}'
    #判断cookies
    if cmp(cookies.get("testCookiesKey"),"testCookiesValue") == 0:
    # if cmp(cookies["testCookiesKey"],"testCookiesValue") == 0:
        #返回响应
        return '{"message":"cookies is right"}'
    else:
        return '{"message":"cookies is wrong"}'

#服务端：1.定义消息的入口，实现接口
        #2. a)获取消息 b)处理业务并获取返回消息 c)返回响应
                       #b1)判断修改的用户是否存在
@app.route("/updateUserPwd",methods=["PUT"])
def update():
    #获取参数
    userName = request.args.get("userName")
    userPwd = request.args.get("userPwd")
    newPwd = request.args.get("newPwd")
    #处理业务
    result = Common.updateUserPwd(userName,userPwd,newPwd)
    #返回响应
    return  jsonify(result)

#定义删除方法
@app.route("/deleteUser",methods=["delete"])
def delete():
    #获取参数
    userName = request.args.get("userName")
    userPwd = request.args.get("userPwd")
    #处理删除逻辑
    result = Common.delete(userName,userPwd)
    #返回响应
    return  jsonify(result)




#配置应用(接口)
#注册url：http://127.0.1.1:80/register?userName=test0827&userPwd=test0827
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
    # result = str(result) #字典类型转换字符串
    #构造响应结果消息
    mr = make_response(jsonify(result))#将响应对象传入到自定义响应中返回
    # mr = make_response('{"message":"user register success","status":0}')
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
