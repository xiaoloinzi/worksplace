# encoding=utf-8
import requests
def testLoginNormal():
    url = "http://127.0.0.1:8888/login"
    params = {"userName":"test","userPwd":"test"}
    r = requests.get(url,params=params)
    print r.content
def testLoginFault():
    url = "http://127.0.0.1:8888/login"
    params = {"userName":"test1","userPwd":"test"}
    r = requests.get(url,params=params)
    print r.content
if __name__ == '__main__':
    testLoginNormal()
    testLoginFault()