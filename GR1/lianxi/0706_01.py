# encoding=utf-8
import threading
import multiprocessing





count = 0
def printrun():
    global count
    pro = multiprocessing.current_process()
    count += 1
    print pro._name,':',count
if __name__=='__main__':
    list1 = []
    for i in xrange(10):
        list1.append(multiprocessing.Process(target=printrun))
    for i in list1:
        i.start()
    for i in list1:
        i.join()
    print count

count = 0
def printrun():
    global count
    count += 10
    threads = threading.currentThread()
    print threads.getName(),':',count

if __name__=='__main__':
    list1 = []
    for i in xrange(10):
        res = threading.Thread(target=printrun)
        list1.append(res)
    for i in list1:
        i.start()
    for i in list1:
        i.join()
    print count



