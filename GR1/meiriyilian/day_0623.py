#!E:/Program Files/python27
# -*- coding: utf-8 -*-
# @Time    : 2017/7/5
# @Author  : Lin
# @Site    :
# @File    : day_0623
# @Software: PyCharm
# 题目：从键盘输入一些字符，逐个把它们送到磁盘上去，直到输入字符包含#号为止。

def printstr():
    while True:
        str = raw_input(u'请输入字符：')
        if str == '#':
            return
        with open('file1.txt','a') as fp:
            fp.write(str+'\n')

if __name__=='__main__':
    printstr()










