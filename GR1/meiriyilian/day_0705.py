#!E:/Program Files/python27
# -*- coding: utf-8 -*-
# @Time    : 2017/7/5
# @Author  : Lin
# @Site    :
# @File    : day_0705
# @Software: PyCharm
import threading
import time
from Queue import Queue

# 每日一练：使用生产者方式实现多线程写队列和读队列
# 要求：边读边写

class Producer(threading.Thread):
    def __init__(self,qname,queue):
        threading.Thread.__init__(self,name=qname)
        self.queue = queue

    def run(self):
        for i in range(5):
            print '%s is producing %d to rhe queue!\n'%(self.getName(),i)
            self.queue.put(i)
            time.sleep(1)
        print '%s put finished!'%self.getName()
class Consumer(threading.Thread):
    def __init__(self,qname,queue):
        threading.Thread.__init__(self,name=qname)
        self.queue = queue

    def run(self):
        for i in range(5):
            num = self.queue.get()
            print '%s is consumine %d to rhe queue!\n'%(self.getName(),num)
            time.sleep(3)
        print '%s get finished!'%self.getName()

if __name__=='__main__':
    q = Queue()
    pro = Producer('Pro',q)
    con = Consumer('Con',q)
    pro.start()
    con.start()
    pro.join()
    con.join()
    print 'end'






