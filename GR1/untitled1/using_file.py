#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/8 12:04
# @Author  : Lin
# @Site    : 
# @File    : using_file.py
# @Software: PyCharm
poem = '''\
Programming is fun
when the work is done
if yo wanna make your work also fun:
        use Python!
        '''
f = file('poem.txt','w')#open for 'w'riting
f.write(poem)#wtite text to file
f.close()#close the file

f = file('poem.txt')
#if no mode is specified ,'r'ead mode is addumed by default
while True:
    line = f.readline()
    print len(line)
    if len(line) == 0:#zero lenght indicates EOF
        break
    print line,
    #Notice comma to avoid automatic newline added by Python
f.close()#close the file
