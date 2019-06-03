#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/8 10:35
# @Author  : Lin
# @Site    : 
# @File    : class_init.py
# @Software: PyCharm
class Person():
    def __init__(self,name):
        #__init__方法在类的一个对象被建立时，马上运行。这个方法可以用来对你的对象做一些你希望的 初始
# 化 。注意，这个名称的开始和结尾都是双下划线。
        self.name = name
    def sayHi(self):
        print'Hello, my name is ',self.name
P = Person('Swaroop')
P.sayHi()
# This short example can also be written as
Person('Swaroop').sayHi()
