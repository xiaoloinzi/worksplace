# encoding=utf-8
import threading,time,random
from Queue import Queue
# 每日一练已修改，做如下的题目：
# 当前目录下有三个班的分数文件，名称分别为score1.txt、score2.txt、score3.txt
# 的文本文件，存放着三个班学生的计
# 算机课成绩，共有学号、总评成绩两列。用多线程编程的方式，请查找班级最高分和
# 最低分的学生，以及年级最高分和最低分的学生，并在屏幕上显示其学号和成绩。




#  每日一练：
# 使用生产者方式实现多线程写队列和读队列
#       要求：边读边写
# 每日一练：
# 3、实现多线程入队列，然后按规则出队列
#       要求：
#       1）实现一个线程不断生成一个随机数到一个队列中(考虑使用Queue    这个模块)
#       2）实现一个线程从上面的队列里面不断的取出奇数
#       3）实现另外一个线程从上面的队列里面不断取出偶数
# 算法：
# 队列sq,用于生产者线程
# 如果sq里面的是奇数，则放入oq，线程C读取该队列的元素
# 如果sq里面的是奇数，则放入eq，线程D读取该队列的元素

def producer(q):
    while exitFlag != True:
        i = random.randint(1,1000)
        q.put(i)
def putQueue(sq,oq,eq):
    while exitFlag!=True:
        i = sq.get()
        if i%2 ==0:
            eq.put(i)
        else:
            oq.put(i)

def consuer(q,flag):
    while exitFlag != True:
        i = q.get()
        print '%s thread get %d now'%(flag,i)
        time.sleep(0.5)

if __name__=='__main__':
    exitFlag = False
    sq = Queue()
    oq = Queue()
    eq = Queue()
    proThread = threading.Thread(target=producer,args=(sq,))
    sortThread = threading.Thread(target=putQueue,args=(sq,oq,eq))
    oddThread = threading.Thread(target=consuer,args=(oq,"odd"))
    evenThread = threading.Thread(target=consuer,args=(eq,'even'))
    proThread.start()
    time.sleep(0.5)
    sortThread.start()
    oddThread.start()
    evenThread.start()
    time.sleep(5)
    exitFlag = True
    proThread.join()
    sortThread.join()
    oddThread.join()
    evenThread.join()


# 每日一练：1、使用多线程交替打印数字
#      要求：
#       1）线程1只打印奇数，线程2只打印偶数
#       2）要求打印1、2、3、4、5、6、7……

def func(startVar,cond):
    start = startVar
    while exitFlag != True:
        with cond:
            print start,
            start += 2
            cond.wait()
def func2(startVar,cond):
    start = startVar
    while exitFlag != True:
        time.sleep(0.1)
        with cond:
            print start
            start += 2
            cond.notify()

if __name__=='__main__':
    exitFlag = False
    cond = threading.Condition()
    t1 = threading.Thread(target=func,args=(1,cond))
    t2 = threading.Thread(target=func2,args=(2,cond))
    t1.start()
    time.sleep(0.1)
    t2.start()
    time.sleep(10)
    exitFlag = True
    t1.join()
    t2.join()























