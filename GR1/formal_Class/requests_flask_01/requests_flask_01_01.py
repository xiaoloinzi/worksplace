# encoding=utf-8
from flask import Flask,jsonify,Response,make_response,request, send_file,abort
import time

app =Flask(__name__)
# methods==可以随便定义，只是用不了
@app.route("/getCookies",methods=["get","post","put","delete","patch"])
def testCookies():

    mr = make_response(jsonify({"message":"getCookies success"}))

    mr.set_cookie("cookiesName","cookiesValue")
    mr.set_cookie("cookiesName1","cookiesValue1")
    return mr

@app.route("/getMyParams",methods=["get"])
def getMyParams():

    # 获取参数
    print request.args
    param1 = request.args.get("param1")
    print request.url

# http://127.0.0.1:80/getMyParams?param1=param11&param1=param11
#     方法一
    praram = request.args.items("param1")
    # 方法二
    url = str(request.url)
#     字符串切割[起始位置:]
    url = url[url.find("?")+1:]
    print "first:",url
    # 使用split进行切割：
    urlList = url.split("&")
    print "second:",urlList
    # 使用循环进行遍历
    userList = []
    for i in range(len(urlList)):
        value = urlList[i]
        userList.append(value.split("=")[1])
        print value.split("=")[1]
    return jsonify({"result":[userList[0],userList[1]]})
# def testHead():
#     res = req
# 上传文件带文件的以表单的形式上传
#接收上传的文件
#步骤:
#     1.获取文件对象，request.files[文件的key]
#     2.存储文件对象,文件.save方法存储文件

@app.route("/upload",methods=["post"])
def upload():
    # 获取文件
    file = request.files["fileName"]
    # 通过表单的形式去传递数据以及服务端获取数据
    praram = request.args.items("testDate")#--有问题？

    data = request.form
    for key,value in data.items():
        print key,":",value
    file.save("testupload.txt")
    return jsonify({"message":"upload seccess","data":data})
# 自己实现多文件存储，需要解析多个文件

# 多个文件接收
@app.route("/uploads",methods=["post"])
def uploads():
    # 获取文件
    file = request.files
    listFiles = []
    # 通过字典方式去遍历
    for i,j in file.items():
        print j.filename#可以查看文件名称
        # 存储文件
        if str(j.filename).endswith(".txt"):
            j.save("new"+str(j.filename))
        # j.save("testupload"+str(i)+".txt")
        else:
            listFiles.append(j.filename)
            continue
    # 返回响应
    return jsonify({"message":"upload seccess","failed files is:":listFiles})

# 下载
@app.route("/download",methods=["get"])
def download():
    # 获取文件
    fileName = request.args.get("filename")
    # 构造返回的消息
    file = send_file(fileName)
    mr = make_response(file)
    return mr

@app.route("/downloadStream",methods=["get"])
def downloadStream():
    # 可以尝试自己使用with再写一遍
    # 第三种可以
    fileName = request.args.get("fileName")
    fp = open(fileName,'rb')
    response = make_response(fp.read())
    fp.close()
    return response
    '''第一种可以
    fileName = request.args.get("fileName")
    fp = open(fileName,'rb')
    response = Response(fp.read())#
    fp.close()
    return response
'''
'''第二种不可以
    fileName = request.args.get("fileName")
    fp = open(fileName,'rb')
    response = make_response(send_file(fp.read()))#返回会报错
    fp.close()
    return response
'''
# errorhandler(code/excption object)
# 自定义异常
@app.errorhandler(500)
def testError500(message):
    print message
    mr = make_response(jsonify({"message":"the length of userName must be 1 to 5"}))
    # 设置返回的status_code--可以修改客户端的code值
    mr.status_code = 500
    return mr

@app.errorhandler(400)
def testError400(message):
    print message
    mr = make_response(jsonify({"message":"username is not null"}))
    # 设置返回的status_code--可以修改客户端的code值
    mr.status_code = 400
    return mr

@app.route("/login",methods=["post"])
def login():
    result = ""
    # 获取参数
    userName = request.args.get("userName")
     # 比较参数
    if userName==None or userName=="":
        abort(400)#使用abort触发异常
    elif len(userName) > 5:
        abort(500)
    # 返回结果
    return jsonify(result)
#
# 目的：1、返回错误响应，提示服务端异常
# 2、需要返回对应的错误码
@app.route("/login2",methods=["post"])
def login2():
    result = ""
    # 获取参数
    userName = request.args.get("userName")
     # 比较参数
    if userName==None or userName=="":
        abort(400)#使用abort触发异常
    elif len(userName) > 5:
        abort(500)
    # 返回结果
    return jsonify(result)

# 自定义异常
# 1、自定义一个异常类继承Exception MyException(Exception)
# 2、初始化方法__init__(错误消息)
# 3、定义一个返回错误消息的方法

class MyException(Exception):
    def __init__(self,result):
        self.result = result

    def returnResult(self):
        return {"message":self.result}

# 2、将异常加载到errorhandle中
@app.errorhandler(MyException)
def testMyException(myException):
    return jsonify(myException.returnResult())
# 3、触发异常
@app.route("/testMyException",methods=["post"])
def testMyException():
    # 设置模拟超时
    time.sleep(6)
#     触发异常
    raise MyException("test0827 my excetion,the servier is offline")

# 返回客户端使用的类型
@app.route("/testPath",methods=["post"])
def testPath():
    message = ""
    method = request.method
    if method == "POST":
       message = "post"
    if method == "PUT":
        message = "put"
    return jsonify({"message":message})

@app.route("/testPath/<path>",methods=["post"])
def testPath1(path):
    message = ""
    method = request.method
    if path == "path1":
        message = "path1"
    if path == "path2":
        message = "path2"
    return jsonify({"message":message})

if __name__=="__main__":
    app.run(host='127.0.0.1',port=80,debug=True)














