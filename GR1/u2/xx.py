# encoding=utf-8
# list = [1,2,3,4,5]
# # print len(list)
# # print range(len(list))
# # print range(2)
# while True:
#     for i in range(len(list)):
#         if i == 4:
#             print i
#
#         else:
#             print i+1
#     break
# else:
#     print 'getover!'

# for i ,j in enumerate(('a','b','c')):
#     print i,j
#
# for i ,j in enumerate(['a','b','c']):
#     print i,j
#
# for i ,j in enumerate({'a':1,'b':2}):
#     print i,j
#
# for i ,j in enumerate('abc'):
#     print i,j
#
# str1 = 'abcd1234'
# list1 = []
#
# for i in str1:
#     list1.append(i)
#
#
# # for i in range(len(str1)):
# s = list1[2]
# print list1
# print type(eval(s))

# str = 'this is my name'
# print '',str.capitalize()
# str1 = 'abcd'
# s = '\t '
# for i in str1:
#     s +=i
# print s

# # 1、
# i = int(raw_input('please input the num'))
#
# if i < 1 or i >127:
#     print 'input error'
#     exit(-1)
# else:
#     print 'this is :',chr(i)

# 2、
# list1 = [1,2,3]
#
# if 4 in list1:
#     print 4
# else:
#     print False

# dict1 = {'1':1,'2':2}
#
# print dict1.copy()
# print dict1.setdefault(3,3)
# print dict1
# import time
# localtime = time.asctime(time.localtime(time.time()))
# print localtime
#
# print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# print time.strftime('%Y.%m.%d %H:%M:%S',time.localtime())
# a = "Sat Mar 28 22:24:24 2016"
# print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
# a = "Sat Mar 28 22:24:24 2016"
# print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
# import calendar
#
# cal = calendar.month(2017,1)
# print u'以下输出2017年1月份的日历'
# print cal

# class Emploee:
#     '所有员工的基类'
#     empCount = 0
#
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         Emploee.empCount += 1
#         print '111'
#
#     def displayCount(self):
#         print 'Total Employee %d'%Emploee.empCount
#
#     def displayEmployee(self):
#         print 'Name:',self.name,'Salary:',self.salary
#
# s = Emploee('lin',23)
# s.empCount = 2
# s.displayCount()

# class Test:
#     def prt(self):
#         print self
#         print self.__class__
#
# t = Test()
# t.prt()

# print 'Content-type:text/html'
# print
# print '<html>'
# print '<head>'
# print '<meta charset="utf-8">'
# print '<title>Hello Word - 我的第一个CGI程序!</title>'
# print '</head>'
# print '<body>'
# print '<h2>Hello Word!我是来自菜鸟教程的第一CGI程序</h2>'
# print '</head>'
# print '<body>'

# import os
#
# print "Content-type: text/html"
# print
# print "<meta charset=\"utf-8\">"
# print "<b>环境变量</b><br>";
# print "<ul>"
# for key in os.environ.keys():
#     print "<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key])
# print "</ul>"
# import socket               # 导入 socket 模块
#
# s = socket.socket()         # 创建 socket 对象
# host = socket.gethostname() # 获取本地主机名
# port = 12345                # 设置端口
# s.bind((host, port))        # 绑定端口
#
# s.listen(5)                 # 等待客户端连接
# while True:
#     c, addr = s.accept()     # 建立客户端连接。
#     print '连接地址：', addr
#     c.send('欢迎访问菜鸟教程！')
#     c.close()                # 关闭连接


# import socket               # 导入 socket 模块
#
# s = socket.socket()         # 创建 socket 对象
# host = socket.gethostname() # 获取本地主机名
# port = 12345                # 设置端口好
#
# s.connect((host, port))
# print s.recv(1024)
# s.close()

# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = 'xiaoloinzi@163.com'
# receivers = ['1247636039@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] =  Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print "邮件发送成功"
# except smtplib.SMTPException:
#     print "Error: 无法发送邮件"

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
# mail_host="smtp.xiaoloinzi@163.com"  #设置服务器
# mail_user="xiaoloinzi@163.com"    #用户名
# mail_pass="xiaoloinzi1992"   #口令
#
#
# sender = '2634929796@qq.com'
# receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] =  Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
#     smtpObj.login(mail_user,mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print "邮件发送成功"
# except smtplib.SMTPException:
#     print "Error: 无法发送邮件"

# list1 = ['a',1,2,'one']
# print list1
# del list1[2]#删除列表中某个元素
# print list1
# list1.remove('one')
# print list1
# list1.insert(2,'lin')
# print list1
# list2 = ['we',1,'re']
# print list1 + list2
# list3 = []
# list3.extend(list2)
# print list3
# print 3 in list3
# print cmp(list3,list1)
# tuple = (1,2,3)
# print list(tuple)
# print [m + n for m in 'ABC' for n in 'XYZ']
#
# l = [x*x for x in range(10)]
# print l
#
# g = (x*x for x in range(10))
# print g

# print g.next()
# print g.next()

# for n in g:
#     print n

# def odd():
#     print 'step 1'
#     yield 1
#
# print odd().next()

# for i ,value in enumerate(['A','B','C']):
#     print i,value

# tupl1 = (1,2,3)
# print tupl1
# tupl1[0] =100
# print tupl1
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get('http://www.cloudit.info/')
# print 'open success'


# import cgi
# form=cgi.FieldStorage()
# name=form.getvalue('name','world')
# print """Content-type:text/html  
#   
# <html>  
#    <head>  
#      <title>Greeting Page</title>  
#    </head>  
#    <body>  
#      <h1>Hello.%s!</h1>  
#        
#        
#      <form action='simple3.cgi'>  
#      Change name <input type='text' name='name'/>  
#      <input type='submit' />  
#      </form>  
#     </body>  
# </html>  
# """%name

# list1 = [[1,42,43,4],
#          [15,120,77,80],
#          [9,120,20,12],
#         [9,10,6,120]]
# def maxMatrix(mylist):
#     maxDIct = {}
#     for index,li in enumerate(mylist):
#         for i,e in enumerate(li):
#             if len(maxDIct)==0:
#                 maxDIct[e] = [(index+1,i+1)]
#             else:
#                 if maxDIct.keys()[0] < e:
#                     maxDIct.clear()
#                     maxDIct[e]= [(index+1,i+1)]
#                 elif maxDIct.keys()[0] ==e:
#                     maxDIct[e].append((index+1,i+1))
#     return maxDIct
# print maxMatrix(list1)
# from selenium import webdriver
# print help(webdriver.implicitly_wait)
# list1 = [1,4,45,33,5,23,8,9,67,79]
#
# def ErFen(list,n):
#     list.sort()
#     print list
#     f = 0
#     e = f+len(list)
#     m = (f+e)/2
#     while n in list:
#         if n == list[m]:
#             print n,u'在列表',list,u'的位置是',m
#             exit()
#         elif n > list[m]:
#             m = len(list[m:e])/2
#         elif n < list[m]:
#             m = len(list[f:m])/2
#     print u'没有在列表中找到',n
#
# ErFen(list1,67)
test = '#glory road is great!\n;glory road is great!\n;glory road is great!;'
fp = open('tuan.txt','w')
print type(fp)
fp.write(test)
fp.close()

fp = open('tuan.txt','r')
print fp.readline()
fp.close()

print '-'*40

fp = open('tuan.txt','r')
print fp.read()
fp.close()

fp = open('tuan.txt','a')
pass
fp.close()


print '-'*40

fp = open('tuan.txt','r')
resuil = fp.readlines()
print resuil
fp.close()

print '-'*40
resuil.insert(2,'34\n')
print resuil


fp = open('tuan1.txt','w')
print u'文件是否关闭：',fp.closed
print u'文件的访问模式：',fp.mode
print u'文件名称：',fp.name
print u'文件末尾是否强制加空格：',fp.softspace
for i in resuil:
    fp.writelines(i)
fp.close()

print '-'*40
fp = open('tuan1.txt','r')
print fp.read()
fp.close()


print '-'*40
with open('tuan1.txt','r') as f:
    for line in f:
        print line

print '-'*40
with open('tuan.txt','r') as fp:
    content = fp.readline(5)
    print content

print '-'*40
with open('tuan1.txt','r') as fp:
    s = fp.readlines()
    print s
    r = []
    for i in s:
        i = i.strip()
        r.append(i)
    print r

print '-'*40
with open('tuan.txt','r') as fp:
    list1 = []
    for line in fp:
        list1.append(line.strip('\n'))
    print list1

print '-'*40
fp = open('tuan.txt','r')
print u'文件名：',fp.name

fp.close()
print u'文件是否关闭：',fp.closed

print '-'*40

fp = open('test0827.txt.txt','r')
#print fp.read()
# print '-'*40
print '1:',fp.next(),
print '2:',fp.next(),
print '3:',fp.next(),
fp.close()

print '-'*40

print u'fileObject.fileno()返回一个长整型的文件标签'
print '-'*40

fp = open('test0827.txt.txt','r')
print fp.fileno()
fp.close()

print '-'*40

print u'fileObject.isatty()文件是否是一个终端设备文件（Unix）系统中的'


fp = open('tuan.txt','r')
print fp.isatty()
fp.close()

print '-'*40
fp = open('tuan.txt','r')
print u'使用readline()'
print u'当前文件操作标记位置为：',fp.tell()
resuia = fp.readline()
print u'现在文件操作标记位置为：',fp.tell()
fp.close()

print '-'*40
fp = open('tuan.txt','r')
print u'使用readlines()'
print u'当前文件操作标记的位置为：',fp.tell()
resuiaw = fp.readlines()
print u'现在文件操作标记位置为：',fp.tell()
fp.close()

print '-'*40

fp = open('tuan.txt','r')
str = fp.read(16)
print u'读取的字符串是：',str
position = fp.tell()
print u'当前文件的位置：',position

position = fp.seek(2,0)
position = fp.tell()
str = fp.read(16)
print u'文件现在的位置：',position
print u'重新读取到的字符',str
fp.close()

print '-'*40
fp = open('test0827.txt.txt','r+')
print 'Name of the file:',fp.name
line = fp.readline()
print 'Read Line:%s'%(line)

# fp.truncate()
print fp.tell()
remainingLine = fp.readline()
print 'Read Line:%s'%(remainingLine)

fp.close()
print '-'*40

fp = open('kong.txt','w')
fp.close()

fp = open('test0827.txt.txt','r')
lin = fp.readlines()
for i in lin[::2]:
    print i.strip()
fp.close()
print '-'*40

# fp = open('test0827.txt.txt','r')
# print fp.next(),
# print fp.next()
# fp.close()

# print '-'*40

fp = open('test0827.txt.txt','r+')

str = fp.readline()
print str
fp.writelines(str)
print fp.read()
fp.close()











