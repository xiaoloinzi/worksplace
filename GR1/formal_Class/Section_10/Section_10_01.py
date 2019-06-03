# encoding=utf-8
import time,sys
# 面向过程：
# 做一件事->分为几个步骤->封装函数->完成
#
# 面向对象：把所有的东西都抽象为网络对象
#
#
# 函数式编程：
# a = lambda x:x
# f(x) = x+1
#
# 基于并发式编程
# Erlang语言
# 单进程、单线程
# 多进程、多进程的编程方式
# new thread
# process

class Foo(object):

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __init__(self):
        print '__init__'

    def __init__(self,*args):
        if len(*args) == 2:
            self.name = args[0]
            self.age = args[1]
        else:
            print 'no agrs'

    def bar(self):#self代表是一个实例方法
        pass

# obj = Foo('andy',18,30000)
# obj1 = Foo()
# 习题：创建一个雇员employee的类，
# 初始化name和salary，并且定义一个方法能显示其工资
# 习题2：对于雇员类，需要知道当前的雇员总数，并且能显示雇员总数。
# 什么样的属性来承载员工总数
# 习题3：不创建实例，显示员工数--使用类方法
# 习题4：定义一个静态方法，打印消息，当下打印如下的信息
# ‘所有员工到操场集合’

class Employee(object):
    employee = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.employee +=1

    def Salary1(self):
        print  'name :%s salary:%s'%(self.name,self.salary)

    def getEmployee(self):
        print u'当前雇员的数量：',Employee.employee

    @classmethod#类方法
    def classemployee(cls):
        print u'当前雇员的数量：',cls.employee
# 静态方法场景：为了独立于类及实例，
# 在面向对象的编程中，为了解决某一类问题而设置的方法。
    @staticmethod
    def printemp(str1):
        print str1

obj = Employee('lin',30000)
obj = Employee('lin',30000)

Employee.classemployee()
Employee.printemp('所有员工到操场集合')
obj.printemp('上课了')

# 类：类属性
#
# 实例：实例属性
# 1）实例中可以引用类的属性
# 2）通过类名引用
# 3）通过实例名--读取操作（类的属性）--写操作（实例的属性）

# 习题5：
# 描述类方法、实例方法、静态方法的区别，以及他们在调用上的区别，
# 例如实例方法只能被实例调用，不能被类调用等
# 实例方法：由对象调用；至少一个self参数；执行实例方法时，
# 自动将调用该方法的对象赋值给self；

# 类方法：由类调用； 至少一个cls参数；执行类方法时，
# 自动将调用该方法的类复制给cls；

# 静态方法：由类调用；无默认参

# 闭包-->装饰器是其的一个子集
# 作用域

outVal = 'this is a global val'

def test():
    innerVar = 'this is local var'
    print 'local vars'
    print locals()

test()
print 'global vars'
print globals()

def outter():
    name = 'python'
    def inner():
        print name
    return inner
print outter()
res = outter()
res()
# 问题：如何判断一个合适是闭包--使用func_closure返回对象就是闭包

print res.func_closure
print outter.func_closure


# 习题6：写一个闭包，完成浮点数到时间字符串的转换，
# 浮点数作为参数传入。并且判断该函数是否是一个闭包

def printtime(str1):
    time1 = time.localtime(str1)
    def inner():
        print time.strftime('%Y-%m-%d %H:%M:%S',time1)
    return inner
print printtime(1212)
res = printtime(0)
if res.func_closure:
    print '是闭包'
    res()
else:
    print None
def now():
    print 'crrent time is %s'%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

res = now()

def log(func):
    def wrapper(*agrs,**kwagrs):
        print 'call %s'%func.__name__
        return func(*agrs,**kwagrs)
    return wrapper
# @classmethod-->classmethod(xxx)
@log#log(now)
def now():
    now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    print 'current time is %s'%now

now()
# 习题：
# @log产生的实际效果是怎样。



# 习题：写一个装饰器，完成如下的功能：
# 在调用函数之前，写如下格式的文件：
# 2017-12-12 09:33:23|info|enter xxx function
# 离开函数的时候，写如下格式的文件：
# 2017-12-12 09:33:23|info|exit xxx function
def log(func):
    def wrapper(*agrs,**kwagrs):
        str1 = '2017-12-12 09:33:23|info|enter %s function'%func.__name__
        with open('t1.txt','w') as fp:
            fp.write(str1)
        func(*agrs,**kwagrs)
    return wrapper
# @classmethod-->classmethod(xxx)
@log#log(now)
def now():
    # now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    # print 'current time is %s'%now
    with open('t1.txt') as fp:
        na = fp.read()
    print na

now()

# 习题7：return func(*args,**kwargs)
# 和 func(*args,**kwargs)的区别，
# 直接使用func(*args,**kwargs)是否可以。

def log(func):
    def wrapper(*agrs,**kwagrs):
        print 'call %s'%func.__name__
        return func(*agrs,**kwagrs)
    return wrapper
# @classmethod-->classmethod(xxx)
@log#log(now)
def now(a,b):
    now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    print 'current time is %s'%now
    print 'a is:',a
    print 'b is :',b
# now(1,2)=log(now)(1,2) = wrapper(1,2)=1、xxx2、now(1,2)

now()

# 习题：写一个装饰器，完成如下的功能：
# 在调用函数之前，写如下格式的文件：
# 2017-12-12 09:33:23|info|enter xxx function
# 离开函数的时候，写如下格式的文件：
# 2017-12-12 09:33:23|info|exit xxx function

def log(func):
    def wrapper(*agrs,**kwagrs):
        str1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+'|info|enter %s function'%func.__name__
        with open('t1.txt','w') as fp:
            fp.write(str1)
        res = func(*agrs,**kwagrs)
        str2 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+'|info|exit %s function'%func.__name__
        with open('t1.txt','a') as fp:
            fp.write('\n'+str2)
        return res
    return wrapper
# @classmethod-->classmethod(xxx)
@log#log(now)
def now():
    # now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    # print 'current time is %s'%now
    with open('t1.txt') as fp:
        na = fp.read()
    print na

now()
# 封装：
class Employee(object):
    def __init__(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

    def __cry(self):
        print self.__name,'is crying'

#
e1 = Employee('wulao')
# print e1._Employee__name
print e1.getName()
e1.setName('lin')
print e1.getName()
# e1._Employee__cry()

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.__score = score

    @property
    def score(self):
        return self.__score

    def getscore(self):
        return self.__score

    @score.setter
    def setscore(self,score):
        if not isinstance(score,int):
            raise ValueError('must be an int')
        if score<0 or score>100:
            raise ValueError('must between 0-100')
        self.__score=score
s1 = Student('a',18,90)
print s1.score
# s1.setscore()
# s1.getscore()
# s1.setscore(999)
# s1.getscore()
s1.setscore = 99
print s1.name,s1.age,s1.score


# 习题：在Student 类中，self.__birth（时间元组）
# @property 读写 该属性1990-12-21

class Student(object):
    def __init__(self,name,age,score,birth):
        self.name = name
        self.age = age
        self.__score = score
        self.__birth = birth

    @property
    def birth(self):
        return time.strptime(self.__birth,'%Y-%m-%d')

    @birth.getter
    def birth(self):
        return time.strptime(self.__birth,'%Y-%m-%d')

    @birth.setter
    def birth(self,birth):
        self.__birth=birth

s1 = Student('a',18,90,'1997-10-15')
print s1.birth
s1.birth = '1992-10-15'
print s1.birth

class Student(object):
    def __init__(self,name,age,score,birth):
        self.name = name
        self.age = age
        self.__score = score
        self.__birth = birth

    @property
    def birth(self):
        return self.__birth

    @birth.getter
    def birth(self):
        return time.strptime(self.__birth,'%Y-%m-%d')

    @birth.setter
    def birth(self,birth):
        self.__birth=time.strptime(self.__birth,'%Y-%m-%d')

s1 = Student('a',18,90,'1997-10-15')
print s1.birth
s1.birth = '1992-10-15'
print s1.birth

# 习题：在上述的代码中，让各属性方法可以达到真正的效果
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.__score = score

    @property
    def birth(self):
        return time.strptime(self.__birth,'%Y-%m-%d')

    @birth.setter
    def birth(self,birth):
        self.__birth=birth

    @birth.deleter
    def birth(self):
        print 'del birth'
        del self.__birth

s1 = Student('a',18,90)
s1.birth = '1992-10-15'
print s1.birth
del s1.birth
print s1.birth

class Student(object):
    def __init__(self,name,age,score,birth):
        self.name = name
        self.age = age
        self.__score = score
        self.__birth = birth

    @property
    def birth(self):
        return self.__birth

    @birth.getter
    def birth(self):
        return time.strptime(self.__birth,'%Y-%m-%d')

    @birth.setter
    def birth(self,birth):
        self.__birth=time.strptime(self.__birth,'%Y-%m-%d')

# 学习属性，getattr(object,name)


#什么样的属性来承载员工总数
class Employee(object):
    count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def showSalry(self):
        print 'NAME: %s .SALARY:%s'%(self.name,self.salary)
    @classmethod
    def showEmCount(cls):
        print cls.count
    #类方法
    @classmethod
    def func1(cls):
        print 'abc'
        print cls.count
    @staticmethod
    def broadcast(msg):
        print msg

def add(x,y):
    Employee.count = 1
    return x+y

wulao = Employee('wulao',30000)
#
# #学习属性，getattr(obj,name) hasattr(obj,name) setattr(obj,name,value) delattr(obj,name)
# print 'wulao salary:', getattr(wulao,'salary')
# print hasattr(wulao, 'sex')
# setattr(wulao,'sex','male')
# print wulao.sex
# delattr(wulao,'sex')
#
# # 习题：针对class 使用这四个方法
#
print getattr(Employee,'count')
print hasattr(Employee, 'sex')
print setattr(Employee,'sex','male')
delattr(Employee,'sex')
print hasattr(Employee, 'sex')


class Employee(object):
    count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def showSalry(self):
        print 'NAME: %s .SALARY:%s'%(self.name,self.salary)

    @property
    def salsry(self):
        pass

# s = Employee('lin',14)
# s.salsry='lin'
print getattr(Employee,'salsry')
print getattr(Employee,'showSalry')
print hasattr(Employee, 'sex')
print setattr(Employee,'sex','male')
delattr(Employee,'sex')
print hasattr(Employee, 'sex')

# 继承：多继承、单继承
class Parent(object):
    parentAttr = 100
    def __init__(self,name,age):
        print 'Calling parent constructor'
        self.name = name
        self.age = age

    def parentMethod(self):
        print 'Calling parent method'

    def setAttr(self,attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print 'Parrent attribute:',Parent.parentAttr

class Childl(Parent):

    def __init__(self):
        print 'calling child1 constructor'

    def childMethod(self):
        print 'Calling child1 methed'
        Parent.parentMethod(self)#表示当前方法的实例传入参数

class Child2(Parent):
    def childMethod(self):
        print 'calling child2 method'
        self.parentMethod()
# 需要父类的初始化的属性，也要自己做点事情
# superclassname.__init__(self,params)
# super(subclassname,self).__init__(params)
class Child3(Parent):
    def __init__(self):
        # Parent.__init__(self,'lin',12)
        Parent.__init__(self,'lin',12)
        print 'calling child3 method'

# 1、c1 = Child1() 打印什么
# 2、print c1.name的结果
# 3、print c1.parentAttr

c1 = Childl()
# print c1.name
# print c1.parentAttr
c2 = Child2('lin',22)
# print c2.name
# c3 = Child3()
# print c3.name
# print c3.parentAttr
c1.childMethod()
c2.childMethod()

class Parent(object):
    parentAttr = 100
    def __init__(self,name,age):
        print 'Calling parent constructor'
        self.name = name
        self.age = age
    def parentMethod(self,name):
        print 'Calling parent method'
        print 'your old name is %s'%self.name
        print 'your new name is %s'%name
        self.name = name
    def setAttr(self, attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print 'Parrent attribute:',Parent.parentAttr

class Child1(Parent):
    def __init__(self,name,age):
        Parent.__init__(self,name,age)
        print 'Calling child1 constructor'
    def childMethod(self,name):
        print 'Calling child1 method'
        Parent.parentMethod(self,name)

class Child2(Parent):
    def childMethod(self):
        print 'Calling child2 method'
        self.parentMethod()


c1 = Child1('lin',12)
# c2 =Child2()
print c1.name
c1.parentMethod('kk')
print c1.name
# isinstance()--判断类实例
# issubclass()--判断类子类
print isinstance(c1,Child1)
print isinstance(c1,Child2)
print issubclass(Child1,Parent)
print issubclass(Child2,object)

# 多重继承
class D(object):
    def bar(self):
        print 'D;bar'

class C(D):
    def __init__(self):
        print 'C:init'
    def bar(self):
        print 'C:bar'

class B(D):
    def __init__(self):
        print 'B:init'

    # def bar(self):
    #     print 'B:bar'
# # 习题： 在A的构造方法中，使用B和C的构造方法
#
class A(B,C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)

    def bar(self):
        print 'A:bar'

a1 = A()
a1.bar()


# moloc() free()
# 1、引用计数

class Point(object):
    def __init__(self,x =0,y=0):
        self.x = x
        self.y = y

    def __del__(self):
        className = self.__class__.__name__
        print className,u'销毁'

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1),id(pt2),id(pt3)
print sys.getrefcount(pt1)
print sys.getrefcount(pt2)
del pt1
print 'pt1 deleted'
del pt2
print 'pt2 deleted'
del pt3
print 'pt3 deleted'
# 2、标记-清除
# 循环引用的问题
a1 = []
a2 = []
a1.append(a2)
a2.append(a1)
print 'a1:',a1#[[[....]]]
print 'a2:',a2
print sys.getrefcount(a1)
del a1#没有清除
del a2#没有清除
print sys.getrefcount(a1)
# root object：对象呗其他对象引用，但是自身没有引用其他对象
# Unreachable：其他
# 引用减一 a->b--导致误删

# 8、实现栈类
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack(object):
    def __init__(self):
        self.top = None
    def pop(self):
        if self.top == None:
            return None
        retVar = self.top.val
        self.top = self.top.next
        return retVar

    def push(self,node):
        node.next = self.top
        self.top = node
    def isempty(self):
        pass

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
s1 = Stack()
s1.push(n1)
s1.push(n2)
s1.push(n3)
s1.push(n4)
s1.push(n5)
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()



