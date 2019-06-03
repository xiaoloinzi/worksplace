# encoding=utf-8
import threading
import time
import os







# 当前目录下有三个班的分数文件，名称分别为score1.txt、score2.txt、score3.txt
# 的文本文件，存放着三个班学生的计
# 算机课成绩，共有学号、总评成绩两列。用多线程编程的方式，
# 请查找班级最高分和最低分的学生，以及年级最高分和最低分的学生，
# 并在屏幕上显示其学号和成绩。

dict1 = {}
def printfile(file,classs,lock,dicts):
    global dict1
    classfile = os.path.splitext(file)
    with lock:
        with open(file,'r') as fp:
            refile = fp.readlines()
            for i in xrange(len(refile)):
                if i != 0:
                    relist = refile[i].split()
                    dict1[classs+":No."+str(relist[0])] = relist[1]
                    dicts[str(relist[0])] = relist[1]
            classsum =  sorted(dicts.items(),key=lambda e:e[1],reverse=True)
            print classsum[0][0]+u"是班级"+classs+u"最高分："+classsum[0][1]
            print classsum[-1][0]+u"是班级"+classs+u"最低分："+classsum[-1][1]
            print '-'*40
if __name__=='__main__':
    dict3 = {'score1.txt':'class1','score2.txt':'class2','score3.txt':'class3'}
    lock = threading.Lock()
    dict2 = {}
    th = [threading.Thread(target=printfile,args=(i,j,lock,dict2)) for i,j in dict3.items()]
    for i in th:
        i.start()
    for i in th:
        i.join()
    strsum =  sorted(dict1.items(),key=lambda e:e[1],reverse=True)
    print strsum[0][0]+u"是年级最高分："+strsum[0][1]
    print strsum[-1][0]+u"是年级最低分："+strsum[-1][1]
# 练习字典
with open('score1.txt','r') as fp:
        refile = fp.readlines()
        for i in xrange(len(refile)):
            if i != 0:
                relist = refile[i].split()
                dict1['score1:'+str(relist[0])] = relist[1]

sore1 = sorted(dict1.items(),key=lambda e:e[1],reverse=True)
print sore1[0][1]






