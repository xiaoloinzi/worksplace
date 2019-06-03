# encoding=utf-8
import threading
import time


class MyThread(threading.Thread):
    def __init__(self,a,b):
        threading.Thread.__init__(self)
        self.a = a
        self.b = b
    def run(self):
        print "%d+%d=%d"%(self.a,self.b,self.a+self.b)
if __name__=='__main__':
    t1 = MyThread(2014,1024)
    t1.start()
    t1.join()
    print 'main end'

def threadA(threads):
    print 'enter threadB'
    threads.start()
    print 'exit threadB'
    threads.join()
    print 'exit threadA'

def threadB():
    print 'this is thread B'
if __name__=='__main__':
    tB = threading.Thread(target=threadB)
    tA = threading.Thread(target=threadA,args=(tB,))
    tA.start()
    tA.join()
    print 'main end'

def A():
    print 'enter A '
    time.sleep(7)
    print 'exit A'
def B():
    print 'enter B'
    time.sleep(10)
    print 'exit B'
if __name__=='__main__':
    tA = threading.Thread(target=A)
    tB = threading.Thread(target=B)
    tA.setDaemon(True)
    tA.start()
    tB.start()
    tA.join()
    tB.join()
    print 'main end'

def A():
    print 'enter A'
    time.sleep(10)
    print 'exit A'

def B():
    print 'enter B'
    time.sleep(7)
    print 'exit B'
if __name__=='__main__':
    tA = threading.Thread(target=A)
    tB = threading.Thread(target=B)
    tA.setDaemon(True)
    tA.start()
    tB.start()
    print 'main exit'


















