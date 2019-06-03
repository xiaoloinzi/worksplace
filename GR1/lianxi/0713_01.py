# encoding=utf-8
import sys
import chardet
import urllib

print u'一周有%d分钟，有%d秒钟。'%(7*24*60,7*24*60*60)










print sys.getfilesystemencoding()
print sys.getdefaultencoding()

res = urllib.urlopen('http://www.baidu.com').read()
print chardet.detect(res)
s = u'中文'.encode('utf-8')
print chardet.detect(s)

with open('D:\\testfile.txt','r') as fp:
    res = fp.read().decode('gbk').encode('utf-8')
print res
with open('D:\\testfile.txt','w') as fp:
    fp.write(res)
with open('D:\\testfile.txt','r') as fp:
    resa = fp.read()
print resa

with open('D:\\testfile.txt','r') as fp:
    stra = fp.read()
print stra






