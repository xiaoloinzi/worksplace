# encoding=utf-8
import random
import sys,chardet,urllib,time,copy,os,datetime
import calendar
import user
import numpy
from multiprocessing import Pool,Process,Pipe
reload(sys)
sys.setdefaultencoding('utf-8')

# byteString = 'hello world'
# unicodeString = u'hello Unicode world'
# print type(byteString),type(unicodeString)

# with open("D:\\tmp\\t1.txt",'r') as fp:
#     str1 = fp.read()
#     tmp = str1.decode('gbk')
# print type(str1),str1
# print isinstance(tmp,unicode),isinstance(str1,unicode)

# with open("D:\\tmp\\t1.txt",'w') as fp:
#     info = tmp.encode('gbk')
#     fp.write(info)
#
# with open("D:\\tmp\\t1.txt",'r') as fp:
#     str1 = fp.read()
#     # tmp = str1.decode('gbk')
# print str1
# # print tmp
# print sys.getdefaultencoding()
#
# TestData = urllib.urlopen('http://www.baidu.com').read()
# print chardet.detect(TestData)
# print help('chardet')
# list1 = [1,2,3,4,5,6,6,7,8,8,9,0,12,23,231]
# print random.sample(list1,4)

# for i in xrange(10,51):
#     if str(i%10) in '12345':
#         print i,

# def printtime(str,num):
#     num +=1
#     print time.time(),':',str,':',num
#
# num = 10
# printtime(u'周末快乐！',num)
# print num
# print list1[0]
# list1[0] = 10
# print list1[0]

# def add_end(L=[]):
#     L.append('end')
#     return L
#
# def add_end1(L=None):
#     '''
#     DocString是一个重要的工具，由于它帮助你的程序文档更加简单易懂
#     :param L:
#     :return:
#     '''
#     if L == None:
#         L = []
#     L.append('end')
#     return L,2
# print add_end1([1,2,3])
# print add_end1(['x','y','z'])
# print add_end1()
# print add_end1()
# print add_end1()
# print add_end1.__doc__


# def addsum(a,b=2,*args):
#     print u'类型：',type(args)
#     print u'参数个数：',len(args)
#     sum = 0
#     for i in args:
#         sum += i
#     print sum+a+b
# addsum(1)
# def fun2(a,b=100,*args,**keys):
#     print "keys type=%s" % type(keys)
#     print "keys=%s" % str(keys)
#     print "name=%s" % str(keys['name'])
#     print "sex=%s" % str(keys['sex'])
#     sum=0
#     for i in args:
#         sum+=i
#     print sum+a+b
# fun2(1,2,3,4,name="vp",age=19,sex="m")
# testSTr = 'python is good 1'
# st = set(testSTr)
# print u'字符串转换集合：',st
# listset = set(list1)
# print u'列表转换集合：',listset
# listlist = list(listset)
# print u'集合转换回列表：',listlist
# s = str(st)
# print 'set:',s
# listset.discard(3)
# element = listset.pop()
# print listset,element
#
# s1 = ''.join(st)
# print s1

# list1 = [1,23,4,5,6,7]
# set1 = set(list1)
# str1 = map(str,set1)
# print str1
#
# def sub(x,y):
#     return x+y
# # print reduce(sub,list1,1)
# def char2num(s):
#     return {'0':0,'1':1,'2':2,'3':3,'4':4,
#             '5':5,'6':6,'7':7,'8':8,'9':9}[s]
# print reduce(sub,map(char2num,'13579'))

# def recur_fibo(n):
#     if n<=1:
#         return n
#     else:
#         s = recur_fibo(n-1)
#         d = recur_fibo(n-2)
#         return s+d
#
# print recur_fibo(5)
# list1 = [1,2,3,4,5]
# list2 = ['1','2','3']
# list1.insert(3,9)
# print list1
# list1.extend(list2)
# list1.extend(str(2))
# print list1
# list1 = [(-1,5,3),(-5,3,6,3),(1,1,2,4,5,6),(2,9),(-2,10)]
# def L(tup) :
#     return tup[0]
# def compare(a,b):
#     if abs(a)>abs(b):
#         return 1
#     elif abs(a)==abs(b):
#         return 0
#     else:
#         return -1
# list1.sort(cmp=compare,key = L,reverse = True)
# print list1
# list1 = [3,2,7,4,5]
# list2 = list1
# list3 = list1[:]
# list1.sort()
# print list1
# print list2
# print list3

# lista = 'abc'
# listb = 'xyz'
# s = (m+n for m in 'abc' for n in 'xyz' if 'abc'.index(m)=='xyz'.index(n))
# y = ['abc'[i]+'xyz'[i] for i in xrange(len('abc'))]
# n = [map(lambda x,y:x+y,'abc','xyz') ]
#
# l = [x for x in range(10)]
# t = [x for x in xrange(10)]

# print type(s)
# print s.next()
# print s.next()
# print '-'*40
# for i in s:
#     print i

# def odd():
#     print 'step 1'
#     yield 9
#     print 'step 2'
#     yield 8
#     print 'step 3'
#     yield 5
# print odd().next()
# print '-'*40
# num = 0
# for i in odd():
#     print i
#     num += 1
# print num
# ste = set([1,3,4,2])
# for i ,value in enumerate([1,3,4,2]):
#     print i,value
# print ste


# a = [1,2,3,4,['a','b']]
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
# print 'a id:',id(a[4])
# print 'b id:',id(b)
# print 'c id:',id(c[4])
# print 'd id:',id(d)
# print 'a :',a
# print 'b :',b
# print 'c :',c
# print 'd :',d
# a.append(7)
# a[4].append('r')
# print 'a id:',id(a)
# print 'b id:',id(b)
# print 'c id:',id(c)
# print 'd id:',id(d)
# print 'a :',a
# print 'b :',b
# print 'c :',c
# print 'd :',d
# tu1 = ({'a':12},1)
# tu1[0]= {'b':3}
# print tu1

# str1 = 'sdfsg'
# str3 = 'fsgsd'
#
# print str1==str3
# print str1 in str3
# print str1 is str3
# print cmp(str1,str3)

# ls = time.localtime()
# print ls
#
# print 'year:',ls[0]
# print 'month:',ls[1]
# print 'day:',ls[2]
# print 'year:',ls.tm_year
# print time.gmtime()
# # print (2017-1970)*366*24*60*60+144*24*60*60
# print int(time.time())

# def procedure():
#     time.sleep(10)
#
# time1 = time.clock()
# procedure()
# print time.clock()-time1
# print '-'*40
#
# time2 = time.time()
# procedure()
# print time.time()-time2

# struct_time = time.localtime()
# print struct_time
# print time.mktime(struct_time)
# print time.strftime("%Y-%m-%d %H:%M:%S %A %B %d",time.localtime())
# print str(time.localtime().tm_year)+u'年'+\
# str(time.localtime().tm_mon)+u'月'+str(time.localtime().tm_mday)\
# +u'日'+str(time.localtime().tm_hour)+u'点'\
# +str(time.localtime().tm_min)+u'分'+\
# str(time.localtime().tm_sec)+u'秒'
# print time.strftime('%Y/%m/%d %H:%M:%S')
# now = time.localtime()
# print time.strftime('%c',now)
# print time.strftime('%U',now)

# stime = '2017-05-24 13:01:30'
# formattime = time.strptime(stime,'%Y-%m-%d %H:%M:%S')
# print formattime
# for i in formattime:
#     print i,

# def fretime():
#     time.sleep(10)

# time1 = time.time()
# fretime()
# print u'time.time计算程序的消耗时间：',time.time()-time1
# time2 = time.clock()
# fretime()
# print u'time.clock计算程序的消耗时间：',time.clock()-time2
# strtime = '2017-05-24 23:00:55'
# fortime = time.strptime(strtime,'%Y-%m-%d %H:%M:%S')
# print fortime
# print time.mktime(fortime)
# print time.time()
# print time.strftime('%Y.%m.%d %H-%M-%S',fortime)
#
# sttime = time.time()
# print sttime
# print time.gmtime(sttime)
# print time.strftime('%Y.%m.%d %H-%M-%S',time.gmtime(sttime))


# lottime = time.strftime('%Y%m%d',time.localtime())
# s = 'D:\\'+str(lottime)
# # os.mkdir(s)
# d = str(lottime)+'.txt'
# with open(os.path.join(s , d),'w') as fp:
#     fp.write(u'你好！')

# print  time.clock()

# print datetime.date.max
# print datetime.date.min
# print datetime.date.resolution
# print datetime.date.day,':',datetime.date.month
# print datetime.date.today()
#
# now = time.time()
# print now
# print datetime.date.fromtimestamp(now)
#
# print datetime.datetime.now().year
# print datetime.datetime.now().month
# print datetime.datetime.now().day
#
# t = datetime.datetime.now()
# print t
# tomorrow = t.replace(day= 29 ,year=2018,month=12,)
# print tomorrow
# print t
# now = datetime.datetime.now()
# print now.timetuple()
# s = datetime.date.today()
# print datetime.date.weekday(s)
# now = datetime.datetime.now()
# print now
# str = now.strftime()

# today = datetime.date.today()
# print today
# print today + datetime.timedelta(days=10)
# print today - datetime.timedelta(days=10)
# future = today.replace(day=15)
# print future
# delta = future-today
# print delta
# print future + delta

# now = datetime.date.today()
# print 'now = datetime.date.today():',now
# tomorrow = now.replace(day = 13)
# print 'tomorrow = now.replace(day=13):',tomorrow
# print 'tomorrow > now:',tomorrow>now
# time.min = time(0,0,0,0)
# time.max = time(23,59,59,999999)
# maxtime = datetime.time.max
# print 'maxtime:',maxtime
# mintime = datetime.time.min
# print 'mintime:',mintime
# tm = datetime.datetime.now()
# print tm
#
# print 'hour:',tm.hour
# print 'minute:',tm.minute
# print 'month:',tm.month
# print 'second:',tm.second
# print 'microsecond:',tm.microsecond
# print datetime.datetime.today().minute
# print datetime.datetime.now().microsecond
# t = time.time()
# print t
# datetimes = datetime.datetime.fromtimestamp(t)
# print datetimes
# print type(datetimes)
# print str(datetimes)

# now = datetime.date.today()
# nowe = datetime.datetime.now()
# print now,nowe
# print datetime.date.weekday(now)
# print datetime.datetime.isocalendar(now)
# print datetime.datetime.isoweekday(now)
# print datetime.datetime.isoformat(nowe)
# print nowe.strftime('%Y-%m-%d %H:%M:%S %f')
# print nowe.strftime('%y-%m-%d %I:%M:%S %p')
# print nowe.strftime('%y-%m-%d %I:%M:%S %p')
# print nowe.strftime('%a')
# print now.strftime('%A')
# print datetime.timedelta(hours=2).seconds
# print datetime.timedelta(minutes=3600).days
# print dir(datetime.timedelta)
#
# d1 = datetime.datetime(2015,7,25)
# d2 = datetime.datetime(2015,8,26)
# print (d2-d1).days
# date = datetime.datetime.now()
# date1 = datetime.timedelta(days=1)
# tomorrom = date+date1
# print tomorrom
# print str(tomorrom)[:-7]
# date2 = datetime.timedelta(days=-1)
# quest = date+date2
# print quest
# now = datetime.datetime.now()
# delta = datetime.timedelta(days=-100)
# oldTime = now+delta
# print oldTime.strftime('%Y-%m-%d %H:%M:%S')
# print datetime.datetime.now()-datetime.timedelta(days=200)
#
# hours1 = datetime.timedelta(hours=3)
# print str(now)[:7]
# hours2 = now+hours1
# print str(hours2)[:-7]
# seconds = datetime.timedelta(hours=1,seconds=30).total_seconds()
# print seconds
# minute = datetime.timedelta(hours=1,minutes=20,seconds=20).total_seconds()
# print minute
# noe = time.time()
# noer = datetime.datetime.timetuple(noe)
# print datetime.datetime.strftime('%Y-%m-%d %H:%M:%S',noe)
# noe = datetime.datetime.now()
# print noe
# daes = datetime.timedelta(days=-3)
# print noe+daes
# hours1 = datetime.timedelta(hours=-3)
# minutes = datetime.timedelta(minutes=-3)
# print noe+hours1
# print noe+minutes
# time1 = datetime.timedelta(days=1)
# print 'tomrrom:',noe+time1
# print 'yestday:',noe-time1
# print datetime.datetime.combine(datetime.datetime.today(),datetime.time(17,12,35))
# t = time.time()
# dataa = datetime.datetime.fromtimestamp(t)
# print dataa.strftime('%Y-%m-%d %H:%M:%S')

# with open('D:\\tmp\\t1.txt') as fp:
#     info = fp.readlines()
#     num = 0
#     for i in info:
#         if num%5==0 and num != 0:
#             stra = raw_input(u'输入任意字符继续：')
#         formatTime = time.localtime()
#         str1 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#         time.sleep(1)
#         print '[',str1,']',i
#         num +=1

# for i in calendar.day_name:
#     print i,
# print
# for i in calendar.day_abbr:
#     print i,
# print
# for i in calendar.month_name:
#     print i,
# print
# for i in calendar.month_abbr:
#     print i,

# if calendar.isleap(2000) is True:
#     print u'2000年是闰年'
# else:
#     print u'2000年不是闰年'

# print calendar.month(2015,3,1,1)
# print '*'*40
# print calendar.calendar(2015,1,1,1)
#
# myCal = calendar.HTMLCalendar(calendar.SUNDAY)
# print myCal.formatmonth(2016,7)
# with open('calendar.html','w') as fp:
#     fp.write(myCal.formatmonth(2016,7))

# ls = time.localtime()
# print ls[0],':',ls[1],':',ls[2]
# print ls.tm_year
#
# print "*"*40
# lr = time.gmtime()
# print lr[0],':',lr[1],':',lr[2]
# print lr.tm_year

# print time.time()
# print int(time.time())
# print time.localtime(144093883)
# print time.mktime(time.localtime())
# array = [2,1,54,333,12,123]
# lenArray = len(array)
# max = max(array)
# min = min(array)
# maxIndex = array.index(max)
# if maxIndex != 0:
#     array[0],array[maxIndex] = max, array[0]
# minIndex = array.index(min)
# if minIndex != lenArray-1:
#     array[-1],array[minIndex] = min, array[-1]
# print array

# for i in xrange(1,10):
#     for j in xrange(1,i+1):
#         print '%d*%d'%(j,i),'=',j*i,
#     print
# msg = {'a':1,'b':2,'c':3,'d':4}
# default = 'invaild'
# print msg.get(raw_input(),default)

# import numpy as np
#
# L = np.arange(1,21)
# print(L)
#
# for i in L:
#     out = []
#     if i<=2:
#         l = np.arange(1,6)
#     elif i>=18:
#         l = np.arange(15,21)
#     else:
#         l = np.arange(i-2,i+3)
#     for j in l:
#         if j==i:
#             out.append(str(j)+'*')
#         else:
#             out.append(str(j))
#     print(i,out)
#
#
#
#
#
# def insertSort(listx):
#     xLen = len(listx)
#     for i in xrange(1,xLen):
#         # key = listx[i]
#         j = i-1
#         while j >= 0:
#             if listx[j] > listx[j+1]:
#                 # listx[j+1] = listx[j]
#                 # listx[j] = key
#                 listx[j+1],listx[j] = listx[j],listx[j+1]
#                 j -= 1
#             else:
#                 break
#     return listx
#
#
# list2 = [23,45,12,2,3,0,45,67,14,0]
#
# if len(list2) < 2:
#     print list2
#
# for i in xrange(len(list2)):
#     j = i
#     while j >= 0:
#         if list2[j] < list2[j-1]:
#             tmp = list2[j]
#             list2[j] = list2[j-1]
#             list2[j-1] = tmp
#         else:
#             break
#         print list2
#         j -= 1
# print list2

def func1(pipe):
    list1 = []
    sendStr = ''
    while sendStr != '#':
        time.sleep(0.01)
        sendStr = raw_input(u'请输入字符串，以#号结束：')
        if sendStr == '#':
            break
        list1.append(sendStr)
    for i in list1:
        pipe.send(i)
        # rcv = pipe.recv()
        # with open('c.txt','a+') as fp:
        #     fp .write(str(rcv)+'\n')

def func2(pipe):
    while True:
        time.sleep(0.01)
        rcv = pipe.recv()
        with open('D.txt','a+') as fp:
            fp .write(rcv+'\n')


if __name__=='__main__':
    pipe = Pipe()#上面传入的参数必须和管道的变量一致
    print len(pipe)
    p1 = Process(target=func1,args=(pipe[0],))
    p2 = Process(target=func2,args=(pipe[1],))
    p2.start()
    time.sleep(0.1)
    p1.start()
    p2.join()
    p1.join()












