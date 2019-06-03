# encoding=utf-8
import os,sys

# 习题：写一个函数，嵌套捕获异常，捕获open文件的IO异常，
# 以及在操作文件过程中的异常（通过raise 抛出异常）。
# 分别构建两种异常（打开文件的IOError 和 raise 的异常），
# 并且讲出程序是在哪里捕获的。

def func(fileName):
    try:
        with open(fileName) as fp:
            print 'enter with area.'
            raise Exception('bad input')
    except IOError as e:
        print 'enter IOerror area'
        print e.message
    finally:
        print 'enter finally area'

# func('D:\\tmp\\t3.txt')
func('D:\\tmp\\t1.txt')#程序本身会出现异常，走的分支是finally

# 断言
#1、断言的好处
#2、断言使用的场景有哪些
# a = 2048
# assert a==2047
# assert a>10 and type(a)==list
# assert type(a)== int
#
# # 写一个乘法函数，之后做断言，一次断言失败，一次断言成功。
#
# def ChenFa(a,b):
#     return a*b
#
# assert ChenFa(2,3)==5
# assert ChenFa(2,3)==6

# 大家在调用的时候总是会遇到 print  模块.函数名
# 这样的结果是表示打印这个函数的返回值，如果没有返回就是none
# 之前很多同学有遇到这个问题

# 模块
# import t1#执行非代码块代码

# import test0827.txt
#
# test0827.txt.printDef()

# # 全局变量
money = 230
list1 = [1,2,3,4,5]
def addMonkey():
    global money
    money = 230
    money +=money
    print money
    list1.append(6)
    list1 = [2,3,4]#内地址改变了
    print list1
#
#
# # 列表在函数中可以直接调用列表，列表只是一个地址，
# # 可以直接使用内存中的地址
#
print money
print list1
addMonkey()
print money
print list1

# import XXX
# from XXX import XXXX

from t1 import *

print a
print str1
func()

import test
reload(test)
test.printDef()
for line in sys.path:
    print line

# package--1、包含多个py文件，多个模块，并且可以包含子package
# 如何识别一个目录是package--通过__init__.py来识别
import p1
# import package会干什么事--执行__init__.py这个文件
print p1.tp1.tp1a
print p1.tp1.tp1b
p1.tp1.tpqFunc()

__all__ = ['a','func']#指定导入的变量和函数
from p1 import *
print tp1.tp1a
print p11.tp11.abc

# 7、关于包的概念，创建一个包，有三层子目录，
# 在最上层新建一个test.py，调用其中函数，
# 覆盖三层中的方法：
# 1）__init__.py 文件内容是import xxx
# 2）__init__.py 文件内容是__all__ =xxx

# if __name__=='__main__'--判断之前执行的脚本是否是主程序在执行
# 导入的时候不会执行if下面的子语句

# 9、实现一个函数，判断文件里面中文的编码格式（1、手工新建，gbk；2、通过python 新建，并写入中文。utf-8），不能使用chardet模块。要求能判断utf-8 和 gbk 的编码格式
# func(fileName)：
# 	return ‘gbk'
# 	return ‘utf-8'
# '中国'

with open('D:\\tmp\\t4.txt','w') as fp:
    fp.write('中国'.encode('base64'))
def func(fileName):
    try:
        with open(fileName) as fp:
            line = fp.read()
        if line =='中国'.encode('gbk'):
            return 'gbk'

        elif line =='中国'.encode('utf-8'):
            return 'utf-8'
        else:
            return u'utf-8和gbk编码方式以外的编码方式'
    except Exception,e:
        print e

print func('D:\\tmp\\t3.txt')
print func('D:\\tmp\\t2.txt')
print func('D:\\tmp\\t4.txt')
#
#
def func(fileName):
    with open(fileName) as fp:
        content = fp.read()
    if content == u'中国'.encode('gbk'):
          return 'gbk'
    elif content == u'中国'.encode('utf-8'):
        return 'utf-8'
    else:
        return 'unknow'

print func('D:\\tmp\\t3.txt')
print func('D:\\tmp\\t2.txt')
print func('D:\\tmp\\t4.txt')


# set集合--元素不能重复
s1 = set('This is string')
s2 = set([1,2,3,4])
s3 = set((1,2,3,4,5,1,2))
s4 = set({1:2,2:3,6:6})
print 's1:',s1
print 's2:',s2
print 's3:',s3
print 's4:',s4
#
# # 添加元素
# # add()--把添加元素当做一个整体提交进去
# # update()--把添加的元素一个一个迭代添加进去
s2.add('abc')
print 's2:',s2
s2.update('abc')
print 's2:',s2
#
# # 删除集合中的元素
# remove(setstr)
s2.remove('c')
print 's2:',s2

# # 遍历集合
for i in s2:
    print i

list1 = [1,2,3,1,2,3,1,2,3,4,5,6,]
for i in set(list1):
    print u'%d出现的次数：%d'%(i,list1.count(i))#使用count计算个数

# 带序号的遍历--枚举enumerate
for index,elem in enumerate(s2):
    print index,':',elem
print list(s2)
print tuple(s2)
print str(s2)

# 删除：remove.discard()、pop()
print 's2:',s2
s2.discard(3)
print 's2:',s2
print s2.pop()
print 's2:',s2
#
# # 2、在集合setA中，新加一个元素'two',
# # 之后新加'hello python'中的每一个字符；
# # 用不少于三种方法，删除集合中一个元素。
#
#
setA = set('abc')
print 'setA:',setA
setA.add('two')
print 'setA:',setA
setA.update('hello python')
print 'setA:',setA
setA.remove('t')
print 'setA:',setA
setA.pop()
print 'setA:',setA
setA.discard('l')
print 'setA:',setA

# clear()清空
print 's1:',s1
s1.clear()
print 's1:',s1

# copy()复制
s6 = s2.copy()
print "s6:",s6

# len()集合的长度
print len(s6)

# 与、或、差
s11 = set([1,2,3])
s10 = set([2,3])
s12 = set([2,3,4,5])
s13 = s12&s11#显示相同的元素
print 's13',s13
s14 = s11 | s12#去掉重复的元素
print 's14:',s14
s15 = s11-s12#显示s11中没有s12的元素
print 's15:',s15
s16 = s11.difference(s12)
print 's16:',s16
print s10 < s12#s10的元素都可以在s12中找到
print s11 >= s12#s11的元素不是全部都能在s12中找到
print s11 != s12

# s1.issuperset(s2)集合s1是s2的父集
print s11.issuperset(s12)
print s10.issuperset(s12)
print s12.issuperset(s10)

# s1.issubset(s2),s1是否是s2的子集
print s11.issubset(s12)
print s10.issubset(s12)
print s12.issubset(s10)
#
#
# # 3、使用不少于两种方法，判断一个集合是否是另外一个集合的子集
#
#
s11 = set([1,2,3])
s10 = set([2,3])
s12 = set([2,3,4,5])


print s11.issubset(s12)
print s10.issubset(s12)
print s12.issubset(s10)
print s10 < s12
print s11 >= s12
print s11.issuperset(s12)
print s10.issuperset(s12)
print s12.issuperset(s10)



# 对于已知的集合A、B，求一个新集合C，集合C中的元素如果在A中，
# 则必不在B中，如果在B中，则必不在A中。且集合C中的元素要么是集合A的元素，
# 要么是集合B的元素

A = set([1,2,3])
B = set([2,3,4])
C = A-B
C.update(B-A)
print C

# 不可变集合：frozenset()
fs = frozenset([1,2,3])
print "fs:",fs

# 5、能够熟练进行字符串、列表、元组和set之间的转换。

ste1 = set('abcdefg')
print 'set:',ste1
print 'list:',list(ste1)
print 'tuple:',tuple(ste1)
# str1 = ''.join(ste1)
print ''.join(ste1)
s3 = set([1,2,3])
str2 = ''
for i in s3:
    str2 += str(i)#强制转换为字符串










