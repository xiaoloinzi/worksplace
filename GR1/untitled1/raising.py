#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/8 14:09
# @Author  : Lin
# @Site    : 
# @File    : raising.py
# @Software: PyCharm
class ShortInputException(Exception):
    '''A user-defined exception class'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    s = raw_input('Enter something-->')
    if len(s) < 3:
        raise ShortInputException(len(s),3)

except EOFError:
    print '\nwhy did you do an EOF on me ?'
except ShortInputException,x:
    print 'ShortInputException: The input was of length %d,was excecting at leasr %d'%(x.length,x.atleast)
else:
    print 'No exception was raised'