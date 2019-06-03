# encoding=utf-8
import sys,os
try:
    fp = open('D:\\sdf\\fg\\score1.txt','r')
    print fp.readline()
    fp.close()
except IOError as e:
    print e,u'文件写入失败！'
else:
    print u'文件写入成功！'

try:
    try:
        1/0
    except IOError:
        print 'IOError occrur'
except Exception,e:
    print e
try:
    n = 0
    print 10/n
except:
    print u'做除法时发生异常！'

try:
    fp = open('D:\\cmp\\c3.txt','r')
    content = fp.read()
    fp.close()
except IOError:
    print u'读取文件时，发生IOError异常！'
else:
    print u'文件读取成功！'
    print content
try:
    s = raw_input('Enter something-->')
except:
    print '\nSome error/exception occurred.'
else:
    print 'no exception occur'
finally:
    print 'finally is executed!'

try:
    fh = open('D:\\cmp\\c123.txt','r')
    try:
        content = fh.read()
        print content
    finally:
        print u'关闭文件'
        fh.close()
except Exception,e:
    print u'Error:没有找到文件或读取文件失败！'
    print u'打印异常信息：'
    print e

def exceptionTest(num):
    if num < 0:
        raise Exception('Invalid num')
    else:
        print num
    if num == 0:
        raise ZeroDivisionError('integer division or modulo by zero')
exceptionTest(-12)
class Networkerror(RuntimeError):
    def __init__(self,value):
        self.value = value

try:
    raise Networkerror('Bad hostname')
except Networkerror,e:
    print 'my exception occurred value:',e.value

class ShortInputException(Exception):
    '''A user-defined excetion class.'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = raw_input('Enter something-->')
    if len(s)<3:
        raise ShortInputException(len(s),3)
except EOFError:
    print '\nWhy did you do an EOF on me?'
except ShortInputException,x:
    print "ShortInputException:The input was of length %d,\
    was expecting at least %d"%(x.length,x.atleast)
else:
    print 'no exception was raised.'

class Nerwordkerror(RuntimeError):
    def __init__(self,value):
        self.value = value

try:
    raise Nerwordkerror(u'异常')
except Nerwordkerror,e:
    print u'抛出异常：',e.value

class ShortInputException(Exception):

    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = raw_input('Enter something -->')
    if len(s)<3:
        raise ShortInputException(len(s),3)
except EOFError:
    print '\nWhy did you do an EOF on me?'
except ShortInputException,x:
    print 'ShoortINputException: The input was of length %d,was exceting at least %d'%(x.length,x.atleast)
else:
    print 'No exception was raised'
class opened(object):
    def __init__(self,filename):
        self.handle = open(filename)
        print 'Resource:%s'%filename
    def __enter__(self):
        print '[Enter%s]:Allocate resource.'%self.handle
    def __exit__(self, exc_type, exc_value, exc_trackback):
        print '[Exit%s]:Free resource.'%self.handle
        if exc_trackback is None:
            print '[Exit%s]:Exited without exception.'%self.handle
        else:
            print '[Exit%s]:Exited with exception raise.'%self.handle
            return False
        self.handle.close()
with opened(r'D:\cmp\c3.txt') as fp:
    for i in fp.readlines():
        print (i)
def add(x,y,*d):
    result = x+y
    for i in d:
        result +=i
    return result
if __name__=='__main__':
    try:
        assert 10==add(1,2,3,4),'111'
        print add(1,2,3,4)
    except AssertionError,e:
        print e
if __name__=='__main__':
    assert 10==add(1,2,3,4)
import test
print test.print_func(10)
Money = 2000
def AddMoey():
    global Money
    Money = Money+1
print Money
AddMoey()
print Money

from test import *

print add(1,2,5,8)
# print sub(100,34,2,5)
import test
print test.add(1,2,3,4,5)
print test.sub(100,2,34,5)

reload(test)
str1 = 8
def foo():
    print 'calling foo()..'
    aStr = 'bar'
    anInt = 23
    print "foo()'s globals:",globals()
    print '1-'*40
    print "foo()'s local:",locals().keys()
print "__main__'s globals:",globals().keys()
print '2-'*40
print "__main__'s locals:",locals().keys()
print '3-'*40
foo()
from test import *
print bar
print baz()
# print waz
print os.sys.path

print 192+'.'+168












