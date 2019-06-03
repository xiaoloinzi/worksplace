#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/8 13:54
# @Author  : Lin
# @Site    : 
# @File    : try_except.py
# @Software: PyCharm
import sys
try:
    s = raw_input('Enter somethiing-->')
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit()#exit the program
except:
    print '\nSome error/exception occcurred.'
    #here,we are not exiting the program
print 'Done'