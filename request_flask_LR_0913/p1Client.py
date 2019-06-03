# encoding=utf-8
import requests
import os

# 添加内容
imageRootPath = os.getcwd()+"\\image"

def login():
    param = {"userName":"18320308441","userPwd":"123456"}
    r = requests.get("http://127.0.0.1:8888/login",params=param)
    print r.text

def testloginContent():
    params = {"contentValue":"我的第一个帖子"}
    file = {"file":open(imageRootPath+"\\test.png",'rb')}
    r = requests.post("http://127.0.0.1:8888/addContent",params=params,files=file)
    print r.text

def testaddContent():
    params = {"contentToken":2445}
    file = {"file":open(imageRootPath+"\\test.png",'rb')}
    r = requests.post("http://127.0.0.1:8888/addContent",params=params)
    print r
    print r.text
# 查询内容
def testqueryContent():
    params = {"contentId":6}
    r = requests.get("http://127.0.0.1:8888/queryContent",params=params)
    print r.json()


# 删除内容
def testdeleteContent():
    params = {"contentId":14}
    r = requests.delete("http://127.0.0.1:8888/deleteContent",params=params)
    print r.text


if __name__=="__main__":
    # login()
    # testaddContent()
    # testqueryContent()
    testdeleteContent()












