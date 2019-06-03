# encoding=utf-8
from flask import Flask,request,jsonify
import re

app = Flask(__name__)
#url中表示空格%20/


def check(username,userpwd):
    # 校验用户名
    if username == None or username == "":
        return {"message":"username is None","status":0}
    # 校验用户名是否有中文
    userNameMatch = u'[\u4e00-\u9fa5]'
    userNameCompilie = re.compile(userNameMatch)
    if len(userNameCompilie.findall(username)) == None:
        return {"message":"username can not cantain chinese","status":0}
    # 校验用户名是否有空格
    if str(username).find(" ")>-1:
        return {"message":"username can not cantain blank","status":0}
    #校验用户名是否符合手机号的规范，校验有效性
    userNameMatch = '^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$'
    if re.match(userNameMatch,username) == None:
        return {"message":"username is wrong","status":0}
    # 校验密码
    if userpwd == None or userpwd == "":
        return {"message":"userpwd is None","status":0}
    # 校验密码是否有中文
    userNameMatch = u'[\u4e00-\u9fa5]'
    userNameCompilie = re.compile(userNameMatch)
    if len(userNameCompilie.findall(userpwd)) == None:
        return {"message":"userpwd can not cantain chinese","status":0}
    # 校验密码是否有空格
    if str(userpwd).find(" ")>-1:
        return {"message":"userpwd can not cantain blank","status":0}
    # 校验密码是否有大写字母
    userpwdletter = re.compile('[A-Z]')
    if len(userpwdletter.findall(userpwd)) == 0:
        return {"message":"userpwd must contain upper letter","status":0}
    # 验证密码是否有数字
    userpwddigit = re.compile('[0-9]')
    if len(userpwdletter.findall(userpwd)) == 0:
        return {"message":"userpwd must contain upper letter","status":0}
    if len(userpwd) < 8 or len(userpwd) > 12:
        return {"message":"userpwd lenth can 8-12","status":0}
    return {"message":"login success","status":1}





@app.route("/login",methods=["POST"])
def login():
    # url格式校验
    url = request.url
    # 获取参数
    username = request.args.get("username")
    userpwd = request.args.get("userpwd")
#     参数校验
    result = check(username,userpwd)
#     返回结果
    return jsonify(result)








if __name__=="__main__":
    app.run(host="127.0.0.1",port=8888,debug=True,threaded = True)






















