#!E:/Program Files/python27
# -*- coding: utf-8 -*-
# @Time    : 2017/7/5
# @Author  : Lin
# @Site    :
# @File    : day_0621
# @Software: PyCharm
# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
# 　　　第10次落地时，共经过多少米？第10次反弹多高？
x = 100
a = 100
for i in xrange(1,10):
    if i == 9:
        x = x/2.0
        a += x
        print u'第10次反弹:',x
    else:
        x = x/2.0
        a += x*2.0
print u'第10次落地时，共经过%0.2f米？'%a
