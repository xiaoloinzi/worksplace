# encoding=utf-8
import collections
import time

# python中一切都是对象，数字、字符串是不可变对象，列表、字典是可变对象
def printme(str):
    print time.time(),'',str
    return

print printme(u'周末愉快')
a =3
print id(a)
a =5
print id(a)

list1 = [1,2,3]
print id(list1)
list1.append(4)
print id(list1)
# 传值，还是传址
number = 10
def changNum():
    global number
    number +=1
    print u'自定义函数num=',number
    print id(number)


changNum()
print u'函数调用后的number=',number
print id(number)
# for循环的是一个地址，后面叠加的是另外的地址，指向的地址不一样，所以不能无限循环

l = 'abc'
a = 'a'
for i in l:
    print i
    print id(l)
    if raw_input('please input:') != 'quit':
        l += a
        print l
        print id(l)
    else:
        break
print id(l)

def chengFao(a,n):
    j =0
    if not isinstance(a and n,(int,float)):
        raise TypeError(u'异常')
    for i in range(1,n+1):
        s = str(a)*i
        j += int(s)
    print j

print chengFao(2,4)

def sum(x,n):
    sum = 0
    for i in range(1,n+1):
        tmp = 0
        for j in range(i):
            tmp += x*10**j
        print '---',tmp
        sum += tmp
    return sum

print sum(3,4)

# 统计字符串中的字母、数字、其他字符个数
s='asADAfdsfdsafdsaf123233223@^'
a =0
b =0
c =0
for i in s:
    if i.isalpha():
        a += 1
    elif i.isdigit():
        b +=1
    else:
        c +=1

print u'字母有：',a
print u'数字有：',b
print u'其他字符：',c
def func(a,b):
    return a,b

c,d = func([123],34)
print c
print d
# raw_input和input
i = input('please:')
print i
print type(i)

def printInfo(a,c=4,*tup,**dic):
    print u'整数',a
    print u'整数',c
    print u'整数',tup
    print u'整数',dic

printInfo(1,3,4,5,x=1,y=6)
# 标点符号的处理
str1 = 'I love python,and you?'
list1 = [',','?','.',':','"']
print str1

for i in list1:
    str1 = str1.replace(i,'')
print str1
# 定义个函数，可以接收任意多个参数，计算他们的和，
# 针对其指定名称的参数，分别有如下四种：
# add=xx, sub=xx, multiply=x, divide=x
# 例如：func(23, 45, 567, add=1354, sub= 987,
# multiply=3, divide = 4)
# 的返回值是：((23+45+567)+1254 - 987)*3/4
# 加减乘除可选，但是计算顺序不变


def StrL(*arg,**agrs):
    s = 0
    for i in arg:
       s += i

#         if 'add' in agrs.keys():
#             s += agrs['add']
#         if 'su'
#
#     return (s + add - sub) * multiply/divide
# print StrL(23, 45, 567, add=1354, sub= 987,multiply=3, divide = 4)


listA = [lambda a:a+1,lambda b:b**3]
print listA[0]

g = listA[0]
f = listA[1]
print g(2046),f(2)

def makeRepeater(n):
    return lambda s:s*n

twice = makeRepeater(2)
print twice('hello world')

# 定义一个函数，其参数是method，其取值分别是如下四种’add’，’sub’，
# ’multiply’，’divide’ 。
# 针对加减乘除，返回对应的函数，并且用列表存储函数。
# 通过列表，并分别使用加减乘除函数一次。
#
# func1(method=None):
# 	使用lambda表达式，返回对应的函数
# 	并且用列表存储函数




# 1、通过eval函数，针对一个字典格式的字符串，转换成字典
# 通过eval函数，针对一个元组格式的字符串，转换成元组



# 6、字符替换
# 1）读入一个字符串
# 2）去掉字符串的前后空格	3）如果字符串包含数字则1替换成a，2替换成b，3替换成c，以此	类推 4）将字符串使用空格进行切分，存到一个列表，然后使用*号连接，	并输出
# 5）把这些功能封装到一个函数里面，把执行结果作为返回值


s = reduce(lambda x,y:x+y,range(1,10001,2))
print s
# 1、通过列表生成器，计算50以内的奇数

list1 = [x for x in xrange(1,50,2)]
print list1
print [x for x in xrange(51) if x%2]
# 迭代器
import collections

class IteratorTest():
    def __init__(self,start,end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def next(self):
        if self.current < self.end:
            self.index = self.current
            self.current += 1
            return self.index
        else:
            raise StopIteration
# it = IteratorTest(5,8)
it = xrange(5,8)
for i in it:
    print 'iterator:'+str(i)
print isinstance(it, collections.Iterable)



# 习题，定义一个迭代器IteratorTest(start,end)，其序列值是start*1,start*2 ... start*n
# 并且分别使用for 循环 以及next 方法遍历该序列。


# 习题：通过yield，写一个生成器，输入参数两个，一个起始，
# 一个终止，步长是2。并且分别使用for 循环 以及next 方法遍历。
# 并且判断该生成器是否是可迭代的
def func1(start,end):
    curVal = start
    while curVal < end:
        yield curVal
        curVal += 2
    raise StopIteration

o1 = func1(1,20)
o2 = func1(1,20)

for i in o1:
    print i

for i in range(10):
    print o2.next()

print isinstance(o1,collections.Iterable)
print type(o2)
print type(iter('123'))

# 10、有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...
# 求出这个数列的前20项之和

a = 2.0
b = 1.0
sum =0.0

for i in xrange(20):
    sum += a/b
    a,b = a+b,a

print sum





#生成器都是迭代器，__iter__() next()
#列表生成器
#函数生成器：yield
def odd():
    print 'step 1'
    yield 1 #返回值；程序停止在这里，直到下一次遍历obj.next()
    print 'step 2'
    yield 2
    print 'step 3'
    yield 3
o = odd()
# print o.next()
# print o.next()
# print o.next()

for i in o:
    print i











































































