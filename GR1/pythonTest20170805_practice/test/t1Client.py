# encoding=utf-8
import requests

#    http://127.0.1.1:80/register?userName=test0827&userPwd=test0827
#测试注册方法
def register():
    #发送请求
    params = {"userName":"18010101011","userPwd":"test0827"}
    headers = {"Content-Type":"application/json"}
    cookies = {"cookiesName":"cookiesValue"}
    r = requests.post("http://127.0.0.1:80/register",params=params,headers=headers,cookies=cookies)
    #打印结果
    print r.headers
    print r.content
    print r.cookies
#测试登录方法
def login():
    params = {"userName":"18010101011","userPwd":"test0827"}
    headers={"Content-Type":"application/json2","Content-Length":"100"}
    # cookies={""}
    r = requests.post("http://127.0.0.1:80/login",params=params,headers=headers)
    print r.headers
    print r.content

#测试客户端cookies
#1.定义一个cookies
#2.将cookies放入request中进行发送
#3.服务端接收后进行判断cookies是否正确，正确返回成功，错误提示cookies错误
#4.接收响应，打印响应结果
def testCookies():
    cookies = {"testCookiesKey1":"testCookiesValue1"} #定义cookies
    url ="http://127.0.0.1:80/testCookies" #定义访问路径
    r = requests.get(url,cookies=cookies) #发送消息
    print r.text #打印响应消息
#3.自己实现一个put方法，修改用注册信息，修改密码
#客户端：1.使用reqesuts进行发送消息
        #2.打印结果
#服务端：1.定义消息的入口，实现接口
        #2. a)获取消息 b)处理业务并获取返回消息 c)返回响应
                       #b1)判断修改的用户是否存在
                       #b2)如果存在直接修改（修改文件_读、改、写）
#测试修改用户密码
def testUpdate():
    #参数与访问的路径放在一起
    url="http://127.0.0.1:80/updateUserPwd?userName=18010101011&userPwd=test0827&newPwd=testNew"
    r = requests.put(url)
    print r.text
#测试删除用户
#4.自己试下一个delete方法，注销用户信息
   #服务端
    #定义个删除方法和对应路径，处理业务和返回
   #客户端
    #构造删除响应
def testDelete():
    url = "http://127.0.0.1:80/deleteUser?userName=18010101011&userPwd=testNew"
    r = requests.delete(url)
    print r.text


#主函数
if __name__ == '__main__':
    testDelete()





# #发送消息  http://ip:port/action?key1=value1&key2=value2
# url ="http://127.0.0.1:80/login?userName=test0827&userPwd=test0827"
# # r = requests.get(url)
# r=requests.post(url)
# print r.headers
# print r.cookies
# r.text
# print r.content
# print r.status_code
# print r.url
