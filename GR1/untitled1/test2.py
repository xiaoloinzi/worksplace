#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 11:08
# @Author  : Lin
# @Site    : 
# @File    : test2.py
# @Software: PyCharm
# number1 = raw_input('please enter a number1:')
# number2 = raw_input('please enter a number2:')
# number3 = raw_input('please enter a number3:')
# if number1 > number2:
#     if number2 > number3:
#         print number3,number2,number1
#     elif number1 > number3:
#         print number2,number3,number1
#     else:
#         print number2,number1,number3
# else:
#     if number3 > number2:
#         print number1,number2,number3
#     elif number3 > number1:
#         print number1,number3,number2
#     else:
#         print number3,number1,number2
#题目： 输入三个整数 x,y,z， 请把这三个数由小到大输出
# listB = [number1,number2,number3]
# listB.sort()
# print listB

listC = []
for i in range(3):
    number = int(raw_input('please enter you number:\n'))
    listC.append(number)
listC.sort()
print listC



