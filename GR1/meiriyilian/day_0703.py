#!E:/Program Files/python27
# -*- coding: utf-8 -*-
# @Time    : 2017/7/5
# @Author  : Lin
# @Site    :
# @File    : day_0703
# @Software: PyCharm
import threading
import time
# 每日一练：1、使用多线程交替打印数字
#      要求：
#       1）线程1只打印奇数，线程2只打印偶数
#       2）要求打印1、2、3、4、5、6、7……

def printPrint(list1):
    for i in list1:
        print threading.currentThread().name,':',i
        time.sleep(1)

if __name__=='__main__':
    prto1 = threading.Thread(target=printPrint,args=(xrange(1,20,2),))
    prto2 = threading.Thread(target=printPrint,args=(xrange(2,20,2),))
    prto1.start()
    prto2.start()
    prto1.join()
    prto2.join()

