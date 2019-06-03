#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/8 12:29
# @Author  : Lin
# @Site    : 
# @File    : pickling.py
# @Software: PyCharm
import cPickle as P
#import cPickle as P
shoplistfile = 'shoplist.data'
#the name of the file where we will store the object
shoplist = ['apple','mango','carrot']
# 为了在文件里储存一个对象，首先以写模式打开一个file对象，然后调用储存器模块的dump函数，把对
# 象储存到打开的文件中。这个过程称为 储存 。
#write to the file
f = file(shoplistfile,'w')
P.dump(shoplist,f)#dump the object to a file
f.close()

del shoplist#remove the shoplist

#Read back from the storage
f = file(shoplistfile)
storedlist = P.load(f)
print storedlist