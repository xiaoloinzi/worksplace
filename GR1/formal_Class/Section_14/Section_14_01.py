# encoding=utf-8

# 多线程编程
# 1、Python被人诟病的地方
# 多线程编程 10
# GIL
# 1、脚本型语言，本身性能相较C，Java等，要慢
# 2、多线程领域，GIL的存在
#
#
# 《多进程编程》
# 1、CPU密集型程序--瓶颈-CPU--推荐多进程编程
# 2、IO密集型---推荐多线程编程（频繁的文件读取或存取数据库数据）
#
# Python2-》Python3
#
# 1、80%的性能损耗，是耗费在20% 的代码，20%的代码通过C去写
# 2、性能是架构出来的
# 进程所占用的内存空间：（新的进程和老的进程的区域是不一样的，使用线程可以复用老的进程的空间区域）
# 1、文本区域--存放所写的代码
#
# 2、数据区域--全局变量，在数据方面所占用的空间
#
# 3、堆栈空间--和函数和方法有关系，运行函数和方法都是临时产生空间的
# 调用时所产生的运行空间都在堆栈空间，包括局部变量

# 阻塞式--等待函数结束才往下走
# 非阻塞式--调用函数就不管了，直接走主进程


import multiprocessing
import time
import urllib2
from multiprocessing import Process,Pool,Lock,Value
# multiprocessing.Process(group=用户组,target=指向函数，运行进程,name=任务管理器进程的名字,args=元组参数,kwargs=字典参数)
multiprocessing.Process()
def func1(msg):
    time.sleep(2)
    print msg

if __name__=='__main__':
    p1 = multiprocessing.Process(target=func1,args=('hello world',))
    # start()--启动进程
    # join()等待前一个进程结束才开始下一个进程
    # existcode()--得到进程返回值（0为NOne，由函数决定）
    # is_alive()判断进程是否运行(是否在活动状态)
    # terminate（）强制中断退出进程
    print p1.is_alive()
    p1.start()
    # 没有join（）则不需要等子进程结束，谁抢到CPU资源，谁先运行
    print p1.is_alive()
    p1.join()
    print p1.is_alive()
    print p1.exitcode
    print 'done'

def func1(url):
    response = urllib2.urlopen(url)
    html = response.read()
    print html[:20],'-------------func1'
    time.sleep(2)

def func2(url):
    response = urllib2.urlopen(url)
    html = response.read()
    print html[:20],'---------------func2'
    time.sleep(2)
#
if __name__=='__main__':
    p1 = multiprocessing.Process(target=func1,args=('http://www.sogou.com',))
    p2 = multiprocessing.Process(target=func2,args=('http://www.baidu.com',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print 'done'

# 习题：写一个多进程程序，程序针对全局变量count，默认值是0，
# 完成加10的操作采用10个进程并发操作，
# 最后统一join()打印出全局变量count的值
count = 0
def func1():
    global count
    count += 10
    # return count
if __name__=='__main__':
    p = []
    for i in xrange(10):
        p.append(multiprocessing.Process(target=func1))

    for i in p:
        i.start()
    for i in p:
        i.join()
    print count

# 老师的方法
globalVal = 0
def func1():
    global globalVal
    globalVal += 10
    print '------',globalVal,'--------'
    return globalVal
if __name__=='__main__':
    procesList = []
    for i in xrange(10):
        p = multiprocessing.Process(target=func1)
        procesList.append(p)

    for i in procesList:
        i.start()
    for i in procesList:
        i.join()
    print 'done'
    print globalVal

# 习题：解释一下count的值为什么是10，后面打印为什么是0
# 进程所占用的内存空间：（新的进程和老的进程的区域是不一样的，使用线程可以复用老的进程的空间区域）
# 1、文本区域--存放所写的代码
#
# 2、数据区域--全局变量，在数据方面所占用的空间
#
# 3、堆栈空间--和函数和方法有关系，运行函数和方法都是临时产生空间的
# 每个进程有自己的全局变量，而count=0是相对于当前文件的全局变量，
# 是当前的主进程的全局变量，进程和进程之间是相互独立的

def f(n,a):
    n.value= 3.14
    for i in range(len(a)):
        a[i] = - a[i]
#
if __name__=='__main__':
    # d表示浮点数--double
    num = multiprocessing.Value('d',1.0)#表示当前的变量
    arr = multiprocessing.Array('i',range(10))#当前的数组
    p = multiprocessing.Process(target=f,args=(num,arr))
    p.start()
    p.join()
    print num#返回的是一个实例
    print num.value
    print arr[:]
# 习题：把count变量，封装成Count类，
# 实现增1方法increase及getValue方法。

class Count(object):
    def __init__(self,num):
        self.num = num

    def increase(self):
        self.num += 1

    def getValue(self):
        return self.num

if __name__=='__main__':
    a = Count(6)
    # a.increase()
    print a.getValue()

# 习题：把类Count中的属性count，使用Value表示，并且使用多进程进行
# count的自增操作，50个进程进行操作

if __name__=='__main__':
    num = multiprocessing.Value('i',7)
    a = Count(num.value)
    p = []
    for i in xrange(50):
        b = multiprocessing.Process(target=a.increase())
        p.append(b)
    for i in p:
        i.start()

    for i in p:
        i.join()

    print num.value

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
#
#
if __name__=='__main__':
    c1 = Count(0)
    procs = [multiprocessing.Process(target=func,args=(c1,)) for i in range(10)]
    for i in procs:
        i.start()
    for i in procs:
        i.join()
    print c1.getValue()

# 习题：上述的答案有什么问题？，为何sleep的时间长，出错的概率高，
# 并发进程数大，出错概率高
# 共享内存，进程同时进行写操作，不加锁，则会出现并发
# 只能有一个写进行中，否则就会出现并发情况，两个进程同时操作一个数据




# 进程间的协同操作：
# Lock（），accquire(),release()

def func(num,lock):
    lock.acquire()
    # time.sleep(0.1)
    print 'hello num:%s'%num.value
    num.value += 1
    lock.release()

if __name__=='__main__':
    lock = Lock()
    val = Value('i',0)
    # for num in range(50):
    #     Process(target=func,args=(val,lock)).start()
    Procs = [Process(target=func,args=(val,lock)) for i in xrange(50)]
    for p in Procs:
        p.start()
    for p in Procs:
        p.join()
    print val.value


class Count(object):
    def __init__(self,num):
        self.num = multiprocessing.Value('i',num)

    def increase(self):
        self.num.value += 1

    def getValue(self):
        return self.num.value

def func(counter,lock):
    lock.acquire()#获得锁
    time.sleep(0.1)
    counter.increase()
    print counter.getValue()
    lock.release()#释放锁
#
#
if __name__=='__main__':
    lock = Lock()#创建一个共享锁
    c1 = Count(0)
    procs = [multiprocessing.Process(target=func,args=(c1,lock)) for i in range(50)]
    for i in procs:
        i.start()
    for i in procs:
        i.join()
    print c1.getValue()


def l(lock,num):
    lock.acquire()
    print 'Hello Num:%s'%num
    lock.release()

if __name__=='__main__':
    lock = Lock()
    for num in range(20):
        Process(target=l,args=(lock,num)).start()
        time.sleep(0.1)#加上等待之间给加锁



