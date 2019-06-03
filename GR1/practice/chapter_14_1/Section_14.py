# encoding=utf-8
import os
import multiprocessing
import urllib2
import time

print os.getpid()
pid = os.fork()
print pid
print os.getppid()


print help(multiprocessing.Process)

def do(n):
    name = multiprocessing.current_process().name
    print name,'starting'
    print 'worker ',n
    return
if __name__=='__main__':
    numList = []
    for i in xrange(5):
        p = multiprocessing.Process(target=do,args=(i,))
        numList.append(p)
        p.start()
        p.join()
        print 'Process end'
        print numList


def func1(url):
    response = urllib2.urlopen(url)
    html = response.read()
    print html[0:20]
    time.sleep(10)

def func2(url):
    response = urllib2.urlopen(url)
    html = response.read()
    print html[0:20]
    time.sleep(10)

if __name__=='__main__':
    p1 = multiprocessing.Process(target=func1,
                                 args=('http://www.baidu.com',),
                                 name='gloryroad1')
    p2 = multiprocessing.Process(target=func2,
                                 args=('http://www.baidu.com',),
                                 name='gloryroad1')

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    time.sleep(5)
    print 'done!'

def m1(x):
    time.sleep(0.01)
    # print x
    return x*x

if __name__=='__main__':
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    i_list = range(1000)
    time1 = time.time()
    pool.map(m1,i_list)
    time2 = time.time()
    print 'time elpse:',time2-time1

    time1 = time.time()
    pool.map(m1,i_list)
    time2 = time.time()
    print 'time elpse:',time2-time1

def m1(x):
    return x*x

if __name__=='__main__':
    # pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # i_list = range(8)
    # print pool.map(m1,i_list)
    pool = multiprocessing.Pool(processes=4)
    result = pool.apply_async(m1,[10])
    print result
    print '-'*40
    print result.get(timeout = 9)
    print pool.map(m1,range(10))












