# encoding=utf-8
import requests
import  os

def test():
    r = requests.get("http://127.0.0.1:8888/test0827")
    print r.text

def testCookies():
    #发送消息
    res = requests.get("http://127.0.0.1:8888/getCookies")
    #获取cookies
    cookies = res.cookies
    value = cookies.get("cookiesName")#通过get获取
    #将CookieJar转为字典：
    cookies = requests.utils.dict_from_cookiejar(cookies)
    print "test0827",cookies
    print value
    print type(cookies)
    print ";".join(['='.join(item) for item in cookies.items()])
    print res.text
def testHead():
    res = requests.head("http://127.0.0.1:8888/getCookies")
    print res.headers
#put 更新一个记录，更新所有参数，传入的是一个对象
# patch 更新部分参数，比如只要更新用户名
def testOpitons():
    res = requests.options("http://127.0.0.1:8888/getCookies")
    print res.headers
#获取当前方法中支持的访问类型
def testPatch():
    #options<head<get
    res = requests.patch("http://127.0.0.1:8888/getCookies")
    print res.headers.get("Allow")

#自定义参数
def testMyParams():
    params = {"param1":["param11","param11"]}
    res = requests.get("http://127.0.0.1:80/getMyParams",params=params)
    print res.text
#单个文件上传
#1.打开文件
#2.将文件通过消息发送
def testUpload():
    f = open(os.getcwd()+"\\test1.png","rb")
    files = {"fileName":f}
    data = {"testData":"testData","testData2":"testData2"}
    #app url:  http://127.0.0.1:8888/upload?filename=test0827&userName=test0827&file=files
    res = requests.post("http://127.0.0.1:8888/upload",files=files,data=data)
    print res.headers
    print res.text
#一次上传多个文件
#md5(hash) ---文件+hash  --->服务端（算法）   (hash)+文件  ==合理安全
#断点续传（100M）上传到99M，网络断了  ----重新传（从99M开始）
def testUploads():
    f1 = open(os.getcwd()+"\\test1.png","rb") #第一个文件
    f2= open(os.getcwd()+"\\test1Upload.png","rb") #第二个文件
    f3= open(os.getcwd()+"\\client.py","rb") #第二个文件
    files = {"file1":f1,"file2":f2,"file3":f3} #定义传输文件
    res = requests.post("http://127.0.0.1:8888/uploads",files=files)
    print res.text

#下载
#客户端：需要指定下载的文件名，需要将返回的响应写入文件中
#服务端：获取文件名称，构造返回响应
def testDownload():
    #指定文件名称
    fileName ="test1.png"
    params = {"fileName":fileName} #使用params传参
    #发送响应
    # res = requests.get("http://127.0.0.1:8888/download?fileName="+fileName)
    res = requests.get("http://127.0.0.1:8888/download",params=params)
    #得到响应内容,并写入文件中
    with open(os.getcwd()+"\\downloadtest1.png","wb") as f:
        f.write(res.content)
    #print res.content

def testDownLoadStream():
     fileName ="test1.png"
     res = requests.get("http://127.0.0.1:8888/downloadStream?fileName="+fileName)
     #得到响应内容,并写入文件中
     with open(os.getcwd()+"\\downloadStreamTest1.png","wb") as f:
        f.write(res.content)
     print  res.status_code
     print res.text
def testLogin():
    userNmae = ""
    res = requests.post("http://127.0.0.1:8888/login?userName="+userNmae)
    print res.text
    print res.status_code #400
def testLogin2():
    userNmae = "11111"
    res = requests.post("http://127.0.0.1:8888/login2?userName="+userNmae)
    print res.text
    print res.status_code #500

def testMyException():
    res = requests.post("http://127.0.0.1:8888/testMyException")
    print res.text

def testTimeout():
    #客户端超时时间
    res = requests.post("http://127.0.0.1:8888/testMyException",timeout=7)
    #下面timeout中，第一个参数为链接建立的时间，第二个为客户端超时时间
    # res = requests.post("http://127.0.0.1:8888/testMyException",timeout=(1,7))
    print res.text
def testPath():
    res = requests.put("http://127.0.0.1:8888/testPath/path2/path22",timeout=7)
    print res.text














if __name__ == '__main__':
    testPath()

