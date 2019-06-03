# coding=utf-8
from flask import Flask,request,jsonify,make_response
import os

app=Flask(__name__)     #实例化应用

# 【练习】怎么拿到返回的cookies
# 使用options方法，获取服务端的访问类型，在服务端新增一个访问类型
@app.route("/getCookies",methods=["get","put","delete","patch"])    #get的话会带这两个HEAD,OPTIONS
def testCookies():
    #自定义请求
    mr = make_response(jsonify({"message":"getCookies sucess"}))
    mr.set_cookie("cookiesName","cookiesValue")
    return mr

# 参数重复怎么处理？(有传多个Key情况)
@app.route("/getMyParams",methods=["get"])
def getMyParams():
    #获取参数url:http://127.0.0.1:8888/getMyParams?param1=param11&param1=param11
    url = str(request.url)
    #字符串切割[起始位置：]
    url = url[url.find("?")+1:]
    #使用split进行切割
    urlList = url.split("&")
    #使用循环去遍历
    for i in range(len(urlList)):
        value = urlList[i]
        print value.split("=")[1]
    print "second:",urlList
    print "first:",url
    return  jsonify({"result":"success"})

#接收上传的文件
#步骤:
#     1.获取文件对象，request.files[文件的key]
#     2.存储文件对象,文件.save方法存储文件
# 接收上传的文件
@app.route("/upload",methods=["post"])
def upload():
# 习题：通过表单的形式去传递数据以及服务端获取数据
# 获取文件对象
    file=request.files["fileName"]
    data=request.form
    print "data",data
# 保存
    file.save(os.getcwd()+"\\testUpload.png")
    # return jsonify({"message":"upload success"})
    return jsonify({"message":"upload success","data":data})


if __name__=="__main__":
    app.run(host="127.0.0.1",port=80,debug=True)








