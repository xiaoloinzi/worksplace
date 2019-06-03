# encoding=utf-8
import  requests,os
imageRootPath = os.getcwd()+"\\image"
downLoadImagePath = os.getcwd()+"\\download"

#下载
def testDownLoad(fileName):
     params = {"fileName":fileName}
     r = requests.get("http://127.0.0.1:8888/downLoad",params=params)
     #写文件
     if r.status_code == 200:
         with open(downLoadImagePath+"\\"+fileName,"wb") as f:
             f.write(r.content)
#添加内容
def testAddContent():
    params = {"contentValue":"我的第一个帖子"}
    files = {"file":open(imageRootPath+"\\test0827.png","rb")}
    r = requests.post("http://127.0.0.1:8888/addContent",params=params,files = files)
    print r.text
#查询内容
def testQueryContent():
    # params = {"contentId":6}
    # r = requests.get("http://127.0.0.1:8888/queryContent",params=params)
    r = requests.get("http://127.0.0.1:8888/queryContent")
    print r.json()
#删除内容
def testDeleteContent():
    params = {"contentId":7}
    r = requests.delete("http://127.0.0.1:8888/deleteContent",params=params)
    print r.text
    print r.status_code

if __name__ == '__main__':
    testAddContent()
    testQueryContent()
    # testDeleteContent()
    fileName = "3.png"
    testDownLoad(fileName)