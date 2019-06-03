#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 11:44
# @Author  : Lin
# @Site    : 
# @File    : test7.py
# @Software: PyCharm
#题目： 打印出如下图案（ 菱形）
# i = 1
# j = 3
# print ' '*(j),'*'*(i)
# i += 2
# j -= 1
# print ' '*(j),'*'*(i)
# i += 2
# j -= 1
# print ' '*(j),'*'*(i)
# i += 2
# j -= 1
# print ' '*(j),'*'*(i)
# if i == 7:
#     i -= 2
#     j += 1
#     print ' '*(j),'*'*(i)
#     i -= 2
#     j += 1
#     print ' '*(j),'*'*(i)
#     i -= 2
#     j += 1
#     print ' '*(j),'*'*(i)
#     i -= 2
#     j += 1
#     print ' '*(j),'*'*(i)

#方法2
from sys import stdout
for i in range(4):
    for j in range(2 -i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print
for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print
