#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 9:55
# @Author  : Lin
# @Site    : 
# @File    : test1.py
# @Software: PyCharm
# d=[1,2,3,4]
# def getnum(num,digit,length):
#     num1=num
#     for i in range(len(digit)):
#         num=num1*10+digit[i]
#         if length==3:
#             yield num
#         elif length<3:
#             for j in  getnum(num,digit[:i]+digit[i+1:],length+1):
#                 yield j
# digit=list(getnum(0,d,1))
# print u"%r 共可以组成%d个三位数字 "%(d,len(digit))
# print u"它们是:%r"%digit
#题目： 有 1、 2、 3、 4 个数字， 能组成多少个互不相同且无重复数字的三位数？ 都是多少？
listA = []
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if( a != c ) and (a != b) and (b != c):
                listA.append(a*100+b*10+c)
print u'有 1、 2、 3、 4 个数字， 能组成',len(listA),u'个互不相同且无重复数字的三位数，分别是',listA






