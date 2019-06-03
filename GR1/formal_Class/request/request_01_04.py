# encoding=utf-8
import random
from flask import Flask,request,jsonify
import requests

# htt://127.0.01:80/register?userName=test0827.txt&userPwd=test0827.txt
# 测试注册方法
def register():
    # 发送请求
    headers = {'Content-Type': 'application/json'}
    r = requests.post("http://127.0.0.1:80/register?userName=18320308446&userPwd=test0827.txt",headers=headers)
    # 打印结果
    print r.headers

    print r.text

def login():
    headers = {'Content-Type': 'application/json'}
    prame = {"userName":"18320308446","userPwd":"test0827.txt"}
    p = requests.post("http://127.0.0.1:80/login",params=prame,headers=headers)
    # p = requests.post("http://127.0.0.1:80/login?userName=18320308446&userPwd=test0827.txt")
    print p.content
    print p.headers

if __name__=="__main__":
    register()
    print '-'*40
    login()





















