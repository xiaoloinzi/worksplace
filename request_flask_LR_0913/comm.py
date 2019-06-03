# encoding=utf-8
import random
import os
import json
filepath = os.getcwd()+"/test.txt"

# 判断用户是否存在
def userExist_login(userName,userPwd):
    flag = 0
    with open(filepath,"a+") as fp:
        lines = fp.readlines()
        for line in lines:
            if line.startswith(userName+","+userPwd):#判断用户是否在文件中
                flag = 1
                break
    return flag
# 登陆方法
def login(userName,userPwd):
    flag = userExist_login(userName,userPwd)
    lineList = []
    if flag == 1:
        token = random.randint(1000,10000)
        with open(filepath,"a+") as fp:
            line = fp.readlines()
            for i in line:
                if i.startswith(userName+","+userPwd):
                    lineList.append(userName+","+userPwd+","+str(token)+"\n")
            lineList.append(i)
        with open(filepath,"w") as ft:
            ft.writelines(lineList)
        return {"message":"success","status":0,"token":token}
    if flag==0:
        with open(filepath,"a+") as f:
            f.write(userName+","+userPwd+"\n")
        return {"message":"user registered success ","status":0}
    else:
        return {"message":"failed","status":1,"token":""}



