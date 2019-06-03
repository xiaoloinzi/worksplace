# encoding=utf-8
import multiprocessing
import time
from multiprocessing.managers import BaseManager


def func1(x):
    ret = []
    for i in xrange(x):
        ret.append(x**3)
    return ret
if __name__=='__main__':
    time1 = time.time()
    print 'time1',time1
    pool = multiprocessing.Pool(6)
    pool.map(func1,xrange(1000))
    time2 = time.time()
    print 'time2:',time2
    print 'pool:',time2-time1
    list1 = range(1000)
    list2 = [i**3 for i in list1]
    time3 = time.time()
    print 'time3:',time3
    print 'for :',time3-time2

def f(x,y):
    return x*y
if __name__=='__main__':
    pool = multiprocessing.Pool(5)
    result = pool.apply_async(f,args=(10,3))
    print result.get()
    # print pool.map(f,xrange(10))
    pool.close()
    pool.join()


class Emptyee(object):
    def __init__(self,name,salay):
        self.name = name
        self.salay = multiprocessing.Value('i',salay)
    def increment(self):
        self.salay.value += 100
    def getValue(self):
        return self.salay.value
def func1(lock,emp):
    with lock:
        emp.increment()
if __name__=='__main__':
    lock = multiprocessing.Lock()
    c1 = Emptyee('lin',3000)
    pro = [multiprocessing.Process(target=func1,args=(lock,c1)) for i in xrange(10)]
    for i in pro:
        i.start()
    for i in pro:
        i.join()
    print c1.getValue()

class Emptyee(object):
    def __init__(self,name,salay):
        self.name = name
        self.salay = salay
    def increment(self):
        self.salay += 100
    def getSalay(self):
        return self.salay
    def getName(self):
        return self.name
class Mymanager(BaseManager):
    pass
def manager():
    m = Mymanager()
    m.start()
    return m
Mymanager.register('Emptyee',Emptyee)
def func1(lock,emp):
    with lock:
        emp.increment()
if __name__=='__main__':
    lock = multiprocessing.Lock()
    emp = manager().Emptyee('lin',3000)
    pro = [multiprocessing.Process(target=func1,args=(lock,emp)) for i in xrange(10)]
    for i in pro:
        i.start()
    for i in pro:
        i.join()
    print emp.getName()
    print emp.getSalay()


class Count(object):
    def __init__(self,count):
        self.count = count
    def increment(self):
        self.count += 1
    def getValue(self):
        return self.count
class Mymaneger(BaseManager):
    pass

def manager2():
    m = Mymaneger()
    m.start()
    return m
Mymaneger.register('Count',Count)
def func1(lock,count):
    with lock:
        count.increment()
if __name__=='__main__':
    lock = multiprocessing.Lock()
    c1 = manager2().Count(1)
    pro = [multiprocessing.Process(target=func1,args=(lock,c1)) for i in xrange(20)]
    for i in pro:
        i.start()
    for i in pro:
        i.join()
    print c1.getValue()


class Count(object):
    def __init__(self,count):
        self.count = count
    def increment(self):
        self.count += 1
    def getValue(self):
        return self.count
class Mymaneger(BaseManager):
    pass
def Manger2():
    m = Mymaneger()
    m.start()
    return m
Mymaneger.register('Count',Count)
def func1(lock,count):
    with lock:
        count.increment()
if __name__=='__main__':
    lock = multiprocessing.Lock()
    c1 = Manger2().Count(2)
    pro = [multiprocessing.Process(target=func1,args=(lock,c1)) for i in xrange(10)]
    for i in pro:
        i.start()
    for i in pro:
        i.join()
    print c1.getValue()

def func1(shareDict,shareList,sharevalue,sharearray,lock,i):
    with lock:
        shareDict[i]=i
        for i in xrange(len(shareList)):
            shareList[i] += 1
        sharevalue.value += 1
        for i in xrange(len(sharearray)):
            sharearray[i] += 1
if __name__=='__main__':
    manager = multiprocessing.Manager()
    lock = multiprocessing.Lock()
    dict1 = manager.dict()
    list1 = manager.list(xrange(5))
    value1 = manager.Value('i',1)
    array1 = manager.Array('i',range(10))
    pro = [multiprocessing.Process(target=func1,args=(dict1,list1,value1,array1,lock,i)) for i in xrange(20)]
    for i in pro:
        i.start()
    for i in pro:
        i.join()
    print dict1
    print list1
    print value1.value
    print array1
    print 'end'







# def func1(shareDict,shareList):
#     shareDict[1] = 'a'
#     shareDict[2] = 'b'
#     print shareList[0]
#     shareList.reverse()
#     print shareList[0]
# def func2(shareDict,shareList):
#     shareDict[3] = 'c'
#     shareDict[4] = 'd'
#     shareList.append(20)
#     # print shareDict[2]
# if __name__=='__main__':
#     manager = multiprocessing.Manager()
#     list1 = manager.list(range(10))
#     dict1 = manager.dict()
#     p = multiprocessing.Process(target=func1,args=(dict1,list1))
#     p2 = multiprocessing.Process(target=func2,args=(dict1,list1))
#     p2.start()
#     time.sleep(2)
#     p.start()
#
#     p2.join()
#     p.join()
#     print dict1
#     print list1

# def printA(pipe):
#     for i in xrange(100):
#         pipe.send('I am A,this '+str(i))
#         res = pipe.recv()
#         with open('score3.txt','a+') as fp:
#             fp.write(res+'\n')
# def printB(pipe):
#     for i in xrange(100):
#         res = pipe.recv()
#         with open('fileB.txt','a+') as fp:
#             fp.write(res+'\n')
#         pipe.send(res+' is writen to filepath')
# if __name__=='__main__':
#     pipe = multiprocessing.Pipe()
#     p1 = multiprocessing.Process(target=printA,args=(pipe[0],))
#     p2 = multiprocessing.Process(target=printB,args=(pipe[1],))
#     p2.start()
#     time.sleep(1)
#     p1.start()
#     p2.join()
#     p1.join()
#     print 'end'







# def func1(pipe):
#     pipe.send('hello!')
#     print 'func1 received:%s'%pipe.recv()
#     pipe.send('what you name!')
#     print 'func1 received:%s'%pipe.recv()
#
# def func2(pipe):
#     print 'func2 received:%s'%pipe.recv()
#     pipe.send('hello too')
#     print 'func2 received:%s'%pipe.recv()
#     pipe.send("dont't tell you")
# if __name__=='__main__':
#     pipe = multiprocessing.Pipe()
#     p1 = multiprocessing.Process(target=func1,args=(pipe[0],))
#     p2 = multiprocessing.Process(target=func2,args=(pipe[1],))
#     p2.start()
#     time.sleep(1)
#     p1.start()
#     p2.join()
#     p1.join()
#     print 'end'
