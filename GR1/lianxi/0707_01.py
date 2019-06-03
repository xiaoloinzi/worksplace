# encoding=utf-8
import multiprocessing
import time
from multiprocessing import Process,Value,Array,Lock

def fuc(num,lock):
    lock.acquire()
    print 'Hello Num:%s'%num
    lock.release()
if __name__=='__main__':
    lock = Lock()
    pro = [Process(target=fuc,args=(i,lock)) for i in xrange(50)]
    for i in pro:
        i.start()
        time.sleep(1)


class Count(object):
    def __init__(self,num):
        self.num = Value('i',num)
    def increment(self):
        self.num.value += 1
    def getValue(self):
        return self.num.value
def func1(counter,lock):
    with lock:
        # time.sleep(1)
        counter.increment()
if __name__=='__main__':
    lock = Lock()
    count = Count(0)
    pro = [Process(target=func1,args=(count,lock)) for i in xrange(50)]
    for i in pro:
        i.start()
    for i in pro:
        i.join()
    print count.getValue()

class Count(object):
    def __init__(self,num):
        self.num = num
    def increment(self):
        self.num += 1
        print self.num
    def getValue(self):
        return self.num
if __name__=='__main__':
    count = Count(2)
    list1 = []
    for i in xrange(50):
        list1.append(multiprocessing.Process(target=count.increment))
    for i in list1:
        i.start()
    for i in list1:
        i.join()
    # print count
    print count.getValue()

class Count(object):
    def __init__(self,num):
        self.num = multiprocessing.Value('i',num)

    def increment(self):
        self.num.value += 1
    def getValue(self):
        return self.num
if __name__=='__main__':
    count = 2
    list1 = []
    sun = Count(count)
    for i in xrange(50):
       list1.append( multiprocessing.Process(target=sun.increment))
    for i in list1:
        i.start()
    for i in list1:
        i.join()
    print count
    print sun.getValue().value

def func1(n,a):
    n = 3.14
    for i in range(len(a)):
        a[i] = - a[i]
if __name__=='__main__':
    num = 0
    arr = range(10)
    p = multiprocessing.Process(target=func1,args=(num,arr))
    p.start()
    p.join()
    print num
    print arr[:]











