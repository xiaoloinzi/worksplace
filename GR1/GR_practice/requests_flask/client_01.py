# encoding=utf-8
import random
import requests
import os
# 【20170806课后练习】 模拟微信朋友圈的服务端，需要满足以下场景：
# 1.发表内容时带上图片信息，内容包括（具体内容和id，id指定全局唯一标识），客户端请求后服务端将信息保存在excel中
# 2.删除无效的内容
# 3.对朋友圈进行查询操作，返回所有的查询结果（内容在控制台进行打印，文件保存在临时目录）
# 【注意】
# 客户端：使用时建议做一个流程，即发表->查询->删除，这样来测试服务端--Publish -> Query -> Delete
# 测试异常：如果进行查询或者删除不存在的资源时，提示资源不存在并且返回错误码为404

def publish():
    files = {"fileName":"1.png"}
    strnum = "43gffdg"
    data = {"ID":"183253214211","Value":strnum}
    res = requests.post("http://127.0.0.1:8888/publish",files = files,data = data)
    print res.content

def query():
    files = "861.png"
    params = {"userID":"183253214211","fileName":files}
    res = requests.get("http://127.0.0.1:8888/query",params = params)
    file = "abc1.png"
    if os.path.exists(file):
        file = str(random.randint(100,200))+file
    with open(file,'wb') as fp:
        fp.write(res.content)
    print res.content
    print res.status_code
    print u"查询的结果：",res.headers['X-Parachutes']


def delete():
    files = "251.png"
    params = {"userID":"183253214211","fileName":files,"stringNum":"123"}
    res = requests.get("http://127.0.0.1:8888/delete",params = params)
    print res.content
    print res.status_code

if __name__=="__main__":
    publish()
    # query()
    # delete()











