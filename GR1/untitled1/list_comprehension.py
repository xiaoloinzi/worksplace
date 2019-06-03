#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/8 18:02
# @Author  : Lin
# @Site    : 
# @File    : list_comprehension.py
# @Software: PyCharm
listone = [9,3,4]
listtwo = [2*i for i in listone if i>2]
print listtwo
print listone

for i in range(1,100):
    print i
#一次读入文件的所有行，然后关闭文件，再迭代每行输出，这样写代码
#的好处是能够快速完整的访问文件，内容输出和文件访问不必交替进行
#file（）内建函数是最近才添加到python当中的，它的功能等同于open（），不过file（）。
filename = raw_input('enter file name:')
fobj = open(filename,'r')
for eachLine in fobj:
    print eachLine,
fobj.close()
try:
    filename = raw_input('enter file name :')
    fojb = open(filename,'r')
    print eachLine,fobj.close()
except IOError,e:
    print 'file open error:',e