# encoding=utf-8
import requests
import os

def testCert():
    cert = os.getcwd()+"\\cert\\server.crt"
    r = requests.get("http://test0827.com:8889/testCert",verify=cert)
    print r.text

if __name__=="__main__":
    testCert()











