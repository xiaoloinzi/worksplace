#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 15:26
# @Author  : Lin
# @Site    : 
# @File    : test4.py
# @Software: PyCharm
#题目： 古典问题： 有一对兔子， 从出生后第 3 个月起每个月都生一对兔子， 小兔子长到第三
#个月后每个月又生一对兔子， 假如兔子都不死， 问每个月的兔子总数为多少？
rabbit1 = 1
rabbit2 = 1
for i in range(1,22):
    print '%d %d'%(rabbit1,rabbit2),
    if(i % 3)==0:
        print ''
    rabbit1 = rabbit1 + rabbit2
    rabbit2 = rabbit1 + rabbit2

