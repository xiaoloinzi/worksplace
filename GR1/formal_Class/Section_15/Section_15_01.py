# encoding=utf-8
from Queue import Queue


# python 多进程 和 多线程
#
# GIL：同一个时间点只有一个线程在cpu上运行：多核的优势没有发挥出来
# 程序：
# 1、cpu密集型 -> 多进程
# 2、IO密集型 -> 多线程
#
# 多进程和多线程的区别：
# 进程：
# 1、PCB
# 2、文本区域
# 3、数据区域
# 4、堆栈
# p1 p2
#
# 线程：只是一个执行流
#
# 问题：
# 1、多进程编程时，在进程之间共享数据，通过什么方式
# 1）通过共享内存的方式。Value、Array
# 2）通过后台进程的方式。Manger
#
# 问题：
# 1、在多线程编程时，如何共享数据
# thread1 thread2 thread3
#
# var1 = 1
#
# def func1():
# 	var1 = 2
#
# t1 = Thread(target=func1,args=(xx,))
# t2 =
#
# def func1():
# 	xxx
# 	ret = func2()
#
# if __name__ == __main__:
# 	func1()
import threading
import time

def func1(a = None,b=None):
    print a,b
    time.sleep(1)

if __name__=='__main__':
    t1 = threading.Thread(target=func1,args=('Hello','world'))
    print t1.isAlive()
    print t1.getName()
    t1.setName('test1')
    print t1.getName()
    t1.start()
    time.sleep(1.1)
    print t1.isAlive()
    t1.join()

def func1(a=None, b=None):
    print a,b
    print 'enter func1'
    time.sleep(5)
    print 'exit func1'

t1 = threading.Thread(target=func1, args=('Hello ','World!'))
print t1.isAlive()
print t1.getName()
t1.setDaemon(True)
print 'daemon:',t1.isDaemon()
t1.setName('test1')
print t1.getName()
t1.start()
time.sleep(1.1)
print t1.isAlive()
print 'main thread end'

# 习题：两个线程，线程A打印enter，exit，中间sleep 10 s，
# 线程B打印enter，exit，中间休眠7s，
# 线程A设置成daemon，线程B不设置。分别运行，并解释执行结果


def func1(a=None):
    print a
    print 'enter A'
    time.sleep(10)
    print 'exit A'

def func2(b=None):
    print b
    print 'enter B'
    time.sleep(7)
    print 'exit B'
if __name__=='__main__':
    ta = threading.Thread(target=func1, args=('ThreadA',))
    tb = threading.Thread(target=func2,args=('ThreadB',))

    ta.setDaemon(True)
    ta.start()
    print 'ta:',ta.isAlive()
    tb.start()
    print 'ta:',ta.isAlive()
    print 'tb:',tb.isAlive()
    ta.join()#就算是守护线程的子线程，也会等待他结束
# 主线程的结束判断是，只要主线程中除了需要守护的子线程之外的
# 其他逻辑程序都已经结束完成了，主线程也就意味的结束了

# 习题：线程之间之间，是可以嵌套的。创建一个线程A，其参数是
# 另外一个线程B
# ，在线程A的方法中启动线程B，并且等待线程B执行结束

def fun1(s):
    print 'enter t1'
    s.start()
    s.join()
    print 'end t1'

def func2():
    print 't1'
    time.sleep(1)
    print '........'


t1 = threading.Thread(target=func2)
t2 = threading.Thread(target=fun1,args=(t1,))
t2.start()
time.sleep(3)
print 'end'

# 重写run方法：
class MyThread(threading.Thread):
    def __init__(self,a):
        threading.Thread.__init__(self)
        self.a = a

    def run(self):
        print 'now sleep ',self.a,' seconds'
        time.sleep(2)
        print 'sleep end'

t1 = MyThread(3)
t2 = MyThread(2)
t1.start()
t2.start()
t1.join()
t2.join()





# 习题：
# 在重写Thread类的方式中，如何完成给函数传入参数。
# 例如：线程MyThread，是做一个加法操作，完成2046 + 1024 的结果计算
class MyThread(threading.Thread) :
    def __init__(self, a,b) :
        super(MyThread,self).__init__()
        self.a = a
        self.b = b
    def run(self) :
        self.sum = self.a + self.b
        print '%d+%d=%d'%(self.a,self.b,self.sum)

if __name__=='__main__':
    t1 = MyThread(2046,1024)
    t1.start()
    t1.join()




# 生产者与消费者
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self,name=t_name)
        self.data = queue

    def run(self):
        for i in xrange(5):
            print '%s:%s is producing %d to the queue!\n'%(time.ctime(),self.getName(),i)
            self.data.put(i)
            time.sleep(3)
        print '%s:%s put finished!\n'%(time.ctime(),self.getName())

class Consumer(threading.Thread):
    def __init__(self,t_name, queue):
        threading.Thread.__init__(self,name=t_name)
        self.data = queue

    def run(self):
        for i in xrange(5):
            val = self.data.get()
            print '%s:%s is consumer %d in the queue!\n'%(time.ctime(),self.getName(),val)
            time.sleep(2)
        print '%s:%s consumer finished!\n'%(time.ctime(),self.getName())

if __name__ == '__main__':
    queue = Queue()
    producer = Producer('Pro',queue)
    consumer = Consumer('Con',queue)
    producer.start()
    time.sleep(1)
    consumer.start()
    producer.join()
    consumer.join()
    print 'mainThread end'

# 习题：把生产者、消费者模式，使用方式一重写

def run1(q):
    for i in xrange(5):
        q.put(i)
        print 'pro ',i
        time.sleep(3)


def run2(q):
    for i in xrange(5):
        val = q.get()
        print 'con ',i
        time.sleep(2)

if __name__ == '__main__':
    queue = Queue()
    producer = threading.Thread(target=run1,args=(queue,))
    consumer = threading.Thread(target=run2,args=(queue,))
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print 'mainThread end'

# 隐含问题：
# 对于线程的执行结果，主线程如何获取？
# 1、通过队列的方式
# 2、通过全局变量的方式

# class MyThread(threading.Thread):
    def __init__(self,a,b,q):
        threading.Thread.__init__(self)
        self.a = a
        self.b = b
        self.q = q

    def run(self):
        ret  = self.a + self.b
        print ret
        self.q.put(ret)
        self.retcode = ret

if __name__=='__main__':
    t0 = threading.currentThread()
    print t0
    q = Queue()
    t1 = MyThread(2046,1024,q)
    t1.start()
    t1.join()
    print t1.q.get()
    print t1.retcode

g = 1
def add(a,b):
    global g
    g += (a+b)
t1 = threading.Thread(target=add,args=(12,34))
t2 = threading.Thread(target=add,args=(12,30))
t1.start()

t1.join()
t2.start()
t2.join()
print g


# 主线程和子线程的区别
def func():
    thread = threading.currentThread()
    print 'this is ',thread.getName()
    time.sleep(10)

if __name__=='__main__':
    t1 = threading.Thread(target=func)
    t1.start()
    t2 = threading.Thread(target=func)
    t2.start()
    thd = threading.currentThread()
    print 'this is ',thd.getName()
    t1.join()
    t2.join()


class MyThread(threading.Thread):
    def __init__(self,a,b,q):
        threading.Thread.__init__(self)
        self.a = a
        self.b = b
        self.q = q

    def run(self):
        ret  = self.a + self.b
        for i in range(5):
            ret  += (self.a + self.b)
            self.q.put(ret)
            self.retcode = ret

if __name__=='__main__':
    t0 = threading.currentThread()
    print t0
    q = Queue()
    t1 = MyThread(2046,1024,q)
    t1.start()
    t1.join()
    # print t1.q.get()
    for i in range(5):
        print t1.q.get()
from multiprocessing.dummy import Pool
import multiprocessing

def func(a):
    time.sleep(1)
    a += 1
    # print a#[none,none,none,none,none]
    return a#返回值自增1

if __name__=='__main__':
    lista = [1,2,3,4,5]
    pool =  Pool(5)
    listb = pool.map(func,lista)
    pool.close()
    pool.join()
    print listb


# 针对线程池，做如下的练习：
# 1、计算x**3次方，原始列表是xrange(10)
def func(a):
    time.sleep(1)
    # print a#[none,none,none,none,none]
    return a**3

if __name__=='__main__':
    pool =  Pool(5)
    lista = xrange(10)
    listb = pool.map(func,lista)
    pool.close()
    pool.join()
    print listb

Even
g = 0
def add(event,a,b):
    print 'now enter wait'
    event.wait()
    time.sleep(2)
    global g
    g += a + b

if __name__ == '__main__':
    tList = []
    e = threading.Event()
    # con = threading.Condition()
    # con.notify()
    print e.isSet()
    for i in xrange(1):
        tList.append(threading.Thread(target=add,args=(e,1,1)))
    for t in tList:
        t.start()
    time.sleep(2)
    print 'the thread Thread-1 is waiting'
    print g
    e.set()
    print g
    for t in tList:
        t.join()
    print g


# 习题：
# 3个线程
# T1：向队列写数据
# T2：向队列写数据
# T3: 读取队列中的数据
# 要求:
# 1、T1 和T2 需要加锁写
# 2、T3读不用加锁
# 3、控制三个线程的结束时间

def writ(lock,q,a,b):
    with lock:
        q.put(a)
        time.sleep(b)

def read(q):
    while not q.empty():
        print q.get()
        time.sleep(2)

if __name__=='__main__':
    q = Queue()
    lock = threading.Lock()
    t1 = threading.Thread(target=writ,args=(lock,q,'t1',2))
    t2 = threading.Thread(target=writ,args=(lock,q,'t2',2))
    t3 = threading.Thread(target=read,args=(q,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

import threading,time,Queue,random
# 老师的方法1
exitFlag = False
def write(lock,queue):
    while exitFlag != True:
        with lock:
            thread = threading.currentThread()
            data = random.randint(1,100)
            print'this is thread:',thread.getName() ,'put:',data
            queue.put(data)
            time.sleep(1)

def read(queue):
    while exitFlag != True:
        print 'get:',queue.get()
        time.sleep(1)

if __name__ == '__main__':
    lock = threading.Lock()
    queue = Queue.Queue()
    t1 = threading.Thread(target=write,args=(lock,queue))
    t2 = threading.Thread(target=write,args=(lock,queue))
    t3 = threading.Thread(target=read,args=(queue,))
    t1.start()
    t2.start()
    t3.start()
    time.sleep(10)
    exitFlag = True
    t1.join()
    t2.join()
    t3.join()

# Semaphore()

g = 0
def add(lock,a,b):
    with lock:
        print 'now enter add'
        global g
        g += a+b
        time.sleep(3)

if __name__=='__main__':
    tList = []
    s = threading.Semaphore(3)
    for i in xrange(60):
        tList.append(threading.Thread(target=add,args=(s,i,i+1)))
    for t in tList:
        t.start()
    for i in tList:
        t.join()
    print g



import threading,time,Queue,random



def write(e,queue):
    while not e.isSet():
        thread = threading.currentThread()
        data = random.randint(1,100)
        print 'this is thread:',thread.getName(),'put:',data
        queue.put(data)
        time.sleep(1)

def read(queue,e):
    while not e.isSet():
        print 'get:',queue.get()
        time.sleep(1)

if __name__ == '__main__':
    e = threading.Event()
    queue = Queue.Queue()
    t1 = threading.Thread(target=write,args=(e,queue))
    t2 = threading.Thread(target=write,args=(e,queue))
    t3 = threading.Thread(target=read,args=(queue,e))
    t1.start()
    t2.start()
    t3.start()
    time.sleep(10)
    e.set()
    t1.join()
    t2.join()
    t3.join()

# 习题：
# con.notify(3) 之后，两秒内，会打印多少个 'now enter add'
# con.notifyAll()之后，会打印多少个 'now enter add'




# 死锁
# T1:拥有lock1锁，申请lock2锁
#
# T2：拥有lock2锁，申请lock1锁
#
# 如何尽量的保证不出现死锁
# 定义锁的使用顺序



# 习题：两个线程，两把锁，构造死锁

def add1(lock1,lock2):
    lock1.acquire()
    time.sleep(2)
    print 'A'
    time.sleep(3)
    lock2.acquire()
    lock2.release()
    lock1.release()


def add2(lock1,lock2):
    lock2.acquire()
    print 'B'
    time.sleep(1)
    lock1.acquire()
    lock2.release()
    lock1.release()

if __name__=='__main__':
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    t1 = threading.Thread(target=add1,args=(lock1,lock2))
    t2 = threading.Thread(target=add2,args=(lock1,lock2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print 'end'

# 解决死锁
def add1(lock1,lock2):
    lock1.acquire()
    time.sleep(2)
    print 'A'
    time.sleep(3)
    lock2.acquire()
    lock1.release()
    lock2.release()


def add2(lock1,lock2):
    lock1.acquire()
    print 'B'
    time.sleep(1)
    lock2.acquire()
    lock1.release()
    lock2.release()

if __name__=='__main__':
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    t1 = threading.Thread(target=add1,args=(lock1,lock2))
    t2 = threading.Thread(target=add2,args=(lock1,lock2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print 'end'

# 淘宝面试性能测试职位的面试题,不要求做出来,只是说一下解题思路.
# 题目: 【在一个文件里有一堆数字大概100多G,数字直接用逗号隔开的,
# 试找出其中最大的100个数字.】
#
# 要求:很简单,只是说一下你解题时能用到那些知识,包括那门课的那块知识,
# 详细说明解题思路.

# 分而治之
# 答:1、切割文件10000份--100M---100000000/5 = 2000000
# 2、内存中，列表存储，快排，取前100个
# 3、10000个列表--100个--2,000,000字节，二叉树存储

# PurPle 12:12:16
# 1.根据安装文档搭建Android studio开发环境，主要包括以下内容：
#   1.1 安装java jdk，并配置好java环境变量
#   1.2 安装Android studio
#   1.3 安装Android sdk，并下载好level 19的android sdk和对应版本的镜像文件，即android4.4版本的SDK和镜像文件
#   //步骤1.4使用android自带的avd
#   1.4 安装Android virtual device，使用android4.4版本的镜像文件创建和启动虚拟设备成功
#   //步骤1.5-1.6，使用genymotion
#   1.5 安装genymotion，并导入镜像文件，在genymotion上启动虚拟设备成功
#   1.6 在Android studio上安装genymotion插件，通过插件启动genymotion的虚拟设备成功
#
#   注意事项：启动的设备需要配置成联网，方便安装第三方应用
#
# 2.创建一个android4.4版本的工程并成功启动，要求如下：
#   2.1 在avd和上安装并启动APP成功
#   2.2 在genymotion的虚拟设备上安装并启动APP成功
#
# 3.在虚拟设备中安装第三方应用
#   3.1 在avd中安装华为应用中心
#   3.2 在genymotion的虚拟设备上安装华为应用中心
#
# 4.其它（选做）
#   完成上面1-3步后，可以研究下怎么把APP部署到真机上















