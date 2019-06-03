# encoding=utf-8
import multiprocessing
import time

def waitForEvent(e):
    print 'wait for event starting ,no timeout'
    e.wait()
    print 'the event has happaned. is :',e.is_set()
def waitForEventtimeout(e,t):
    print 'wait for event staring.Timeout is ',t
    e.wait(t)
    print 'the event is:',e.is_set()
if __name__=='__main__':
    e = multiprocessing.Event()
    print 'thre event is_set is :',e.is_set()
    # p1 = multiprocessing.Process(target=waitForEvent,args=(e,))
    # p1.start()
    # time.sleep(3)
    # e.set()
    p2 = multiprocessing.Process(target=waitForEventtimeout,args=(e,2))
    p2.start()
    time.sleep(1)
    e.set()

def write(q):
    for i  in [1,'123','123asd0','str']:
        print 'put %s to queue.'%i
        q.put(i)
def read(q):
    def isEmpty(q):
        i = 0
        while i<5:
            if not q.empty():
                return False
            time.sleep(2)
            i +=1
        return True
    while not isEmpty(q):
        res = q.get()
        if isinstance(res,str) and res.isdigit():
            print 'get %s to queue.'%res
        else:
            print 'write %s to file'%res
            with open('score2.txt','a') as fp:
                fp.write(str(res)+'\n')
if __name__=='__main__':
    queue = multiprocessing.Queue()
    pw = multiprocessing.Process(target=write,args=(queue,))
    pr = multiprocessing.Process(target=read,args=(queue,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print 'end'

def writes(q):
    for i in [1,'str','123strt']:
        print 'put %s to queue'%i
        q.put(i)
def read(q):
    def isEmpty(queue):
        i = 0
        while i< 5:
            if not queue.empty():
                return False
            time.sleep(2)
            i += 1
    while not isEmpty(q):
        res = q.get()
        if isinstance(res,str):
            print 'get %s to queue.'%res
        else:
            with open('score1.txt','a') as fp:
                fp.write(str(res)+'\n')
if __name__=='__main__':
    queue = multiprocessing.Queue()
    pw = multiprocessing.Process(target=writes,args=(queue,))
    pr = multiprocessing.Process(target=read,args=(queue,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print 'end'

def write(queue):
    for i in ['A','B','C']:
        print 'put %s to queue.'%i
        queue.put(i)
        time.sleep(1)
def read(queue):
    while not queue.empty():
        print 'get %s to queue.'%queue.get()
        time.sleep(5)
def read(queue):
    def isempty(q):
        times = 0
        while times < 5:
            if not q.empty():
                return False
            time.sleep(2)
            times += 1
        return True
    while not isempty(queue):
        print 'get %s to queue.'%queue.get()
        time.sleep(2)

if __name__=='__main__':
    q = multiprocessing.Queue()
    print q.empty()
    pw = multiprocessing.Process(target=write,args=(q,))
    pr = multiprocessing.Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()



class Count(object):
    def __init__(self,num):
        self.num = multiprocessing.Value('i',num)
    def increment(self):
        self.num.value += 1
    def getValue(self):
        return self.num.value
def func1(s,counter):
    s.acquire()
    print multiprocessing.current_process().name+': '+'acquire.'
    counter.increment()
    print counter.getValue()
    time.sleep(5)
    print multiprocessing.current_process().name+':'+'release.'
    s.release()
def func2(s,counter):
    with s:
        print multiprocessing.current_process().name+'----read----'
        time.sleep(3)
        print counter.getValue()

if __name__=='__main__':
    semaphores = multiprocessing.Semaphore(3)
    count = Count(0)
    for i in xrange(7):
        multiprocessing.Process(target=func2,args=(semaphores,count)).start()
        time.sleep(1)

def func1(s,i):
    with s:
        print multiprocessing.current_process().name+': '+'acquire.'
        time.sleep(i)
        time.sleep(5)
        print multiprocessing.current_process().name+': '+'release.'

if __name__=='__main__':
    s = multiprocessing.Semaphore(4)
    for i in xrange(7):
        pro = multiprocessing.Process(target=func1,args=(s,i))
        pro.start()
        time.sleep(1)

















