# -*- coding: utf-8 -*-

from flask import Flask,request,jsonify,json
import requests
import Cookie


def resigter():
    param = {"userName":"18320455323","userPwd":"123456"}
    l = requests.get("http://127.0.0.1:8080/resigter",params=param,)
    print l.content


def login():
    # 2.实现cookis的判断，客户端传入cookies，服务端校验cookies正确性
    param = {"userName":"18320125321","userPwd":"123456"}
    cookie = {"name":"lin","pass":"xiao"}
    l = requests.get("http://127.0.0.1:8080/login",params=param,cookies=cookie)
    print l.content

# 3.自己实现一个put方法，修改用注册信息，修改密码
def updata():
    param = {"userName":"18320125321","userPwd":"123456","newPwd":"654321"}
    l = requests.put("http://127.0.0.1:8080/updeta",params=param)
    print l.content

# 4.自己实现一个delete方法，注销用户信息
def delete():
    param = {"userName":"18320455323","userPwd":"123456"}
    l = requests.delete("http://127.0.0.1:8080/delete",params=param)
    print l.content

if __name__=="__main__":
    updata()
    delete()
    login()

