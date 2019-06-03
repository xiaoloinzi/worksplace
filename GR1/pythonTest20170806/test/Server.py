# encoding=utf-8
from flask import Flask,jsonify,request,make_response,send_file,Response,abort
import  os
import  time
app = Flask(__name__)
 #配置后可以返回中文信息
app.config['JSON_AS_ASCII'] = False
@app.route("/test0827",methods=["get"])
def test():
    return jsonify({"message":"test0827 success"})

@app.route("/getCookies",methods=["get","POST","put","patch"])
def testCookies():
    #自定义请求
    mr = make_response(jsonify({"message":"getCookies sucess"}))
    mr.set_cookie("cookiesName","cookiesValue") #设置cookies
    return mr
@app.route("/getMyParams",methods=["get"])
def getMyParams():
    #获取参数url:http://127.0.0.1:8888/getMyParams?param1=param11&param1=param11
    url = str(request.url)
    print request.args
    #字符串切割[起始位置：]
    url = url[url.find("?")+1:]
    #使用split进行切割
    urlList = url.split("&")
    #使用循环去遍历
    listTmp =[]
    for i in range(len(urlList)):
        value = urlList[i]
        print value.split("=")[1]
        listTmp.append(value.split("=")[1])
    print "second:",urlList
    print "first:",url
    return jsonify({"result":listTmp})
#接收上传的文件
#步骤:
#     1.获取文件对象，request.files[文件的key]
#     2.存储文件对象,文件.save方法存储文件
@app.route("/upload",methods=["post"])
def upload():
    #获取
    file = request.files["fileName"]
    data = request.form
    print "data",data
    #保存
    file.save(os.getcwd()+"\\test1Upload.png")
    #响应
    return jsonify({"message":"upload success","data":data})

@app.route("/uploads",methods=["post"])
def uploads():
    #获取文件
    files = request.files
    print files.items()
    #通过字典方式去遍历
    listFiles = []
    for key,value in files.items():
        print value.filename #获取文件名称包括后缀名
        if str(value.filename).endswith(".png"):
            value.save(os.getcwd()+"\\new"+value.filename)
        else:
            listFiles.append(value.filename)
            continue
    #实现存储文件
    #返回响应
    return jsonify({"message":"upload success","failed files":listFiles})

@app.route("/download",methods=["get"])
def download():
    #读文件名称
    fileName = request.args.get("fileName")
    #构造相应的返回消息
    file = send_file(os.getcwd()+"\\"+fileName)
    print "file type",type(file)
    response = make_response(file)#自定义响应
    return response #返回自定义响应

@app.route("/downloadStream",methods=["get"])
def downLoadStream():
    #读文件名称
    fileName = request.args.get("fileName")
    print os.getcwd()+"\\"+fileName
    #获取文件流
    with open(os.getcwd()+"\\"+fileName,"rb") as f :
        content = f.read()
    # response = Response(content)#自定义响应,正常
    response = make_response(content) #自定义响应,正常
    # response = make_response(send_file(content)) #这种会报错
    return response #返回自定义响应

#自定义异常
@app.errorhandler(400)#errorhandler(code/exeception object)
def testError400(abc):
    print abc
    mr = make_response(jsonify( {"message":"the length of userName must be 1 to 5"}))
    mr.status_code=400
    return mr
@app.errorhandler(500)#errorhandler(code/exeception object)
def testError500(message):
    print message
    mr = make_response(jsonify( {"message":"the server is offline"}))
    mr.status_code=500
    return mr

@app.route("/login",methods=["post"])
def login():
    #获取参数
    userName = request.args.get("userName")
    #比较参数
    if userName == None or userName =="":
        abort(400) #使用abort触发异常
    elif len(userName) >5:
        abort(400)
    return jsonify({"result":"success"})
#目的：1.返回错误响应，提示服务端异常
#      2.需要返回对应的错误码
@app.route("/login2",methods=["post"])
def login2():
    #获取参数
    userName = request.args.get("userName")
    #比较参数
    if userName == None or userName =="":
        abort(500) #使用abort触发异常
    elif len(userName) >5:
        abort(500)
    return jsonify({"result":"success"})

#1.自定义异常类
#   1.自定义一个异常类继承Exception  MyExcepton(Excepiton)
#   2.初始化方法 __init__(错误消息)
#   3.定义一个返回错误消息的方法（字典类型）
class MyException(Exception):
    def __init__(self,message):
        self.message = message
    def getResult(self):
        return {"message":self.message}
#2.将异常加载到errorhandler中
@app.errorhandler(MyException)
def testMyError(myException): #myExcepion为实例化的对象
    #获取异常结果
    return jsonify(myException.getResult())
#3.触发异常
@app.route("/testMyException",methods=["post"])
def testMyException():
    time.sleep(6)
    #触发异常
    message = "test0827 my exception, the server is offline"
    raise MyException(message)

@app.route("/testPath",methods=["post","put"])
def testPath():
    message = ""
    method = request.method
    if method == "POST":
        print "post" #处理post业务
        message = "post"
    if method == "PUT":
        print "put" #处理put
        message = "put"
    return  jsonify({"message":message})

#url: http://127.0.0.1:8888/userManage/addUser?k1=v1&k2=v2
#url: http://127.0.0.1:8888/userManage/updateUser?k11=v11
#url:http://127.0.0.1:8888/userManage/deleteUser?k22=v22
@app.route("/testPath/<path>/<path2>",methods=["post","put"])
def testPath2(path,path2):
    message = ""
    if path == "path1" and path2 == "path11":
        message = "path1 path11"
    if path == "path2" and path2 == "path22":
        message = "path2 path22"
    return  jsonify({"message":message})










if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)