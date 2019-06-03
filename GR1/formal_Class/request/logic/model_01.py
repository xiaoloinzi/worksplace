# encoding=utf-8
import json
import requests
from flask import Flask
import random
import os

def userExist(username):
    flag = 0
    with open('model.txt','a+') as fp:
        line = fp.readlines()
        for i in line:
            if i.startswith(username):
                flag = 1
                break
    return flag

def register(username,userpwd):
    flag = userExist(username)
    if flag == 0:
        with open('model.txt','a+') as fp:
            fp.write(username+","+userpwd)
        return {"message":"register success","status":0,"usertel":username,"userpwd":userpwd}
    else:
        return json.loads('{"message":"user has registered,user name is '+username+'","status":1}')


def userExist_login(username,userpwd):
    flag = 0
    with open("model.txt",'a+') as fp:
        linew = fp.readlines()
        for i in linew:
            if i.startswith(username+","+userpwd):
                flag = 1
                break
    return flag

def login(username,userpwd):
    flag = userExist_login(username,userpwd)
    if flag==1:
        return {"message":"login success","status":0,"usertel":username,"userpwd":userpwd}
    else:
        return json.loads('{"message":"user has not registered,user name is '+username+'","status":1}')
























