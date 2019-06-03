# encoding=utf-8
from flask import Flask,request,jsonify
import random
import os

def userExist(username):
    flag = 0
    with open('file1.txt','a+') as fp:
        lines = fp.readlines()
        for i in lines:
            if i.startswith(username):
                flag = 1
                break
    return flag

def rigester(username,userpwd):
    flag = userExist(username)
    if flag == 0:
        with open("file1.txt","a+") as fp:
            fp.write(username+","+userpwd+"\n")
        return {"massage":"rigester success","status":0,"username":username}
    else:
        return {"massage":"rigester failed ","status":1,"username":username}


def userExist_login(username,userpwd):
    flag = 0
    with open('file1.txt','a+') as fp:
        lines = fp.readlines()
        for i in lines:
            if i.startswith(username+","+userpwd):
                flag = 1
                break
    return flag

def login(username,userpwd):
    flag = userExist_login(username,userpwd)
    token = random.randint(100000000000000,999999999999999999)
    if flag == 1:
        with open("file1.txt","a+") as fp:
            lines = fp.readlines()
        with open("file2.txt","w") as fp:
            for i in lines:
                if i.startswith(username+","+userpwd):
                    stra = username+","+userpwd+","+str(token)+"\n"
                    fp.write(stra)
                else:
                    fp.write(i)
        with open("file2.txt","r") as fp:
            linesa = fp.readlines()
        with open("file1.txt","w") as ft:
            for i in linesa:
                ft.write(i)
        return {"massage":"login success","status":0,"username":username,"token":token}
    else:
        return {"massage":"login failed ","status":1,"username":username}



























