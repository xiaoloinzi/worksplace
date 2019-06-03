# encoding=utf-8
import os
from multiprocessing import Process,Lock,Queue
import time


# 1、统计目录下文件中字符数和行数
# 要求：
# 并行统计指定目录下所有文件（以.txt/.10w结尾）中的字符个数和行数，
# 并将结果写入res.txt文件中，每个文件一行，格式为：
# filename:lineNumber,charNumber。


def printcount(str1):
    str2 = str1.split()
    return len(str2)

def printdir(path,lock):
    with lock:
        str3 = 0
        for dirpath,dirnames,filenames in os.walk(path):
            for filename in filenames:
                if filename.endswith('.txt'):
                    filePath = os.path.join(dirpath,filename)
                    print filePath
                    with open(filePath,'r') as fp:
                        linenum = len(fp.readlines())
                        str3 += printcount(filePath)

                try:
                    with open('D:\\tmp\\res.txt','a') as fp:
                        fp.write(filename+':'+str(linenum)+','+str(str3)+'\n')
                except Exception:
                    with open('D:\\tmp\\res.txt','w') as fp:
                        fp.write(filename+':'+str(linenum)+','+str(str3)+'\n')

if __name__ == '__main__':
    lock = Lock()
    pathdir = 'D:\\tmp\\log'
    proces = [Process(target=printdir,args=(pathdir,lock)) for i in range(3)]
    for i in proces:
        i.start()
    for i in proces:
        i.join()

# 2、以加锁的方式完成一个先写队列，然后才读队列多进程程序
#
def write(q,lock):
    with lock:
        for value in ['A','B','C']:
            print 'put %s to queue'%value
            q.put(value)
            time.sleep(1)

def read(q,lock):
    def isEmpty(q):
        i = 0
        while i < 5:
            if not q.empty():
                return False
            time.sleep(2)
            i += 1
        return True
    while not isEmpty(q):
        with lock:
            print 'get %s from queue.'%q.get()
            time.sleep(1)

if __name__ == '__main__':
    q = Queue()
    lock = Lock()
    pw = Process(target=write,args=(q,lock))
    pr = Process(target=read,args=(q,lock))
    pw.start()
    pr.start()
    pw.join()
    pr.join()

# 3、借助队列，实现一个边读边写的多进程程序

def write(q,lock):
    with lock:
       for value in ['A','B','C']:
            print 'put %s to queue'%value
            q.put(value)
            time.sleep(1)

def read(q,lock):
    def isEmpty(q):
        i = 0
        while i < 5:
            if not q.empty():
                return False
            time.sleep(2)
            i += 1
        return True
    while not isEmpty(q):
        with lock:
            print 'get %s from queue.'%q.get()
            time.sleep(1)

if __name__ == '__main__':
    q = Queue()
    lock = Lock()
    pw = Process(target=write,args=(q,lock))
    pr = Process(target=read,args=(q,lock))
    pw.start()
    pr.start()
    pw.join()
    pr.join()


# 4、实现命令交互功能
# 要求：
# 实现命令交互功能，不断从键盘接受命令执行，给出执行结果，直到用户
# 输入exit或者bye退出命令交互。




def printinput():
    i = 0
    while i == 0:
        command = raw_input('please input command:')
        if command == 'exit' or command == 'bye':
            print 'end'
            i = -1
        else:
            os.system(command)


if __name__=='__mian__':
    printinput()
#老师的方法：
 # encoding=utf-8
import subprocess

def runCmd(cmd):
    p1 = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    sout,serr = p1.communicate()
    print sout
    print serr
    return p1.returncode,sout,serr,p1.pid

if __name__ == '__main__':
    while True:
        inputStr = raw_input('please input the cmd:')
        if inputStr.lower() in ['exit','bye']:
            print 'now exit'
            exit(1)
        else:
            ret = runCmd(inputStr)
            print 'the return code of cmd:',ret[0]
            print 'the stdout of cmd:',ret[1]
            print 'the stderr of cmd:',ret[2]
            print 'the pid of cmd:',ret[3]













































