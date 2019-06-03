# encoding=utf-8
import random,os
# 1、实现自己的数学模块mymath，提供有4个函数，分别为加减乘除，
# 在B模块中调用A模块的函数。
# 把当前的py文件当做B模块,mymath作为A模块
import mymath

print mymath.add(1,2)
print mymath.division(2,4)
print mymath.ride(4,8)
print mymath.sub(9,3)



# 2、实现自己的字符串模块mystr，里面有方法：isdigit,strip,
# join,split
import mystr
str3 = '\n\t abc ccc\n\t '
print mystr.Strip(str3)
str4 = '*bay *bay*'
print mystr.Strip(str4,'*')
print mystr.Split('bbog bog bogbb','bb',-2)
print mystr.Join(['abc','xyz','glory road'])
print mystr.Join(['abc','123','oj'],'*')
print mystr.Isdigit('109')


#老师的方法在mystr_01

# 3、构建一个模块的层级包
# 在当前的目录下面建立和当前文件同级的package：p1，
# 在p1下面建立两个模块分别为，p11和p12，

import p1
print p1.p11.b
print p1.p12.a


# 4、实现一个除法函数，并处理异常

def subError(x,y):
    try:
        return x/y
    except ZeroDivisionError,e:
        return u'除法异常'

if __name__=='__main__':
    print subError(4,0)


def div(x,y):
    try:
        return x/y
    except ZeroDivisionError,e:
        print e.message
    else:
        print 'no exception'

print div(3/54)
print


# 5、引发一个异常，并将它抛除到上层函数，上层函数捕获该异常并处理

def boHuoError():
    '''
    用户输入非数值，则把异常抛出到上层函数处理，输入0则捕获异常进行处理
    :return:
    '''
    try:
        num = int(raw_input('请输入一个数值：'))
        numnoe = 4/num

        return numnoe
    except ZeroDivisionError,e:
        return e

if __name__=='__main__':
    print boHuoError()


# 老师的方法：
def func1():
    raise Exception('zte')

def func2():
    try:
        func1()
    except Exception,e:
        pass


# 6、实现字符串、列表、元组和set之间互相转换

def printSet(sep):
    print u'原始序列：',sep
    print u'转换成set：',set(sep)

if __name__=="__main__":
    str1 = '1112345'
    str2 = 'ababcdfb'
    list1 = ['1','2','1','4','5','2']
    list2 = [1,2,3,1,2,3,4,5,6,7,6]
    tuple1 = ('1','2','1','4','5','2')
    tuple2 = (1,2,3,4,2,3,1,2,6)
    printSet(str1)
    printSet(str2)
    printSet(list1)
    printSet(list2)
    printSet(tuple1)
    printSet(tuple2)



# 7、结合set对象，统计某个list出现的重复元素个数

def ChongFu(list1):
    '''
    计算有重复的元素个数
    :param list1:
    :return:
    '''
    ste1 = set(list1)
    sun = 0
    for i in ste1:
        if list1.count(i)>1:
            sun +=1
    print u"重复元素个数：",sun

if __name__=="__main__":
    list1 = ['1','1','2','1','1','4','5','2','6','6','7','6']
    ChongFu(list1)

# 老师的方法：
list1 = ['1','1','2','1','1','4','5','2','6','6','7','6']
set1 = set(list1)
for i in set1:
    print 'count',i,':',list1.count(i)




# 8、定义一个元组，向元组中添加元素或者修改已有元素，并捕获异常

def fixTuple(tuple1):
    '''
    向元组中添加元素或者修改已有元素，并捕获异常
    :param tuple1:
    :return:
    '''
    try:
        print u'修改前的元组',tuple1
        tuple1[1]=3
    except TypeError,e:
        print u'元组修改元素异常：',e


def addTuple(tuple2):
    '''
    向元组中添加元素,并捕获异常
    :param tuple1:
    :return:
    '''
    try:
        print u'添加前的元组',tuple2
        tuple2 = tuple2+(8,)
        print u'添加后的元组',tuple2
    except TypeError,e:
        print u'元组添加元素异常：',e

if __name__=="__main__":
    tuple1 = (1,2,3,4,5)
    tuple2 = ('1','2','3','4','5')
    fixTuple(tuple1)
    addTuple(tuple2)

# 老师的方法：
tuple1 = tuple([1,2,3,4])
try:
    tuple1[1] = 12
except ArithmeticError,e:
    print e.message




# 9、删除无重复元组中给定的元素

def DeleteTuple(tuple):
    '''
    删除无重复元组中给定的元素
    :param tuple:
    :return:
    '''
    try:
        del tuple[1]
        print tuple

    except TypeError,e:
        print u'删除无重复元组中给定的元素：',e
if __name__=="__main__":
    tuple1 = (1,2,3,4,5)
    DeleteTuple(tuple1)
# 老师的方法：
def removeTupleElement(tup,e):
    setVal = set(tup)
    setVal.remove(e)
    return tuple(setVal)

tuple1 = (1,2,3,4,5)
ret = removeTupleElement(tuple1,3)
print ret


# 10、有一个ip.txt，里面每行是一个ip，实现一个函数，
# ping 每个ip的结果，把结果记录存到ping.txt中，
# 格式为ip:0或ip:1 ，0代表ping成功，1代表ping失败

def pingIP(ippath,pingpath):
    with open(ippath,'a+') as fp:
        fp.writelines('192.168.1.101'+'\n')
        fp.write('120.123.12.1'+'\n')
        fp.write('192.168.1.1'+'\n')
        fp.write('1@.1@.1.104'+'\n')
        fp.seek(0)
        line = fp.readlines()
    for i in line:
        msg = os.system('ping '+ i.strip())
        print msg
        with open(pingpath,'a') as fp:
           fp.write(i.strip()+':'+ str(msg)+'\n')

if __name__=="__main__":
    ippath = 'D:\\tmp\\ip.txt'
    pingpath = "D:\\tmp\\ping.txt"
    pingIP(ippath,pingpath)


