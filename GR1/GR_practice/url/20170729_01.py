# encoding=utf-8
import requests
import json
import flask
from flask import Flask,jsonify


# response = requests.get("http://www.baidu.com")
# print type(response)
# print u"响应返回的状态码："+str(response.status_code)
# assert response.status_code==200
# print u'user_url的值为：'+response.json()['user_url']
# print type(response.json()['user_url'])
# assert response.json()['user_url']==u'http://www.baidu.com/users/{user}'
# response = requests.get("https://api.github.com")
# print u'响应返回的状态码： ' + str(response.status_code)
# assert response.status_code == 200
# print u'user_url的值为： ' + response.json()['user_url']
# print type(response.json()['user_url'])
# assert response.json()['user_url'] == u'https://api.github.com/users/{user}'

# payload = {'key1':'value1','key2':'value2'}
# r = requests.get('http://www.baidu.com',params=payload)
# assert r.status_code==200
# print r.url
# print '-'*40
# print r.text
# print '-'*40
# try:
#     response = requests.get('http://www,baidu.com/get',timeout=0.001)
#     print response.status_code
# except Exception,e:
#     print e
# print '-'*40
#
# payload = {'key1':'value1','key2':'value2'}
# p = requests.post("http://www.baidu.com/post",data= payload)
# q = requests.post("http://www.baidu.com/post",json = json.dumps(payload))
# assert p.status_code == 200
# print p.url
# print '-'*40
# print p.text
#
# assert q.status_code==200
# print '-'*40
# print q.text

# url = "http://httpbin.org/post"
# files = {'file':open(r'E:\1.jpg','rb')}
# payload = {"name":"Lucy","sex":"male"}
# headers = {"content-type":"application/json"}
# r = requests.post(url,data=json.dumps(payload),headers=headers)
# print r.status_code
# print r.url
# for i in r:
#     print i

app = Flask(__name__)
# @app.route("/test0827.txt",methods=["GET"])
# def testHelloWorldHttp():
#     return "Hello world http！"
#
# if __name__=='__main__':
#     app.run('127.0.0.1',8888,debug = True)
#     app.run('127.0.0.1',8889,debug = True,ssl_context = 'adhoc')

@app.route('/register',methods=["POST"])
def register():
    telephoneNum = requests.args.get("telephonrNum")
    password = requests.args.get("password")
    result = Common.register(telephoneNum,password)
    return jsonify({"result":result})

param = {"telephonrNum":"18320308441","password":"123456"}
r = requests.post("http://localhost:8888/register",params=param)












