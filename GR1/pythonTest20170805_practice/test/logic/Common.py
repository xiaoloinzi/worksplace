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
#修改用户密码
def updateUserPwd(userName,userPwd,newPwd):
    #判断修改的用户是否存在(读文件，判断)
    flag = userExist_login(userName,userPwd)
    #修改动作(1.先把内容读出来，读出来的过程中对数据进行修改
    #  2. 将修改后的数据重新写入文件中)
    if flag == 1:
        listUsers = []
        with open(filePath,"r") as f:
            lines = f.readlines()
            for line in lines:
                tmp1 = userName+","+userPwd+"\n"
                tmp2 = userName+","+userPwd
                if cmp(line,tmp1) == 0 or cmp(line,tmp2) ==0:
                    #修改
                    line = line.replace(userPwd,newPwd)
                #将每行数据加入到集合中
                listUsers.append(line)
        with open(filePath,"w") as f:
            f.writelines(listUsers)
        return {"message":"update password successfully"}
    else:
        return {"message":"userName or password is wrong"}


#删除方法
def delete(userName,userPwd):
    #先读取，读取删除的用户，重新写入文件
    listUsers = []
    with open(filePath,"r") as f:
        lines = f.readlines()
        for line in lines:
            tmp1 = userName+","+userPwd
            tmp2 = userName+","+userPwd+"\n"
            #如果不相等，我们就挑选出来
            if cmp(line,tmp1) != 0 and  cmp(tmp2,line) != 0:
                 listUsers.append(line)
    #重新写入文件
    with open(filePath,"w") as f:
        f.writelines(listUsers)
    return {"message":"delete user successfully"}

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


