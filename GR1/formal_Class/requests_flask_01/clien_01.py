# encoding=utf-8
import requests
# 【练习】怎么拿到返回的cookies
# 使用options方法，获取服务端的访问 类型，在服务端新增一个访问类型


def testCookies():
     # 发送消息
    r = requests.get("http://127.0.0.1:80/getCookies")
    #  将CookiesJar转为字典
    cookies = requests.utils.dict_from_cookiejar(r.cookies)
    print "test0827.txt",cookies
    # 获取cookies
    # 方法一
    for c in r.cookies:
        print c.name
        print c.value
    # 方法二
    print r.cookies.get("cookiesName")
    # 方法三
    print ":".join(['='.join(item) for item in r.cookies.items()])
    print [item for item in r.cookies.items()]
    print type(r.cookies)
    print r.text

def testHead():
    res = requests.head("http://127.0.0.1:80/getCookies")
    print res.headers

# put--更新一个记录--更新所有参数，传入的是一个对象
# patch--更新一个记录--更新部分参数，比如只要更新用户名
def testpatch():
    res = requests.patch("http://127.0.0.1:80/getCookies")
    print res.headers

def testOption():
    # option<head<get
    # 获取当前方法中支持的访问类型
    res = requests.options("http://127.0.0.1:80/getCookies")
    print res.headers
    print res.headers.get("Allow")

# 参数重复怎么处理？
def testMyParams():
    params = {"param1":["param11","param11"]}
    res = requests.get("http://127.0.0.1:80/getMyParams",params=params)
    print res.text
# 上传文件：
#单个文件上传
#1.打开文件
#2.将文件通过消息发送

def testUpload():
    f = open("test0827.txt",'rb')
    files = {"fileName":f}
    data = {"testData":"testData","testData2":"testData2"}
    res = requests.post("http://127.0.0.1:80/upload",files=files,data=data)
    print res.text

# 上传多个文件
# md5(hash)--文件+hash--->服务端（算法） （hash)+文件--检验是否一致==合理
def testUploads():
    f1 = open("test1.txt",'rb')
    f2 = open("test2.txt",'rb')
    f3 = open("clien_01.py",'rb')
    # 定义传输文件
    files = {"file1":f1,"file2":f1,"file3":f3}
    res = requests.post("http://127.0.0.1:80/uploads",files=files)
    print res.text
# 下载
def testDownload():
    # 指定文件名称
    filename="test0827.txt"
    # 定义传输文件
    # 使用params传值
    params = {"filename":filename}
    # 回响应
    # 方法一
    # res = requests.get("http://127.0.0.1:80/download?fileName="+filename)
    # 方法二
    res = requests.get("http://127.0.0.1:80/download",params=params)
    with open("downloadtest1.txt","wb") as fp:
        fp.write(res.content)


def testdownloadStream():
    # 指定文件名称
    filename="test0827.txt"
    res = requests.get("http://127.0.0.1:80/downloadStream?fileName="+filename)
    with open("downloadtest2.txt","wb") as fp:
        fp.write(res.content)

def testlogin():
    # 指定文件名称
    username="1234567"
    res = requests.post("http://127.0.0.1:80/login?userName="+username)
    print res.text
    print res.status_code


# 自定义异常
def testMyException():
    res = requests.post("http://127.0.0.1:80/testMyException")
    print res.text

def testTimeout():
    # 设置timeout多少秒不返回默认失败
    # 设置客户端超时时间
    # res = requests.post("http://127.0.0.1:80/testMyException",timeout=5)
    # 下面timeout中，第一个为链接建立的时间，第二个为客户端超时时间
    res = requests.post("http://127.0.0.1:80/testMyException",timeout=(1,7))
    print res.text

def testPath():
    res = requests.post("http://127.0.0.1:80/testPath")
    print res.text

def testPath2():
    res = requests.post("http://127.0.0.1:80/testPath/path2")
    print res.text

if __name__=="__main__":
   testUpload()


















