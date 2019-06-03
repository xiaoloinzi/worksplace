# encoding=utf-8
from threading import Thread,Lock
import time
import threading
import thread
from multiprocessing.dummy import Pool
from Queue import Queue
import random
import sys,logging
import multiprocessing

def run(a = None,b=None):
    print a,b
    time.sleep(1)

t = Thread(target=run,args=('this is ','thread'))
print t.getName()
print t.is_alive()

t.start()
t.join()
print t.is_alive()

class MyThread(Thread):
    def __init__(self,a):
        super(MyThread,self).__init__()
        self.a = a

    def run(self):
        time.sleep(self.a)
        print 'sleep:',self.a


t1 = MyThread(2)
t2 = MyThread(4)
t1.start()
t2.start()
print t1.is_alive()
print t2.is_alive()
t1.join()
t2.join()
print t1.is_alive()

class timer(threading.Thread):
    def __init__(self,num,interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.terval = interval
        self.thread_stop = False

    def run(self):
        print self.thread_num
        print self.terval
        print self.thread_stop


t1 = timer(1,2)
t1.start()
print 'vv'
print t1.is_alive()
t1.join()
print t1.is_alive()


class timer(threading.Thread):
    def __init__(self,num,interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False


    def run(self):
        while not self.thread_stop:
            print 'Thread Object(%d),Time:%s\n'%(self.thread_num,time.ctime())
            time.sleep(self.interval)


    def stop(self):
        self.thread_stop = True



def test():
    threat1 = timer(1,1)
    threat2 = timer(2,2)
    threat1.start()
    threat2.start()
    time.sleep(10)
    threat1.stop()
    threat2.stop()

if __name__=='__main__':
    test()

exitFlag = 1

class myTread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print 'Starting '+self.name
        print_time(self.name,self.counter,5)
        print 'Exiting'+self.name

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print '%s:%s'%(threadName,time.ctime(time.time()))
        counter -= 1

thread1 = myTread(1,'Thread-1',1)
thread2 = myTread(2,'Thread-2',2)

thread1.start()
thread2.start()
print 'Exiting Main Thread'


def context(tjoin):
    print 'in threadContext.'
    tjoin.start()
    tjoin.join()
    print 'out threadCountext'

def join():
    print 'in threadjoin.'
    time.sleep(1)
    print 'out threadjoin.'

tjoin = threading.Thread(target=join)
tCOntext = threading.Thread(target=context,args=(tjoin,))
tCOntext.start()


class MyThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(5)
        print 'This is '+self.getName()

if __name__=='__main__':
    t1 = MyThread(999)
    t1.setDaemon(True)
    t1.start()
    print 'I am the father thread.'


def run(fn):
    time.sleep(2)
    print fn

if __name__=='__main__':
    testFL = [1,2,3,4,5]
    pool = Pool(1)
    pool.map(run,testFL)
    pool.close()
    pool.join()


date = 0
lock = threading.Lock()

def func():
    global date
    print '%s acquire lock...\n'%threading.currentThread().getName()
    if lock.acquire():
        print '%s get lock..\n'%threading.currentThread().getName()
        date += 1
        print date
        time.sleep(1)
        print '%s release lock..\n'%threading.currentThread().getName()
    lock.release()

startTime = time.time()
t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

endtime = time.time()
print 'used time is ',endtime-startTime

class Producer(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name = t_name)
        self.data = queue


    def run(self):
        for i in range(5):
            print '%s :%s is producing %d to the queue!\n'%(time.ctime(),self.getName(),i)
            self.data.put(i)
            time.sleep(random.randrange(10/5))
        print '%s:%s finished!'%(time.ctime(),self.getName())

class Cousumer(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print '%s :%s is consuming.%d in the queue is consumed!\n'%(time.ctime(),self.getName(),val)
            time.sleep((random.randrange(10)))
        print '%s:%s finished!'%(time.ctime(),self.getName())

def main():
    queue = Queue()
    producer = Producer('Pro',queue)
    cousumer = Cousumer('Con',queue)
    producer.start()
    cousumer.start()
    producer.join()
    cousumer.join()
    print 'All threads terminate'

if __name__=='__main__':
    main()

def run(lock,num):
    lock.acquire()
    threadName = threading.current_thread().getName()
    print '%s,hello Num:%s'%(threadName,num)
    lock.release()

if __name__=='__main__':
    lock = Lock()
    for num in range(20):
        Thread(name='Thread-%s'%str(num),target=run,args=(lock,num)).start()

def worker(s,i):
    s.acquire()
    print threading.current_thread().name+'acquire'
    time.sleep(i)
    print threading.current_thread().name+'release'
    s.release()

if __name__=='__main__':
    s = threading.Semaphore(3)
    for i in range(10):
        t = Thread(target=worker,args=(s,i*2))
        t.start()

def wait_for_event(e):
    print 'wait_for_event:starting'
    e.wait()
    print 'wait_for_event:e.is_set()->',e.is_set()

def wait_for_event_timeout(e,t):
    print 'wait_for_event_timeout:starting'
    e.wait(t)
    print 'wait_for_event_timeout:e.is_set()->',e.is_set()
    e.set()

if __name__=='__main__':
    e = threading.Event()
    w1 = Thread(name = 'block',target=wait_for_event,args=(e,))
    w1.start()

    w2 = Thread(name='nonblock',target=wait_for_event_timeout,args=(e,2))
    w2.start()

    print 'main:waiting before calling Event.set()'
    time.sleep(3)
    print 'main:event is set'


def consumer(cond):
    with cond:
        print 'consumer before wait'
        cond.wait()
        print 'consumer after wait'

def producer(cond):
    with cond:
        print 'producer before notifyAll'
        cond.notify_all()
        print 'producer after notifyAll'

if __name__=='__main__':
    condtion = threading.Condition()
    t1 = threading.Thread(name = 'thread-1',target= consumer,args=(condtion,))
    t2 = threading.Thread(name = 'thread-2',target=consumer,args=(condtion,))
    t3 = threading.Thread(name = 'thread-3',target=producer,args=(condtion,))
    t1.start()
    time.sleep(2)
    t2.start()
    time.sleep(2)
    t3.start()

def creat(queue):
    for i in [100,50,20,10,5,1,0,5]:
        if not queue.full():
            queue.put(i)
            print 'Put %sRMB to queue.'%i
            time.sleep(1)

def get(queue):
    while 1:
        if not queue.empty():
            print 'Get %sRMB from queue.'%queue.get()
            time.sleep(2)
        else:
            break
q = Queue(5)
creat_t = Thread(target=creat,args=(q,))
get_t = Thread(target = get,args=(q,))
creat_t.start()
get_t.start()
creat_t.join()
get_t.join()

q = Queue(maxsize=10)
q.put(10)
q.put('key')
print u'返回队列的大小：',q.qsize()
print u'如果队列为空，返回True，否则返回False：',q.empty()
print u'如果队列满了，返回True，否则返回False：',q.full()

print q.get()
print q.get()

def daemon():
    p = multiprocessing.current_process()
    print 'Starting:',p.name,p.pid
    sys.stdout.flush()
    print 'Exiting:',p.name,p.pid
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process()
    print 'StartingL',p.name,p.pid
    sys.stdout.flush()
    print 'Exiting:',p.name,p.pid
    sys.stdout.flush()

daemon()
non_daemon()


exitFlag = 0
class myThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print 'Starting'+self.name
        process_data(self.name,self.q)
        print 'Exiting'+self.name

def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print '%s processing %s'%(threadName,data)
        else:
            queueLock.release()
        time.sleep(1)

threadList = ['Thread-1','Thread-2','Thread-3']
nameList = ['One','Two','Four','Five']
queueLock = threading.Lock()
workQueue = Queue(10)
threads = []
threadID = 1

for tName in threadList:
    thread = myThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass
exitFlag = 1
for i in threads:
    i.join()
print 'Exitinf Main Thread'


# 1、使用多线程交替打印数字
# 要求：
# 1）线程1只打印奇数，线程2只打印偶数
# 2）要求打印1、2、3、4、5、6、7……


# 2、使用生产者方式实现多线程写队列和读队列
# 要求：边读边写



# 3、实现多线程入队列，然后按规则出队列
# 要求：
# 1）实现一个线程不断生成一个随机数到一个队列中(考虑使用Queue
# 这个模块)
# 2）实现一个线程从上面的队列里面不断的取出奇数
# 3）实现另外一个线程从上面的队列里面不断取出偶数






















































































































































