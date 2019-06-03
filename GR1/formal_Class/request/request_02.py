# encoding=utf-8
import requests
import json

# 发送消息
url = "http://127.0.0.1/login?userName=test0827.txt&userPwd=123456"
url1 = "http://httpbin.org"
url2 = "http://127.0.0.1/zc?userName=test0827.txt&userPwd=123456"
# r = requests.get(url)
r = requests.get(url2)
strs =  r.text
print strs
with open("file1.txt",'w') as fp:
    fp.write(json.dumps(strs))


# print r.content
# print r.status_code
# print r.cookies
# print r.headers
# print r.url


#
























