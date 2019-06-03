# encoding=utf-8
# 习题，对于如下列表，返回第2个元素到第4个元素，不少于两种方法：
#
list2 = [1, 2, 3, 4, 5, 6, 7 ]
# print list2[2:5]
print list2[-5:-2]
print 'new list:',list2[1:4]
for i in xrange(len(list2)):
    if i >=2 and i<=4:
        print list2[i],
print

# 列出你们所知道的列表运算符
list1 = [1,2,3,4]
print  list1 + list2#组合
print  list1 * 2#重复
print 3 in list1#是否存在
for i in list1:#迭代
    print i,
print
print len(list1)#长度
list2 = list1
list3 = list1[:]

print list2 is list1
print list3 is list1
# 1、比较两个列表中的元素是否相等，不少于两种方法
# 2、取出列表中的最大元素，不少于两种方法
print 'list1:',list1,'list2:',list2
print list1==list2#也可以用于比较字符串
# 也可以使用for进行遍历去比较，但是在比较之前，要比较长度是否相等
print cmp(list1,list2)#比较两个变量的值是否相等
print max(list1)
list1.reverse()
print list1
print list1[0]
list3 = [2,6,8,1,9]
list3.sort()
print list3[-1]
# 3、对于列表[1,2,3,4,5,6]，在列表的末尾添加一个元素7
# 4、在列表[1,2,3,4,5,6]，在2和3中间，添加一个元素1024
# 5、在列表[1,2,3,4,5,6]中，使用不少于三种方法删除数字3

list5 = [1,2,3,4,5,6]
list6 = [1,2,3,4,5,6]
list7 = [1,2,3,4,5,6]
list8 = [1,2,3,4,5,6]
list9 = [1,2,3,4,5,6]
list5.append(7)
print list5
list6.insert(2,7)
print list6
for i in range(len(list7)):
    if list7[i] == 3:
        del list7[i]
        break
print list7
del list8[2]
print list8
list9.remove(3)
print list9
list11 = [1,2,3,4,5,6]
a = list11.pop(2)#pop(index) 移除列表中的一个元素
# （默认最后一个元素），并且返回该元素的值
print list11
# 6、统计列表[1,2,3,4,5,6,3,4,5,6,3]中3出现的次数，不少于两种方法
list12 = [1,2,3,4,5,6,3,4,5,6,3]
n = 0
for i in list12:
    if i == 3:
        n +=1
print n
print list12.count(3)
# 7、反转列表[1,2,3,4,5,6]中的元素，不少于两种方法
list13 =[1,2,3,4,5,6]
list13 = list13[::-1]
print list13
list13.reverse()
print list13
# 8、对于列表：[2387483,454,23,456,45,454],
# 返回454首次出现的索引位置，方法不少于两种
list10 = [2387483,454,23,456,45,454]
for i in xrange(len(list10)):
    if 454 == list10[i]:
        print i
        break
print list10.index(454)
for key,value in enumerate(list10):
    if value == 454:
        print key
        break

# sort方法的使用
# L.sort(cmp=None,key=None,reverse=Flase)
# cmp比较的方式，可以等于函数名，key可以

list16 = [(1,5,3),(1,3,6,3),(1,1,2,4,5,6),(1,9)]
def L(tup):
    return len(tup)
list16.sort(key=L,reverse=True)
print list16

# list1 = [(-1,5,3),(-5,3,6,3),(1,1,2,4,5,6),(2,9),(-2,10)]，
# 请大家修改代码实现，
# 使用元组的第一个元素大小比较来实现 list 的排序，逆序排列,需要自定义cmp参数
list17 = [(-1,5,3),(-5,3,6,3),(1,1,2,4,5,6),(2,9),(-2,10)]

def LL(x,y):
    if x==y:
        return 0
    elif x>y:
        return 1
    else:
        return -1


def LLL(tup):
    return tup[0]
list17.sort(cmp=LL,key=LLL,reverse=False)
print list17

# 老师的方法
def tkey(tup):
    return tup[0]

def tcmp(x,y):
    if x==y:
        return 0
    elif x>y:
        return 1
    else:
        return -1
list17.sort(cmp= tcmp,key=tkey,reverse=True)
print list17
# 按绝对值比较大小，逆序排序
def tkey(tup):
    return tup[0]

def tcmp(x,y):
    if abs(x)==abs(y):
        return 0
    elif abs(x)>abs(y):
        return 1
    else:
        return -1

list17.sort(cmp= tcmp,key=tkey,reverse=True)
print list17
# 方法二
def tkey(tup):
    return abs(tup[0])#通过该key为绝对值来做比较

def tcmp(x,y):
    if abs(x)==abs(y):
        return 0
    elif abs(x)>abs(y):
        return 1
    else:
        return -1

list17.sort(cmp= tcmp,key=tkey,reverse=True)
print list17

# 列表生成器
list18 = [1,2,3,4]
list19 = [2*i for i in list18 if i>2]
list20 = [m+n for m in 'ABC' for n in 'XYZ']
dict1 = {'x':'A','y':'b','z':'c'}
list21 = [k+'='+v for k,v in dict1.items()]
list23 = ['Hellow','World','IBM','Apple']
list24 = [s.lower() for s in list23]



# list22 = [m+n for m in 'ABC' for n in 'XYZ'if m+n =='AX' or m+n == 'BY' or m+n == 'CZ']
list22 = [m+n for m in 'ABC' for n in 'XYZ'if 'ABC'.index(m)=='XYZ'.index(n)]
print list22
print ['ABC'[i]+'XYZ'[i] for i in xrange(len('ABC'))]

print map(lambda x,y:x+y,'ABC','XYZ')#不是列表生成器，只是返回为一个列表


import copy
a = [1,2,3,4,['a','c']]
# 拷贝：浅拷贝,子串还是拷贝地址
# 深度拷贝：全部拷贝，重新生成一个列表
b = copy.copy(a)
c = copy.deepcopy(a)

a[4].append(5)
del a[2]

print a
print b
print c

# 练习题2： 完成引用复制和非引用复制的一个例子
lista = [1,2,3,4,6,7]
list30 = [1,2,3,'a','b']
listb = lista
listc = copy.deepcopy(lista)#非引用复制
lista.append(2)
print lista
print listb
print listc


# 练习题3： 找到两个列表中不同的元素和相同元素
list33 = [1,2,3,4,6,7]
list34 = [1,2,3,'a','b']
list31 = []
list32 =[]
for i in list33:
    if i in list34:
        list31.append(i)
    else:
        list32.append(i)
for j in list34:
    if j not in list33:
        list32.append(j)
print u'原列表为：',list33,u'和',list34
print u'相同的元素：',list31
print u'不同的元素',list32
# 老师的方法

list04 = [1,2,3,3]
list05 = [1,2,3,4,5,5]
listS = [x for x in list04 if x in list05]
listD = [x for x in list04 if x not in list05]+[x for x in list05 if x not in list04]
print listS,listD

# 练习题4：数字和字母混合的list中，奇数位如果是数字，
# 则加1，偶数位如果是数字，则加2
list35 = [1,2,3,6,7,'a','b']
for i in xrange(1,len(list35)+1):
    if isinstance(list35[i-1],int) and i%2==0:
        list35[i-1] = list35[i-1]+2
    elif isinstance(list35[i-1],int) and i%2!=0:
        list35[i-1] = list35[i-1]+1
print list35
# 老师的方法
list06 = [1,23,344,'d','f',898]
for i in xrange(len(list06)):
    if isinstance(list06[i],int):
        if i%2==0:
            list06[i] +=1
        else:
            list06[i] +=2
print list06


# 练习题5： 递归处理嵌套的list
list07 = [[12],[12,[12,[123],[12345]]]]
def printVal(var):
    for i in var:
        if isinstance(i,list):
            printVal(i)
        else:
            print i
printVal(list07)
# 练习题6:遍历list， 但是list中元素的数据类型不定，
# 有可能有嵌套的list， 嵌套的tuple， dict等
list36 = [1,2,3,(4,5,6),{'x':7,'y':8}]
for i in list36:
    if isinstance(i,tuple):
        for j in i:
            print j
    elif isinstance(i,dict):
        for key,value in i.items():
            print key,value
    else:
        print i

# 老师的方法，在第五题的基础上
list08 = [[1,2,3,[12,34]],(4,5,6),{'x':7,'y':8},123]

def printVall(var):
    for i in var:
        if isinstance(i,list) or isinstance(i,tuple):
            print i
        elif isinstance(i,dict):
            for key,value in i.items():
                print key,':',value
        else:
            print i

printVall(list08)

from collections import Iterable
list1 = [[1,2,3],(4,6,7,9),{'a':1,'b':2},123]
listOut = []
def func1(listIn):
    for i in listIn:
        if not isinstance(i,Iterable):
            listOut.append(i)
        else:
            func1(i)
    return listOut
print func1(list1)

# 练习题7: 通过遍历list去掉重复部分[1,23,4,5,67,4,4,3,2,345,34]
list40 = [1,23,4,5,67,4,4,3,2,345,34]
list41 =[]
for i in list40:
    if i not in list41:
        list41.append(i)

print list41

# 另外一种方法
list1 =[1,23,4,5,67,4,4,3,2,345,34]
for i in list1:
    if list1.count(i)>1:
        list1.remove(i)
print list1

# 老师的方法
for i in list40:
    num = list40.count(i)
    while num>1:
        list40.remove(i)
        num = list40.count(i)
print list40


# 练习题8：1个纯数字的list中，分别输出奇数坐标字符或偶数坐标字符
list42 = [1, 23, 4, 5, 67, 3, 2, 345, 34]
print list42[::2]
print list42[1::2]
# 练习题9：找到序列中最大的元素
list43 = [1, 23, 4, 5, 67, 3, 2, 345, 34]
print max(list43)

# 练习题10：返回列表中第二大元素
list44 = [1, 23, 4, 5, 67, 3, 2, 345,345,34]

for i in list44:
    if list44.count(i)>1:
        list44.remove(i)
list44.sort()
print list44[-2]
# 练习题11：键盘读入一字符串，逆序输出
str1 = raw_input('please input string:')
print str1[::-1]
