# encoding=utf-8
# 1、方法的重载
# func(int a,int b)
# func()
# func(int a,int b,int c)
# func(a1,b1)
# func(a1,b1,c1)
#
# 2、方法的重写
# class A(B):
#     子类方法重写和父类的方法没有关系，而是一个重新的方法
class Parent(object):
    def myMethod(self):
        print 'class Parent'
    def printName(self):
        print 'my name is lily'

class Child(Parent):
    def myMethod(self):
        print 'call child'
c = Child()
c.myMethod()
c.printName()

class Vector(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d,%d)'%(self.a,self.b)

    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)

v1 = Vector(2,8)
v2 = Vector(4,98)
# print v1+v2
v3 = v1+v2
print v3
print v1
# 3、有一个雇员类，实例相加的结果是返回一个新的雇员实例，
# 且工资是原先两个人工资之和的2/3，姓名可任意指定

class Vector(object):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return '%s %d'%(self.name,self.salary*(2.0/3.0))

    def __add__(self, other):
        return Vector(self.name+other.name,self.salary+other.salary)

v1 = Vector('a',8)
v2 = Vector('b',98)
# print v1+v2
v3 = v1+v2
print v3
print v1

# 老师的方法：

class Vector(object):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    def __add__(self, other):
        return Vector('lin',(self.salary+other.salary)*2.0/3.0)


v1 = Vector('a',8)
v2 = Vector('b',98)
# print v1+v2
v3 = v1+v2
print v3.salary

class A(object):
    '''
    Production of thr class A:
    attr:
    method:
    end.
    '''
#     __getitem__
# __setitem__
# __delitem__
    def __getitem__(self, item):
        print 'get item'

    def __setitem__(self, key, value):
        print 'set item'

    def __delitem__(self, key):
        print 'del item'

# print A.__doc__
a = A()
a['key1']
a['k2'] = 12
del a['k3']


# 习题：定义一个实例属性，完成针对该属性的字典操作，
# 覆盖增加、删除、修改、查找
# 使用雇员类。
class A(object):
    def __init__(self):
        self.deictVar = {}


    def __getitem__(self, key):
        if self.deictVar.has_key(key):
            return self.deictVar[key]
        else:
            print 'the key not exist'
            return None

    def __setitem__(self, key, value):
        print 'set item'
        self.deictVar[key] = value

    def __delitem__(self, key):
        del self.deictVar[key]

    # __getslice__
    # __setslice__
    # __delslice__
    def __getslice__(self, i, j):
        print '__getslice__',self.sequence[i:j]
    def __setslice__(self, i, j, sequence):
        print '__setslice__',i,j
        self.sequence = sequence[i:j]
    def __delslice__(self, i, j):
        print '__delslice__',i,j
# print A.__doc__
a = A()
a['name1']=12
print a['name1']

a[1:9] = 'sdfsdfsdfsdf'
print a[2:5]
del a[2:8]
#
#
# # 题：定义一个实例属性，完成针对该属性的切片操作，
# # 覆盖增加、删除、修改、查看
#
class Employee(object):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.dictVar = {}
        self.seq = []
    def __add__(self, other):
        return Employee('cindy',(self.salary+other.salary)*2.0/3.0)
    def __getitem__(self, key):
        if self.dictVar.has_key(key):
            return self.dictVar[key]
        else:
            print 'the key not exist'
            return None
    def __setitem__(self, key, value):
        print 'set item'
        self.dictVar[key] = value
    def __delitem__(self, key):
        del self.dictVar[key]

    def __getslice__(self, i, j):
        print '__getslice__',self.seq[i:j]
    def __setslice__(self, i, j, sequence):
        print '__setslice__',i,j
        self.seq[i:j] = sequence
    def __delslice__(self, i, j):
        del self.seq[i:j]


e1 = Employee('a',10000)
e2 = Employee('a',14000)
e3 = e1 + e2
print e3.salary
print e3.name
e1['k1'] = 12
print e1['k1']
print e1['k2']
del e1['k1']
a[0:11] = 'sdfsdfsdfsdf'
print a[2:5]
print a[:]
del a[2:8]


# __call__
class Employee(object):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.dictVar = {}
        self.seq = []
    def __add__(self, other):
        return Employee('cindy',(self.salary+other.salary)*2.0/3.0)
    def __getitem__(self, key):
        if self.dictVar.has_key(key):
            return self.dictVar[key]
        else:
            print 'the key not exist'
            return None
    def __setitem__(self, key, value):
        print 'set item'
        self.dictVar[key] = value
    def __delitem__(self, key):
        del self.dictVar[key]

    def __getslice__(self, i, j):
        print '__getslice__',self.seq[i:j]
    def __setslice__(self, i, j, sequence):
        print '__setslice__',i,j
        self.seq[i:j] = sequence
    def __delslice__(self, i, j):
        del self.seq[i:j]

    def __call__(self, *args, **kwargs):
        print '__call__',args,kwargs
#     __iter__()
    def __iter__(self):
        # return iter([1,2,3,4,5])
        return iter(self.seq[:])


e1 = Employee('a',10000)
e2 = Employee('a',14000)
e3 = e1 + e2
print e3.salary
print e3.name
e1['k1'] = 12
print e1['k1']
print e1['k2']
del e1['k1']
a = Employee('a',10000)
a[0:11] = 'sdfsdfsdfsdf'
print a[2:5]
print a[:]
del a[2:8]
a(1,2,3,4,5,p1='abc',p2='def')
print Employee.__dict__
print '*'*50
print a.__dict__
# 两个属性方法的调用有什么区别
# Employee.__dict__：类的属性
# a.__dict__：实例的属性
# __iter__

for i in a:
    print i

# __new__
class A(object):
    def __init__(self):
        print 'init method'

    def __new__(cls, *args, **kwargs):
        print 'cls new method.new %s'%cls
        return object.__new__(cls,*args,**kwargs)

a = A()
# 单例--只有一个实例
# 设计一个单例之前是否创建过实例，有，则不重新创建，没有则重新创建
class A(object):
    def __init__(self,a):
        print 'init method'
        self.a = a

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
        # print 'cls new method.new %s'%cls
        # return object.__new__(cls,*args,**kwargs)

a1 = A(4)
print a1.a
a2 = A(6)
print a2.a
print a1.a
print id(a1),id(a2)

def log(patams):
    def log2(func):
        def wrapper(*args,**kwargs):
            # if patams=='a':--有参数的装饰器的意义在于通过判断装饰器的参数做不同的事

            print 'befor run',func.__name__,'the params is ',patams
            re = func(*args,**kwargs)
            print 'after run',func.__name__,'the params is ',patams
            return re
        return wrapper
    return log2

@log
def f(a,b):
    print a+b


# 带参数的装饰器：log(params)(f)(1,2)=log2(f)(1,2)
# =wrapper(1,2)=1、print XXXX;2、f(1,2)
# 3、print xxxx;4、return XXXX
@log('execute')
def f(a,b):
    print a+b

# log(f)(1,2) = wrapper(1,2)=1、print XXXX;2、f(1,2)
# 3、print xxxx;4、return XXXX--不带参数的运行逻辑

f(1,2)
f(4,5)
#
# 6、说出类方法和静态方法的区别？分别实现一个类方法和静态方法



# 7、什么是数据封装与隐藏？



# 8、什么是方法重写，方法重写的规则是什么？举一个实例










