# encoding=utf-8
import time
import multiprocessing
from multiprocessing import Process,Pool,Lock,Pipe,Manager
from multiprocessing.managers import BaseManager
import random

# Semphore--生成N把锁
# Lock --生成一把锁

def woek(s,i):
    s.acquire()
    print multiprocessing.current_process().name+'acquire'
    time.sleep(i)
    time.sleep(10)
    print multiprocessing.current_process().name+'release'
    s.release()

if __name__=='__main__':
    s = multiprocessing.Semaphore(4)
    for i in xrange(7):
        p = Process(target=woek,args=(s,i))
        p.start()

# 习题：针对上题中的getValue方法，允许同时3个进程同时读取
# 使用Semaphore进行控制

class Count(object):
    def __init__(self,num):
        self.num = multiprocessing.Value('i',num)

    def increase(self):
        self.num.value += 1

    def getValue(self):
        return self.num.value

def func(counter,lock):
    lock.acquire()#获得锁
    # time.sleep(0.1)
    counter.increase()
    print counter.getValue()
    time.sleep(10)
    lock.release()#释放锁
#
#
if __name__=='__main__':
    s = multiprocessing.Semaphore(3)#创建一个共享锁
    c1 = Count(0)
    procs = [multiprocessing.Process(target=func,args=(c1,s)) for i in range(50)]
    for i in procs:
        i.start()
    for i in procs:
        i.join()

# 老师的方法：


class Count(object):
    def __init__(self,num):
        self.num = multiprocessing.Value('i',num)

    def increase(self):
        self.num.value += 1

    def getValue(self):
        return self.num.value

def func(counter):
    time.sleep(0.1)
    counter.increase()

def func2(counter,s):
    with s:
        print '---read---'
        time.sleep(2)
        return counter.getValue()


if __name__=='__main__':
    s = multiprocessing.Semaphore(3)#创建3个共享锁
    c1 = Count(0)
    procs = [multiprocessing.Process(target=func2,args=(c1,s)) for i in range(20)]
    for i in procs:
        i.start()
    for i in procs:
        i.join()
    for i in procs:
        print i.exitcode
    print c1.getValue()


#Queue--先进先出，put--把变量放到队列中，get--从队列取变量，empty（）判断队列是否为空
# 队列中加参数，表示队列的长度，不加默认不限长
def offer(queue):
    queue.put('hello world')

def write(q):
    for value in ['A','B','C']:
        print ' put %s to queue..'%value
        q.put(value)
        time.sleep(2)

def read(q):
    # time.sleep(3)#设置等待写的时间
    #循环等待

#把read方法用循环等待的方式进行读（重点）
    def isEmpty(q):
        i = 0
        while i<5:
            if not q.empty():
                return False
            time.sleep(2)
            i += 1
        return True

    while not isEmpty(q):
        print 'get %s from queue.'%q.get()
        time.sleep(1)

if __name__=='__main__':
    q = multiprocessing.Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    # print q.get()

# 问题：队列和lock以及信号量的使用场景区别
# 对不同的值采取不同的队列

# 习题：使用Queue实现多进程，进程A向队列中放入数据，分别是数字、字符串、
# 数字和字符串混合，进程B从里面获取，如果是字符串，则打印，其他则写文件

def write(q):
    listc = [1,'a',[1,'a']]
    for i in listc:
        q.put(i)

def read(q):
    def isEmty(q):
        i = 0
        while i < 5:
            if not q.empty():
                return False
            time.sleep(2)
            i += 1
        return True

    while not isEmty(q):
        s = q.get()
        if isinstance(s,str):
            print u'字符串：',s
        elif isinstance(s,list):
            for i in s:
                with open('queue.txt','a') as fp:
                    fp.write(str(i)+'\n')
        elif isinstance(s,int):
            with open('queue.txt','a') as fp:
                    fp.write(str(s)+'\n')
#
#
if __name__=='__main__':
    q = multiprocessing.Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pr.join()
    pw.join()

# 老师的方法：
def write(q):
    for i in [1,'B','123']:
        print 'put %s to queue...'%i
        q.put(i)
        time.sleep(2)

def read(q):
    def isEmty(q):
        i = 0
        while i < 5:
            if not q.empty():
                return False
            time.sleep(2)
            i += 1
        return True

    while not isEmty(q):
        s = q.get()
        if type(s)== str and s.isdigit():
            print 'get %s from queue.'%s
        else:
            print 'write to file'
            with open('queue.txt','a+') as fp:
                fp.write(str(s))



if __name__=='__main__':
    q = multiprocessing.Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pr.join()
    pw.join()

#锁，事件，Event:轻量级协同类，：set(设置信号量),
# is_set(是否设置),wait([time等待多长时间])，
# clear(设置的事件清除掉)

def waitForEvent(e):
    print 'wait for event starting No timeout'
    e.wait()#没有填时间表示为主差事，
    # 如果事件没有发生，会一直等待下去，直到天长地久
    print 'the event has happened.',e.is_set()

def waitForEventTimeout(e,t):
    print 'wait for event starting Timeout is ',t
    e.wait(t)#没有填时间表示为主差事，
    # 如果事件没有发生，会一直等待下去，直到天长地久
    print 'the event is:',e.is_set()
#
if __name__=='__main__':
    e = multiprocessing.Event()
    print 'the event is_set is',e.is_set()
    # p1 = Process(target=waitForEvent,args=(e,))
    # p1.start()
    # time.sleep(3)
    # e.set()
    p1 = Process(target=waitForEventTimeout,args=(e,2))
    p1.start()
    time.sleep(3)
    e.set()
# 结果：the event is_set is False
# wait for event starting Timeout is  1
# the event is: False
# 解释：e.wait(2)指定的是2秒，在2秒内，主进程还没有到e.set()这个方法
# 没有走到的时候，waitForEventTimeout()就已经超时了，超时之后就继续往下走
# 往下走的时候，e.is_set()返回False
#
# 使用场景：如果两个进程之间的处理逻辑依赖于特定的事件发生，
# 如：到了下课的时间需要放一段音乐，那么这个事件就可以设置为时间，到没到下课时间，
# 假如到下课时间，那我另外一个进程就监听这个事件，如果这个时间一到，代码
# 分支就是放一段音乐。

# Pipe管道：
# pipe = Pipe()；返回两个端口：在pipe[0]里面去send()或者recv()
# 在pipe[0]里面去send()的数据是在pipe[1]里面recv()取到的
# pipe[1]和pipe[0]一样
# send()
#recv()

def func1(pipe):
    pipe.send('hello')
    print 'func1 recevied:%s',pipe.recv()
    pipe.send('what is your name?')
    print 'func1 received :%s'%pipe.recv()

def func2(pipe):
    print 'func2 recevied:%s',pipe.recv()
    pipe.send('hello too')
    print 'func2 received :%s'%pipe.recv()
    pipe.send("I don't tell you!")

if __name__=='__main__':
    pipe = Pipe()#上面传入的参数必须和管道的变量一致
    print len(pipe)
    p1 = Process(target=func1,args=(pipe[0],))
    p2 = Process(target=func2,args=(pipe[1],))
    p2.start()
    time.sleep(0.1)
    p1.start()
    p2.join()
    p1.join()

# A进程给B进程发送100条消息，B进程把内容全部写入文件
# B进程每写一个文件，则给A回复一条XXX is writen to fulePath
# 的消息，A进程把这个消息也写文件

def func1(pipe):
    for i in xrange(100):
        pipe.send(str(i)+'hello')
    for i in xrange(100):
        s = pipe.recv()
        with open('A.txt','a+') as fp:
            fp .write(s+'\n')

def func2(pipe):
    for i in xrange(100):
        s = pipe.recv()
        with open('B.txt','a+') as fp:
            fp .write(s+'\n')
            e = s + 'is writen to filePath'
            pipe.send(e+'\n')

if __name__=='__main__':
    pipe = Pipe()#上面传入的参数必须和管道的变量一致
    print len(pipe)
    p1 = Process(target=func1,args=(pipe[0],))
    p2 = Process(target=func2,args=(pipe[1],))
    p2.start()
    time.sleep(0.1)
    p1.start()
    p2.join()
    p1.join()

# 老师的方法：
def func1(pipe):
    for i in xrange(100):
        time.sleep(0.01)
        sendStr = 'msg'+str(i)
        pipe.send(sendStr)
        rcv = pipe.recv()
        with open('c.txt','a+') as fp:
            fp .write(str(rcv)+'\n')

def func2(pipe):
    for i in xrange(100):
        time.sleep(0.01)
        rcv = pipe.recv()
        with open('D.txt','a+') as fp:
            fp .write(rcv+'\n')
            pipe.send(str(rcv)+'is writen to D.txt')

if __name__=='__main__':
    pipe = Pipe()#上面传入的参数必须和管道的变量一致
    print len(pipe)
    p1 = Process(target=func1,args=(pipe[0],))
    p2 = Process(target=func2,args=(pipe[1],))
    p2.start()
    time.sleep(0.1)
    p1.start()
    p2.join()
    p1.join()

# Value、Array()通过共享内存的方式共享数据
# Manger()在后台以进程的形式存在，程序中会有一个独立的进程，
# 这个进程就是Manage进程，在Manage（）进程中就存放了我们所有的一些需要共享
# 的变量，表示的范围广，可以表示Value，也可以表示Array（），
# 还可以表示dict、list、Lock、Samphor等


def f(shareDict,shareList):
    shareDict[1] = '1'
    shareDict[2] = '2'
    shareList.reverse()

if __name__=='__main__':
    manager = Manager()
    dict1 = manager.dict()
    list1 = manager.list(range(5))
    p = Process(target=f,args=(dict1,list1))
    p.start()
    p.join()
    print dict1
    print list1

# 习题：通过manager共享如下类型的数据，list、dict、value、Array，
# 在子进程中，对于list以及Value中所有的整数加1，并发20个进程，
# 做好写锁控制。最后在主进程中，打印这些数据。

def f(lock,shareValue,shareList):
    with lock:
        shareValue.value += 1
        for i in xrange(len(shareList)):
            shareList[i] += 1

if __name__=='__main__':
    manager = Manager()
    dict1 = manager.dict()
    list1 = manager.list(range(5))
    value1 = manager.Value('i',0)
    array1 = manager.Array('i',range(10))
    lock = manager.Lock()
    procs = [Process(target=f,args=(lock,value1,list1)) for i in xrange(20)]
    for i in procs:
        i.start()
    for i in procs:
        i.join()
    print dict1
    print list1
    print array1
    print value1.value


class Count(object):
    def __init__(self,count= 0):
        self.count = count

    def increment(self):
        self.count += 1

    def getVal(self):
        return self.count

class MyManger(BaseManager):
    #重新创建一个类继承BaseManager的目的是新加的类型不会对Python的库有影响
    pass

def Manger2():
    m = MyManger()
    m.start()
    return m

MyManger.register('Count',Count)

def func1(counter,lock):
    with lock:
        counter.increment()

if __name__=='__main__':
    manager = Manger2()
    c1 = manager.Count(2)
    lock = Lock()
    procs = [Process(target=func1,args=(c1,lock)) for i in xrange(10)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print c1.getVal()


# 习题：针对雇员类，初始化工资是3000，实现一个雇员在10个进程中加薪
# 每次加薪100元，最后打印出该雇员的最新工资
class Count(object):
    def __init__(self,count= 0):
        self.count = count

    def increment(self):
        self.count += 100

    def getVal(self):
        print u'雇员的最新工资为：',
        return self.count

class MyManger(BaseManager):
    #重新创建一个类继承BaseManager的目的是新加的类型不会对Python的库有影响
    pass

def Manger2():
    m = MyManger()
    m.start()#后台的进程做一个变量的共享
    return m

MyManger.register('Count',Count)

def func1(counter,lock):
    with lock:
        counter.increment()

if __name__=='__main__':
    manager = Manger2()
    c1 = manager.Count(3000)
    lock = Lock()
    procs = [Process(target=func1,args=(c1,lock)) for i in xrange(10)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print c1.getVal()

def f(x):
    return x*x*x

if __name__=='__main__':
    pool = Pool(5)
    result = pool.apply_async(f,args=(10,))
    print result.get()
    print pool.map(f,range(10))
    pool.close()
    pool.join()

# 习题：计算10000000个数的3次方，分别用单进程和进程池计算，的出时间差异
def f(s):
    for i in xrange(1,10000001):
        s += i**3
    return s

if __name__=='__main__':
    time1 = time.clock()
    pool = Pool(multiprocessing.cpu_count()-1)
    result = pool.apply_async(f,args=(0,))#进程池
    print result.get()
    # print pool.map(f,range(10000000))#进程池
    pool.close()
    pool.join()
    time2 = time.clock()
    timepool = time2-time1
    print u'进程池的时间：',timepool
    proce = Process(target=f,args=(0,))
    proce.start()
    proce.join()
    time3 = time.clock()
    timeProcess = time3-time2
    print u'单进程的时间：',timeProcess
    print U'进程池和单进程的时间差：',timepool-timeProcess

# 老师的方法：

def f(x):
    ret = []
    for i in xrange(x):
        ret.append(x*3)
    return ret

if __name__=='__main__':
    t1 = time.time()
    list1 = range(1000)
    list2 = [1**3 for i in list1]
    t2 = time.time()
    print t2 - t1

    t3 = time.time()
    pool = Pool(6)
    result = pool.map(f,range(1000))
    pool.close()
    pool.join()
    t4 = time.time()
    print t4-t3

print multiprocessing.cpu_count()#计算机的核数


















