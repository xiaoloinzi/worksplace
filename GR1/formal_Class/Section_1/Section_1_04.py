# encoding=utf-8
import chardet
import urllib
TestDate = urllib.urlopen('http://www.baidu.com').read()
print chardet.detect(TestDate)

# 题目：定义一个中文的字符串，
# 并且使用utf-8编码，使用chardet 检测其编码方式
s1 = u'你好'
print chardet.detect(s1)

#


