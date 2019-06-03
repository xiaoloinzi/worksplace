#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 12:07
# @Author  : Lin
# @Site    : 
# @File    : test8.py
# @Software: PyCharm
#题目： 求 1+2!+3!+...+20!的和
#方法1
s = 0
t = 1
for i in range(1,21):
    t *= i
    s +=t
print s
#方法2
s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1,x + 1):
        r *= i
    return r
sun = sum(map(op,l))
print sun