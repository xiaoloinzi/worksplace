#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 15:17
# @Author  : Lin
# @Site    : 
# @File    : test3.py
# @Software: PyCharm
#题目： 用*号输出字母 C 的图案。
import sys
acode = ['000000000',
         '001111110',
         '010000000',
         '100000000',
         '100000000',
         '010000000',
         '001111110',]
for line in acode:
    for c in line:
        if c == '0':
            print ' ',
        else:
            print '*',
    print




