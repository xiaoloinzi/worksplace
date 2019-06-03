# encoding=utf-8
import requests

#    http://127.0.1.1:80/register?userName=test0827.txt&userPwd=test0827.txt
#测试注册方法
def register():
    #发送请求
    params = {"userName":"18010101011","userPwd":"test0827.txt"}
    headers = {"Content-Type":"application/json"}
    cookies = {"cookiesName":"cookiesValue"}
    r = requests.post("http://127.0.0.1:80/register",params=params,headers=headers,cookies=cookies)
    #打印结果
    print r.headers
    print r.content
    print r.cookies
#测试登录方法
def login():
    params = {"userName":"18010101011","userPwd":"test0827.txt"}
    headers={"Content-Type":"application/json2","Content-Length":"100"}
    # cookies={""}
    r = requests.post("http://127.0.0.1:80/login",params=params,headers=headers)
    print r.headers
    print r.content
#主函数
if __name__ == '__main__':
    register()





# #发送消息  http://ip:port/action?key1=value1&key2=value2
# url ="http://127.0.0.1:80/login?userName=test0827.txt&userPwd=test0827.txt"
# # r = requests.get(url)
# r=requests.post(url)
# print r.headers
# print r.cookies
# r.text
# print r.content
# print r.status_code
# print r.url
