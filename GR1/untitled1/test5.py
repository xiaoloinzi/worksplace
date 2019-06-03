#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 12:24
# @Author  : Lin
# @Site    : 
# @File    : test5.py
# @Software: PyCharm
#题目： 判断 101-200 之间有多少个素数， 并输出所有素数。
listD = []
i = 101
while (i < 200):
    j = 2
    while(j <= (i/j)):
        if not(i%j):break
        j = j + 1
    if (j > i/j):
        print i,u'是素数'
        listD.append(i)
    i = i + 1
print u'总共',len(listD),u'个素数'
#方法2
h = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(101,201):
    k = int(sqrt(m +1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print '%-4d'%m
        h += 1
        if h % 10 == 0:
            print ''
    leap = 1
print 'The total is %d'%h