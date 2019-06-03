#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/8 14:24
# @Author  : Lin
# @Site    : 
# @File    : finally.py
# @Software: PyCharm
import time
try:
    f = file('poem.txt')
    while True:
        line = f.readline()
        if len(line) ==0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print 'Cleaning up ...closed the file'
