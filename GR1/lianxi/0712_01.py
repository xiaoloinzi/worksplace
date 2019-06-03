# encoding=utf-8
from multiprocessing.dummy import Pool
import multiprocessing
import random
import Queue
import threading
import time

exitflag = False
def write(lcok,queue):
    while True:
        with lcok:
            data = random.randint(1,100)
            print threading.currentThread().name,' put is ',data
            queue.put(data)
            time.sleep(1)

def read(queue):
    while exitflag != True:
        print threading.currentThread().name,' put is ',queue.get()
        time.sleep(1)
if __name__=='__main__':
    queue = Queue.Queue()
    lock = threading.Lock()
    t1 = threading.Thread(target=write,args=(lock,queue))
    t2 = threading.Thread(target=write,args=(lock,queue))
    t3 = threading.Thread(target=read,args=(queue,))
    t1.start()
    t2.start()
    t3.start()
    time.sleep(10)
    exitflag = True
    t1.join()
    t2.join()
    t3.join()





def write(lock,queue):
    with lock:
        for i in xrange(5):
            print threading.currentThread().name,' put in queue is :',i
            queue.put(i)
            time.sleep(1)
def read(queue):
    def isEmpty(q):
        i = 0
        while i<5:
            if not q.empty():
                return False
            time.sleep(2)
            i += 1
        return True
    while not isEmpty(queue):
        print threading.currentThread().name,' get is :',queue.get()
        time.sleep(1)

if __name__=='__main__':
    queue = Queue.Queue()
    lock = threading.Lock()
    t1 = threading.Thread(target=write,args=(lock,queue))
    t2 = threading.Thread(target=write,args=(lock,queue))
    t3 = threading.Thread(target=read,args=(queue,))
    t1.start()
    t2.start()
    t3.start()
    time.sleep(3)
    t1.join()
    t2.join()
    t3.join()

def write(lock,queue):
    while True:
        with lock:
            i = random.randint(1,100)
            print threading.currentThread().name,' put is :',i
            queue.put(i)
            time.sleep(1)
def read(queue):
    while True:
        print threading.currentThread().name,' get is :',queue.get()
        time.sleep(1)


if __name__=='__main__':
    queue = Queue.Queue()
    lock = threading.Lock()
    t1 = threading.Thread(target=write,args=(lock,queue))
    t2 = threading.Thread(target=write,args=(lock,queue))
    t3 = threading.Thread(target=read,args=(queue,))
    t1.start()
    t2.start()
    t3.start()
    time.sleep(5)
    t1.join()
    t2.join()
    t3.join()

g = 0
def add(lock,a,b):
    with lock:
        global g
        g += a+b
if __name__=='__main__':
    list1 = []
    lock = threading.Lock()
    for i in xrange(20):
        list1.append(threading.Thread(target=add,args=(lock,i,i+1)))
    for i in list1:
        i.start()
    for i in list1:
        i.join()
    print g

def func(a):
    return a**3
if __name__=='__main__':
    pl = Pool(multiprocessing.cpu_count()-2)
    list2 = pl.map(func,xrange(10))
    print list2

def fucn(a):
    time.sleep(1)
    a += 1
    print a
    return a
if __name__=='__main__':
    list1 = [1,2,3,4,5]
    pl = Pool(5)
    listb = pl.map(fucn,list1)
    pl.close()
    pl.join()
    print listb













