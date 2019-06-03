# encoding=utf-8
import json
import os
import random
filePath = os.getcwd()+"\\data\\register.txt"

#判断用户是否存在
def userExist(userName):
    flag = 0 #0表示不存在
    if os.path.exists(filePath) == False:
        with open(filePath,"w") as f:
            f.write("")
    if os.path.exists(filePath):
        with open(filePath,"r") as f:
            lines = f.readlines()
            for line in lines:
                if(line.startswith(userName)):
                    flag = 1 #表示存在
                    break
    return flag
#登录验证用户是否正确
def userExist_login(userName,userPwd):
    flag = 0 #0表示用户名和密码错误
    if os.path.exists(filePath) == False:
        with open(filePath,"w") as f:
            f.write("")
    if os.path.exists(filePath):
        with open(filePath,"r") as f:
            lines = f.readlines()
            for line in lines:
                if(line.startswith(userName+","+userPwd)):
                    flag = 1 #表示用户名和密码正确
                    break
    return flag
#注册方法
def regiger(userName,userPwd):
    #判断用户是否存在
    flag = userExist(userName)
    if flag == 0:#用户不存在的情况
        with open(filePath,"a+") as f:
            f.write("\n"+userName+","+userPwd)
        # return json.loads('{"message":"user register success","status":0}') #或者使用下面的选项
        return {"message":"user register success","status":0}
    else: #用户存在的情况
        return json.loads('{"message":"user has registered,user name is '+userName+'","status":1}')

#登录方法
def login(userName,userPwd):
    flag = userExist_login(userName,userPwd)
    if flag ==1:
        token = random.randint(0,10000)
        return {"message":"success","status":0,"token":token}
    else:
        return {"message":"failed","status":1,"token":""}


