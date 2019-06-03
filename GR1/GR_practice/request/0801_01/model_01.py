# -*- coding: utf-8 -*-

from flask import request,jsonify,Flask
import random

def userExist_resiger(username):
    flag = 0
    with open("file.txt",'a+') as fp:
        for i in fp.readlines():
            if i.startswith(username):
                flag = 1
                break
    return flag


def resiger(username,userpwd):
    flag = userExist_resiger(username)
    if flag == 0:
        with open("file.txt","a+") as fp:
            fp.write(username+","+userpwd+"\n")
        return {"massage":"resiger success","status":0,"username":username}
    else:
        return {"massage":"resiger failed","status":1,"username":username}


def userExist_login(username,userpwd):
    flag = 0
    with open("file.txt","a+") as fp:
        for i in fp.readlines():
            if i.startswith(username+","+userpwd):
                flag = 1
                break
    return flag

def login(username,userpwd):
    flag = userExist_login(username,userpwd)
    token = random.randint(1,10000)
    if flag == 1:
        with open("file.txt","a+") as fp:
            lines = fp.readlines()
            for i in xrange(len(lines)):
                if lines[i].startswith(username+","+userpwd):
                    lines[i] = lines[i].strip()+","+str(token)
                    break
        with open("file.txt","w") as fp:
            for j in lines:
                fp.write(j)
        return {"massage":"login success","status":0,"username":username,"token":token}
    else:
        return {"massage":"login failed","status":1,"username":username}


def userExist_updata(username,userpwd):
    flag = 0
    with open("file.txt","a+") as fp:
        for i in fp.readlines():
            if i.startswith(username+","+userpwd):
                flag = 1
                break
    return flag
# 3.自己实现一个put方法，修改用注册信息，修改密码
def updata(username,userpwd,newpwd):
    flag = userExist_login(username,userpwd)
    token = random.randint(1,10000)
    if flag == 1:
        with open("file.txt","a+") as fp:
            lines = fp.readlines()
            for i in xrange(len(lines)):
                if lines[i].startswith(username+","+userpwd):
                    lines[i] = username+","+newpwd+","+str(token)+"\n"
                    break
        with open("file.txt","w") as fp:
            for j in lines:
                fp.write(j)
        return {"massage":"updata success","status":0,"username":username,"newpwd":newpwd}
    else:
        return {"massage":"updata failed","status":1,"username":username}

def userExist_delete(username,userpwd):
    flag = 0
    with open("file.txt","a+") as fp:
        for i in fp.readlines():
            if i.startswith(username+","+userpwd):
                flag = 1
                break
    return flag

# 4.自己实现一个delete方法，注销用户信息
def delete(username,userpwd):
    flag = userExist_login(username,userpwd)
    if flag == 1:
        with open("file.txt","a+") as fp:
            lines = fp.readlines()
            for i in xrange(len(lines)):
                if lines[i].startswith(username+","+userpwd):
                    del lines[i]
                    break
        with open("file.txt","w") as fp:
            for j in lines:
                fp.write(j)
        return {"massage":"delete success","status":0,"username":username}
    else:
        return {"massage":"delete failed","status":1,"username":username}