#!E:/Program Files/python27
# -*- coding: utf-8 -*-
# @Time    : 2017/7/5
# @Author  : Lin
# @Site    :
# @File    : day_0628
# @Software: PyCharm
# 题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
# 　　　第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下
# 　　　的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

def taozi(n,x):
    while n!=0:
        print u'第%d天的桃子数%d'%(n,x)
        x = (x+1)*2
        n -= 1

if __name__=='__main__':
    taozi(10,1)













