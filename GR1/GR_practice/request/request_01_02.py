# encoding=utf-8
import requests

def rigester():
    pare = {"userName":"18324323441","userPwd":"123456"}
    p = requests.post("http://127.0.0.1/rigester",params=pare)
    print p.content
    print p.headers

def login():
    pare = {"userName":"18324323441","userPwd":"123456"}
    p = requests.post("http://127.0.0.1/login",params=pare)
    print p.content
    print p.headers


if __name__=="__main__":
    rigester()
    print '-'*40
    login()




























