# encoding=utf-8
import requests
import os

# 添加内容
imageRootPath = os.getcwd()+"\\image"
def testaddContent():
    params = {"contentValue":"我的第一个帖子"}
    file = {"file":open(imageRootPath+"\\test0827.png",'rb')}
    r = requests.post("http://127.0.0.1:80/addContent",params=params,files=file)
    print r.text
# 查询内容
def testqueryContent():
    params = {"contentId":2}
    r = requests.get("http://127.0.0.1:80/queryContent",params=params)
    print r.json()


# 删除内容
def testdeleteContent():
    params = {"contentId":2}
    r = requests.delete("http://127.0.0.1:80/deleteContent",params=params)
    print r.text()


if __name__=="__main__":
    # testaddContent()
    # testqueryContent()
    testdeleteContent()












