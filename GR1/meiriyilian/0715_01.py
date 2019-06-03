# encoding=utf-8
import threading,time

product = 0

def consumer(con):
    global product
    while exitFlag != True:
        with con:
            print 'enter consummer thread'
            if product==0:
                con.wait()
            else:
                print 'now consummer 1 product'
                product -= 1
                print 'after consummer ,we have ',product,'product now'
            time.sleep(2)

def producer(con):
    global product
    while exitFlag != True:
        with con:
            print 'enter product thread'
            product += 1
            con.notify()
            print 'after product ,we have ',product,'products now'
if __name__=='__main__':
    exitFlag = False
    con = threading.Condition()
    c1 = threading.Thread(target=consumer,args=(con,))
    c2 = threading.Thread(target=producer,args=(con,))
    c1.start()
    c2.start()
    time.sleep(20)
    exitFlag = True
    c1.join()
    c2.join()






# Condition
# 使用场景：处理复杂逻辑
# Queue
# Lock
# Semaphore
# 线程 做了某一件事，中途需要停止
# 线程B做另外一件事，线程B通知线程A
# 线程A继续
#
# 1、condition是条件，内部也是锁
# 2、额外提供了wait()方法和notify（）方法，用于处理复杂的逻辑
# 3、wait()释放锁，并且等待通知
# 4、Notify()
# 唤醒对方，可以继续下去，但是并不意味着，wait（）线程可以立刻执行
# 需要抢锁

















