# encoding=utf-8
#字节字符串
byteString = 'Hello world!'
#Unicode字符串
unicodeString = u'hello unicode world!'
print type(byteString)
print type(unicodeString)
print type('111'.decode('utf-8'))
print u'字节字符串和Unicode字符串的互换'
s = "byte string"
print type(s)
u = s.decode()
print type(u)
backToBytes = u.encode()
print type(backToBytes)
s = "hello normal string"
print u"字节字符串",type(s)
u = s.decode("UTF-8" )
print u"Unicode字符串",type(u)
backToBytes = u.encode( "UTF-8" )
print u"字节字符串",type(backToBytes)

#字节字符串
s1 = 'hello world'
#Unicode字符串
s2 = u'hello unicode world'
if isinstance(s1,str):
    print u's1是str类型'
if isinstance(s2,unicode):
    print u's2是unicode类型'
if isinstance(s2,basestring):
    print u's2可以用basestring进行判断'
if isinstance(s1,basestring):
    print u's1可以用basestring来判断'
list2 = "镇国"
file1 = open('test1.txt','r')
#file1.write(list2)
info1 = file1.read()
print type(info1)
print info1
file1.close()
tmp = info1.decode('GBK')
print isinstance(info1,unicode)
print isinstance(tmp,unicode)
print u'获取系统编码'
import sys
print sys.getdefaultencoding()
import chardet
import urllib
TestData = urllib.urlopen('http://www.baidu.com/').read()
print chardet.detect(TestData)
print u'比较高级的获取系统编码'
from chardet.universaldetector import UniversalDetector
usock = urllib.urlopen('http://www.baidu.com/')

#创建一个检测对象
detector = UniversalDetector()
for line in usock.readlines():
    #对块进行测试，直到阈值
    detector.feed(line)
    if detector.done:
        break
#关闭检测对象
detector.close()
usock.close()
#输出检测结果
print detector.result
import const
const.magic = 23
print const.magic
const.line = 33
print const.line
