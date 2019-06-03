# encoding=utf-8
import os
import json
import random
from flask import flash
filePath = os.getcwd()+"\\data\\register.txt"

# 判断用户是否存在
def userExist(userName):
    flag = 0
    # if not os.path.exists(filePath):
    #     with open(filePath,'w') as f:
    #         f.write("")
    with open('register.txt',"a+") as fp:
        lines = fp.readlines()
        for line in lines:
            if(line.startswith(userName)):#判断用户是否在文件中
                flag = 1
                break
    return flag



# 注册方法
def regiger(userName,userPwd):
    flag = userExist(userName)#判断用户是否存在
    if flag==0:
        with open('register.txt',"a+") as f:
            f.write(userName+","+userPwd+"\n")
        return {"message":"user registered success ","status":0}
    else:
        return json.loads('{"message":"user has registered,user name is '+userName+'","status":1}')

# 判断用户是否存在
def userExist_login(userName,userPwd):
    flag = 0
    # if not os.path.exists(filePath):
    #     with open(filePath,'w') as f:
    #         f.write("")
    with open('register.txt',"a+") as fp:
        lines = fp.readlines()
        for line in lines:
            if(line.startswith(userName+","+userPwd)):#判断用户是否在文件中
                flag = 1
                break
    return flag

# 登陆方法
def login(userName,userPwd):
    flag = userExist_login(userName,userPwd)
    if flag == 1:
        token = random.randint(0,10000)
        return {"message":"success","status":0,"token":token}
    else:
        return {"message":"failed","status":1,"token":""}




















