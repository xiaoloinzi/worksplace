#!E:/Program Files/python27
# -*- coding: utf-8 -*-
# @Time    : 2017/7/6
# @Author  : Lin
# @Site    :
# @File    : day_0707
# @Software: PyCharm
from Queue import Queue
import threading
import random
import time
# 每日一练：
# 3、实现多线程入队列，然后按规则出队列
#       要求：
#       1）实现一个线程不断生成一个随机数到一个队列中(考虑使用Queue    这个模块)
#       2）实现一个线程从上面的队列里面不断的取出奇数
#       3）实现另外一个线程从上面的队列里面不断取出偶数

def write(q1):
    s = 50
    while s != 0:
        res = random.randint(1,50)
        q1.put(res)
        s -= 1
    time.sleep(3)
def read1(q,lock):
    # with lock:
    threads = threading.currentThread()
    for i in xrange(25):
        res = q.get()
        if res%2==0:
            print threads.name,':',res
def read2(q,lock):
    # with lock:
    threads = threading.currentThread()
    for i in xrange(25):
        res = q.get()
        if res%2!=0:
            print threads.name,':',res
    # print threads.name,':',q2.put()
if __name__=='__main__':
    lock = threading.Lock()
    que1 = Queue()
    thread1 = threading.Thread(target=write,args=(que1,))
    thread2 = threading.Thread(target=read1,args=(que1,lock))
    thread3 = threading.Thread(target=read2,args=(que1,lock))
    thread1.start()
    thread2.start()
    thread3.start()
    time.sleep(1)
    thread1.join()
    thread2.join()
    thread3.join()
    print 'end'

