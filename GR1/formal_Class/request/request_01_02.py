# encoding=utf-8
import requests
import json

def register():
    param = {"telnumber":"18320308441","pwd":"123456"}
    r = requests.post("http://127.0.0.1/zc",params=param)
    print r.text
def login():
    param = {"usertel":"18320308441","userpwd":"123456"}
    r = requests.post("http://127.0.0.1/login",params=param)
    print r.text

if __name__=='__main__':
    register()
    login()







