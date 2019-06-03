# encoding=utf-8
from datetime import datetime


# class Foo:
#     '''
#     类的帮助信息
#     '''
#
#     def Bar(self):
#         print 'Bar'
#
#     def Hello(self,name):
#         print 'i am %s'%name
#
# obj = Foo()
# obj.Bar()
# obj.Hello('lin')
# print Foo.__doc__
#
# class Emplotee(object):
#     empCount = 0
#
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         Emplotee.empCount += 1
#
#     def displayCount(self):
#         print 'total employee',Emplotee.empCount
#
#     def displayEmployee(self):
#         print 'name:',self.name,'salay:',self.salary
#         # print 'dd;',he
#
# se = Emplotee('name1',10000)
# se.empCount=3
# se.displayEmployee()
# se.displayCount()
# se1 = Emplotee('name2',15000)
# se1.displayEmployee()
# se1.displayCount()
#
# def kanchai(name,age,gender):
#     print u'%s,%s岁,%s,上山砍柴'%(name,age,gender)
#
# def qudongbei(name,age,gender):
#     print u'%s,%s岁,%s,开车去东北'%(name,age,gender)
#
# def dabaojian(name,age,gender):
#     print u'%s,%s岁,%s,最爱大保健'%(name,age,gender)
#
# kanchai(u'小明',10,u'男')
# qudongbei(u'小明',10,u'男')
# dabaojian(u'小明',10,u'男')
#
# kanchai(u'老李',90,u'男')
# qudongbei(u'老李',90,u'男')
# dabaojian(u'老李',90,u'男')
#
# class Faa:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def kanchai(self):
#         print u'%s,%s岁,%s,上山砍柴'%(self.name,self.age,self.gender)
#
#     def qudongbei(self):
#         print u'%s,%s岁,%s,开车去东北'%(self.name,self.age,self.gender)
#
#     def dabaojian(self):
#         print u'%s,%s岁,%s,最爱大保健'%(self.name,self.age,self.gender)
#
#
# xiaoming = Faa(u'小明',10,u'男')
# xiaoming.age=20
# xiaoming.dabaojian()
# xiaoming.qudongbei()
# xiaoming.kanchai()
#
# laoli = Faa(u'老李',10,u'男')
# laoli.dabaojian()
# laoli.kanchai()
# laoli.qudongbei()
#
# class Person:
#
#     def __init__(self,name,six,age,power):
#         self.name = name
#         self.six = six
#         self.age = age
#         self.power = power
#
#     def caocong(self):
#         '''
#         草丛战斗，消耗200战斗力
#         :return:
#         '''
#         self.power -= 200
#         print u'已完成草丛战斗，消耗200战斗力'
#
#     def xiulian(self):
#         '''
#         自我修炼，增长100战斗力
#         :return:
#         '''
#         self.power += 100
#         print u'已完成自我修炼，增长100战斗力'
#
#     def duor(self):
#         '''
#         多人游戏，消耗500战斗力
#         :return:
#         '''
#         self.power -= 500
#         print u'已完成多人游戏，消耗500战斗力'
#
#     def detail(self):
#         '''
#         当前对象的详细情况
#         :return:
#         '''
#         temp = u"姓名：%s；性别：%s；年龄：%s；战斗力：%s"%(self.name,self.six,
#         self.age,self.power)
#         print u'当前对象的详细情况：\n',temp
# print '-'*40
# again = Person('苍井井','女',18,1000)
# again.caocong()
# again.detail()
# again.duor()
# again.detail()
# again.xiulian()
# again.detail()
# again.xiulian()
# again.detail()
# print '-'*40
# again1 = Person('东尼木木','男',20,1800)
# again1.caocong()
# again1.detail()
# again1.duor()
# again1.detail()
# again1.xiulian()
# again1.detail()
# print '-'*40
# again2 = Person('波多多','女',19,2500)
# again2.caocong()
# again2.detail()
# again2.duor()
# again2.detail()
# again2.xiulian()
# again2.detail()

# class Foo:
#     def __init__(self,name):
#         self.name = name
#
#     def ord_func(self):
#         '''
#         定义普通方法，至少有一个self参数
#         :return:
#         '''
#         print u'普通方法，name：',self.name
#
#     @classmethod
#     def class_func(cls,ahe):
#         '''
#         定义类方法，至少有一个cls参数
#         :param ahe:
#         :return:
#         '''
#         print u'类方法，ahe:',ahe
#
#     @staticmethod
#     def static_func():
#         '''
#         定义静态方法，无默认参数
#         :return:
#         '''
#         print u'静态方法'
#
#     # def function(name):
#     #     print 'kk'
#     @property
#     def prop(self):
#         return u'普通方法/属性'
#
#     @prop.setter
#     def prop(self,value,key):
#         print '@prop.setter:'
#         print 'value:',value,'key:',key
#
#     # @prop.fget
#     # def prop(self):
#     #     print '@prop.fget'
#
#
#     @prop.deleter
#     def prop(self):
#         print '@prop.deleter'
#
#     # @prop.fdel
#     # def prop(self):
#     #     print '@prop.fdel'
#
#
#
#
#
# f = Foo('lin')
# f.ord_func()
# f.class_func('k')
# f.static_func()
# Foo.static_func()
# Foo.class_func('o')
# print f.prop
# f.prop = 12,67
# print f.prop
# del f.prop

# class lin:
#     '''
#     lin的文档
#     '''
#     emp = 0
#
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         lin.emp += 1
#         self.age = 100
#
#     def disCount(self):
#         print u'直接输出静态字段：',lin.emp
#         print 'age:',self.age
#
#     def disemp(self):
#         print u'输出name:',self.name,u'salay:',self.salary
#         name = 'xiaolin'
#         print u'局部变量',name
#
#     def disage(self):
#         print u'实例变量：',self.age
#         for i in xrange(10):
#             self.age += i
#             lin.emp += i
#         print u'循环后的实例变量：',self.age
#         print u'静态字段：',lin.emp
#     @classmethod
#     def up(cls,a):
#         print cls,cls.__name__
#         return a+1

# p = lin('alpha',12)
# print lin.up(1)
# print p.up(20)

# r = lin('cc',12)
# print r.name
# r.disemp()
# t = lin('kk',10)
# print u't.emp内存地址：',id(t.emp),'t.emp=',t.emp
# print u'lin.emp内存地址：',id(lin.emp),'lin.emp=',lin.emp
# t.emp = 10
# print u'通过实例后对象改变emp的值后'
# print u't.emp内存地址：',id(t.emp),'t.emp=',t.emp
# print u'lin.emp内存地址：',id(lin.emp),'lin.emp=',lin.emp



# lin3 = lin('lin',12)
# print lin3.age,';',lin3.emp
# lin3.disage()
# lin3.disCount()
# print lin3.age,';',lin3.emp
# lin1 = lin('sr',1000)
# lin1.disCount()
# lin1.disemp()
# lin1.salary=2000
# print lin1.salary
# lin1.disemp()
# lin1.age = 21
# print lin1.age
# del lin1.salary
# # print lin1.salary
# lin2 = lin('we',234)
# # print lin2.age
#
# if hasattr(lin1,'name'):
#     print True
# else:
#     print False
#
# try:
#     a = getattr(lin1,'name')
#     print u'name的属性值：',a
# except Exception,e:
#     print e
# setattr(lin1,'tel','123')
# try:
#     s = getattr(lin1,'tel')
#     print u'添加的tel的值：',s
# except Exception.e:
#     print e
#
# try:
#     delattr(lin1,'tel')
# except Exception,e:
#     print e
# else:
#     if hasattr(lin1,'tel'):
#         print u'属性tel存在'
#     else:
#         print u'属性tel不存在'

# print lin.__dict__
# print lin.__doc__
# print lin.__name__
# print lin.__module__
# print lin.__bases__

# class employee(object):
#     city = 'BJ'
#
#     def __init__(self,name):
#         self.name = name
#
#     @classmethod
#     def getCity(cls):
#         return cls.city
#
#     @classmethod
#     def setCity(cls,city):
#         cls.city = city
#
#     def set_City(self,city):
#         employee.city = city
#
# emp = employee('joy')
#
# print u'通过实例对象引用类方法：',emp.getCity()
# print u'通过类对象引用类方法：',employee.getCity()
#
# emp.setCity('ty')
# print u'实例对象调用类方法改变类属性的值'
# print emp.getCity()
# print employee.getCity()
# employee.setCity('cd')
# print u'类对象调用类方法改变类属性的值'
# print emp.getCity()
# print employee.getCity()
#
# emp.set_City('SH')
# print u'调用实例方法改变类属性的值'
# print emp.getCity()
# print employee.getCity()
#
# employee.city=20
# print u'直接修改类属性的值'
# print emp.getCity()
# print employee.getCity()

# class Person(object):
#     __secretCount = 0
#     id = 12
#     def __init__(self,name):
#         self.name = name
#         self.__inName = 'abs'
#
#     def visit_private_aattribute(self):
#         self.__secretCount += 1
#         print '__secretCount:',self.__secretCount
#         print u'__inName:',self.__inName
#
#     def __setId(self,id):
#         Person.id = id*2
#         print Person.id
#
#     def getId(self):
#         self.__setId(2)
#         return Person.id
#
#
# p = Person('lin')
# print p.getId()
# print u'类外部调用私有方法：'
# p._Person__setId(10)
# print p.getId()

# p.visit_private_aattribute()
# print u'在类外直接通过实例访问私有属性'
# print p._Person__inName
# print p._Person__secretCount

# class Animal:
#     def eat(self):
#         print u'%s吃'%self.name
#
#     def drink(self):
#         print u'%s喝'%self.name
#
#     def shit(self):
#         print u'%s拉'%self.name
#
#     def pee(self):
#         print u'%s撒'%self.name
#
# class Cat(Animal):
#     def __init__(self,name):
#         self.name = name
#         self.breed = u'猫'
#
#     def crt(self):
#         print u'喵喵叫'
#
# class Dog(Animal):
#     def __init__(self,name):
#         self.name = name
#         self.breed = u'狗'
#
#     def crt(self):
#         print u'汪汪叫'
#
# c1 = Cat(u'小白家的小黑猫')
# c1.eat()
#
# c2 = Cat(u'小黑家的小白猫')
# c2.drink()
# c2.crt()
#
# d1 = Dog(u'胖子家的小瘦狗')
# d1.eat()
# d1.crt()

# class Parent(object):
#     parentAttr = 100
#     def __init__(self):
#         print 'Call parent constructor'
#
#     def parentMethod(self):
#         print 'Calling parent method'
#
#     def setAttr(self,attr):
#         Parent.parentAttr = attr
#
#     def getAttr(self):
#         print 'Parent attribute:',Parent.parentAttr
#
# class Chlid1(Parent):
#     def __init__(self):
#         print 'Calling child1 constructor'
#
#     def childMethod(self):
#         print 'Calling child1 method'
#         Parent.parentMethod(self)
#         self.getAttr()
#
# class Chlid2(Parent):
#     def chlidMenthod(self):
#         print 'Calling child2 method'
#         self.parentMethod()
#
# c1 = Chlid1()
# c2 = Chlid2()
# print 'c1.childMethod():'
# c1.childMethod()
# print 'c2.chlidMenthod():'
# c2.chlidMenthod()
# print 'c1.parentMethod():'
# c1.parentMethod()
# print 'c1.setAttr(200):'
# c1.setAttr(200)
# print 'c1.getAttr():'
# c1.getAttr()
# print 'c2.setAttr(1):'
# c2.setAttr(1)
# c2.getAttr()
# print 'c2.parentMethod():'
# c2.parentMethod()

# class A(object):
#     name = ''
#     def __init__(self,age):
#         self.name = 'fosterwu'
#         self.age = age
#
#     def getName(self):
#         print 'A'+self.name
#
#     def getAge(self):
#         print self.age
#
# class B(A):
#     def __init__(self,six):
#         self.six = six
#         super(B,self).__init__(age=12)
#
#
#     def getB(self):
#         print self.six
#
# if __name__=='__main__':
#     c = B('lin')
#     c.getName()
#     c.getB()
#     c.getAge()

# class UniverityMember(object):
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def getName(self):
#         return self.name
#
#     def getAttr(self):
#         return self.age
#
# class  Student(UniverityMember):
#     def __init__(self,name,age,sno,Department):
#         UniverityMember.__init__(self,name,age)
#         self.sno = sno
#         self.Dapartment = Department
#
#     def getSno(self):
#         return self.sno
#
#     def getDepartment(self):
#         return self.Dapartment
#
# s = Student('name1','12','cs',18)
# print s.name,s.age
# print s.getAttr()
# print s.getName()
# s.name = 'name2'
# s.age = 14
# print s.getAttr()
# print s.getName()
# print s.name,s.age
# u = UniverityMember('dd',12)
#
# if issubclass(Student,UniverityMember):
#     print True
# else:
#     print False
#
# if isinstance(s,UniverityMember):
#     print True
# else:
#     print False
#
# if isinstance(u,Student):
#     print True
# else:
#     print False


# class D:
#     def bar(self):
#         print 'D.bar'
#
# class C(D):
#     def bar(self):
#         print 'C.bar'
#
# class B(D):
#     def bar1(self):
#         print 'B.bar'
#
# class A(B,C):
#     def bar1(self):
#         print 'A.bar'
#
# a = A()
# a.bar()

# class D(object):
#     def bar(self):
#         print 'D.bar'
#
# class C(D):
#     def bar(self):
#         print 'C.bar'
#
# class B(D):
#     def bar1(self):
#         print 'B.bar'
#
# class A(B,C):
#     def bar1(self):
#         print 'A.bar'
#
# a = A()
# a.bar()

# class house(object):
#     # def __init__(self,name):
#     #     print u"house类"
#     def getHeigh(self):
#         print u'调用house类的方法'
#
# class car(object):
#     # def __init__(self):
#     #     print u'car类'
#     def getHeight(self):
#         print U'调用car类的方法'
#
#
# class carHouse(house,car):
#     def __init__(self):
#         print u'carhouse继承house和car,没有__init__构造方法'
#     def carHeight(self):
#         car.getHeight(self)
#
# class busHouse(house,car):
#     def __init__(self):
#         car.__init__(self)
#         print u'bushouse调用car类的构造方法'
#
# c = carHouse()
# # b = busHouse()
# c.carHeight()

# class Animal(object):
#     def __init__(self,name):
#         print u'Animal类'
#         self.Name = name
#         print u'sefl.Name的值：',self.Name
#
#     def accessibleMethod(self):
#         print u'accessibleMethod方法'
#         print 'I have a self current name is:'
#         print self.Name
#         print 'the secret message is:'
#         self.__inaccessible()
#
#     def __inaccessible(self):
#         print 'U cannot see me....'
#
#     @staticmethod
#     def staticMentod():
#         print u'静态方法'
#
#     def setName(self,name):
#         print u'访问器函数setName'
#         self.Name = name
#
#     def getName(self):
#         print u'访问器函数getName'
#         return  self.Name
#
# a = Animal('learns')
# print a.getName()
# a.setName('sr')
# print 'new name:',a.getName()
# a.staticMentod()
# a._Animal__inaccessible()

# class Person(object):
#     def __init__(self,name):
#         self.Name = name
#
#     def getName(self):
#         print u'getName方法'
#         return self.Name
#
#     def setName(self,name):
#         print u'setName方法'
#         self.Name = name
#
#     def delName(self):
#         print u'delName方法'
#         del self.Name
#
#     name = property(getName,setName,delName,'name property docs')
#     # name = property(getName,setName)
#     # name = property(setName,delName)
#
# bob = Person('Bob Smith')
# print bob.name
# bob.name = 'name1'
# print bob.name
# del bob.name
# print bob.getName
#
#
# fof = Person('Bob Smith')
# print fof.name

# class Student():
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def set_score(self,score):
#         print u'set_score方法'
#         if not isinstance(score,int):
#             raise ValueError("score must be an interger!")
#         if score < 0 or score > 100:
#             raise ValueError("score must be between 0 -100")
#     def get_score(self):
#         print u'get_score方法'
#         return self.score
#
# s = Student('tom',19,90)
# print 'score is ',s.get_score()
# try:
#     s.set_score(999)
# except Exception,e:
#     print 'score eroor!',e
# try:
#     s.set_score('33')
# except Exception,e:
#     print 'score eroor!',e

# print s.name,s.age,s.score
# s.name = 'lily'
# s.score = 9999
# print s.name,s.age,s.score
# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self,value):
#         self._birth = datetime.strptime(value,'%Y-%m-%d')
#         print self._birth
#
#     @property
#     def age(self):
#         cueewntTime = datetime.now()
#         cueewntDate = cueewntTime.strftime('%Y-%m-%d')
#         print cueewntDate
#         print self._birth
#         timedelta = datetime.strptime(cueewntDate,'%Y-%m-%d')-self._birth
#         print timedelta
#         return timedelta.days/365
#
# if __name__=='__main__':
#     s = Student()
#     s.birth = '1992-08-18'
#     print u'现在的年龄：',s.age

# class F1:
#     pass
#
# class S1(F1):
#     def show(self):
#         print 'S1.show'
#
# class S2(F1):
#     def show(self):
#         print 'S2.show'
#
# def Func(obj):
#     obj.show()
#
# s1_obj = S1()
# Func(s1_obj)
# s2_obj = S2()
# Func(s2_obj)

# class calculator:
#
#     def count(self,args):
#         return 1
#
# calc = calculator()
#
# from random import choice
#
# obj = choice(['hello,world',[1,2,3],calc])
# print obj
# print type(obj)
# print obj.count('a')

# class Duck(object):
#     def quack(self):
#         print 'Quaaaaaack!'
#
#     def feathers(self):
#         print 'The duck has white and gray feathers.'
#
# class Person(object):
#     def quack(self):
#         print 'The person imitates a duck.'
#
#     def feathers(self):
#         print 'The person takes a feather from the ground and show it.'
#
# def in_the_forest(duck):
#     duck.quack()
#     duck.feathers()
#
# def game():
#     donald = Duck()
#     john = Person()
#     # in_the_forest(donald)
#     in_the_forest(john)
#
# game()

# def add(x,y):
#     return x+y
#
# print add(1,2)
# print add('hello','world')
# print add(1,'abc')

# class Parent(object):
#     def myMethod(self):
#         print 'call Parent'
#
#     def printName(self):
#         print 'my name is LiLY'
#
# class Child(Parent):
#     def myMethod(self):
#         print 'call Child'
#
# c = Child()
# c.myMethod()
# c.printName()

# class Vector(object):
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector(%d,%d)'%(self.a,self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a,self.b + other.b)
#
# x = Vector(3,7)
# y = Vector(1,-10)
# # print x+y
# print str(x)
# print str(y)

# class Foo:
#     '''
#     描述类信息，这是用于看片的神奇
#     '''
#     def func(self):
#         pass
#
#     def __del__(self):
#         print ' i will be deleted!'
#
#     def __call__(self, *args, **kwargs):
#         print '__call__'
#
# print Foo.__doc__
# f = Foo()
# f()
# class C:
#
#     def __init__(self):
#         self.name = 'gloryroad'
#
# obj = C()
# print obj.__module__
# print obj.__class__

# class Province:
#     country = 'China'
#
#     def __init__(self,name,count):
#         self.name = name
#         self.count = count
#
#     def func(self,*args,**kwargs):
#         print 'func'
#
# print Province.__dict__
#
# obj1 = Province('HeBei',10000)
# print obj1.__dict__
#
# obj2 = Province('HeNan',3888)
# print obj2.__dict__

# class Foo:
#     def __str__(self):
#         return 'gloryroad'
#
# obj = Foo()
# print obj

# class Foo(object):
#     def __getitem__(self,key):
#         print '__getitem__',key
#
#     def __setitem__(self, key, value):
#         print '__setitem__',key,value
#
#     def __delitem__(self, key):
#         print '__delitem__',key
#
#
# obj = Foo()
# result = obj['k1']
# obj['k2'] = 'wupeiqi'
# del obj['k1']
# class Foo(object):
    # def __getslice__(self,i,j):
    #     print '__getslice__',i,j
    #
    # def __setslice__(self, i, j, sequence):
    #     print '__setslice__',i,j
    #
    # def __delslice__(self, i, j):
    #     print '__delslice__',i,j

#     def __init__(self,sq):
#         self.sq = sq
#
#     def __iter__(self):
#         return iter(self.sq)
#
# obj = Foo([11,22,33,44])
# for i in obj:
#     print i


# obj[-1:1]
# obj[0:1] = [11,22,33,44]
# del obj[0:2]

# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'_instance'):
#             orig = super(Singleton,cls)
#             cls._instance = orig.__new__(cls,*args,**kwargs)
#             return cls._instance
#
# class MyClass(Singleton):
#     a = 1
#
# one = MyClass()
# two = MyClass()
#
# two.a = 3
# print one.a
# print id(one)
# import sys
# print id(5001111)
# print sys.getrefcount(9)
# a = 9
# print sys.getrefcount(9)
# b = a
# print sys.getrefcount(a)
# c = [b]
# print sys.getrefcount(9)
# del a
# print sys.getrefcount(9)
# b = 100
# print sys.getrefcount(9)
# c[0] = -1
# print sys.getrefcount(9)

# import time
# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print class_name,u'销毁'
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print id(pt1),id(pt2),id(pt3)
#
# del pt1
# del pt2
# del pt3
# print id(pt1),id(pt2),id(pt3)

# class LeakTest:
#     def __init__(self):
#         self.a = None
#         self.b = None
#         print 'object = %d bom here.'%id(self)
#
# A = LeakTest()
# B = LeakTest()
# A.a = B
# B.b = A
#
# import sys
# print sys.getrefcount(A)
# print sys.getrefcount(B)
#
# del A
# try:
#     print sys.getrefcount(A)
# except Exception,e:
#     print e
#
# del B
# try:
#     print sys.getrefcount(B)
# except Exception,e:
#     print e
# outerVar = 'this is a global varible'
#
# def test0827.txt():
#     innerVar = 'this is a Local variable'
#     print 'lpcal variables:'
#     print locals()
#     print outerVar
#
# test0827.txt()
# print 'global variables:'
# print globals()

# def outer():
#     name = 'python'
#     print 'outer'
#     def inner():
#         print name
#     return inner()
# outer()

# def add(x,y):
#     return x+y
#
# def sub(x,y):
#     return x-y
#
# def apply(func,x,y):
#     return func(x,y)
#
# print apply(add,2,1)
# print apply(sub,2,1)
# import sys
# lista = ['a','b','c']
# print sys.getrefcount(lista)
# listb = lista
# print sys.getrefcount(listb)

import time


# def log(func):
#     def wrapper(*args,**kw):
#         print 'call %s'%func.__name__
#         return func(*args,**kw)
#     return wrapper
#
# @log
# def now():
#     now = time.strftime("%Y-%m-%d %H:%M:%S"
#                          ,time.localtime())
#     print 'current time is %s'%now
#
# now()




# def deco(func):
#     def _deco(*args,**kwargs):
#         print 'before %s called.'%func.__name__
#         ret = func(*args,**kwargs)
#         print 'after %s called.result:%s'%(func.__name__,ret)
#         return ret
#     return _deco
#
# @deco
# def myfunc(a,b):
#     print 'myfunc(%s,%s) called.'%(a,b)
#     return a+b
#
# @deco
# def myfunc2(a,b,c):
#     print 'myfunc2(%s,%s,%s)called.'%(a,b,c)
#     return a+b+c
#
# # myfunc1 = deco(myfunc)
# myfunc(1,2)
# # myfunc1()
# myfunc(3,4)
# myfunc2(1,2,3)
# myfunc2(3,4,5)

# class locker:
#     def __init__(self):
#         print 'locker.__init__()should be not called.'
#
#     @staticmethod
#     def acquire():
#         print u'locker.acquire() called.(只是静态方法）'
#
#     @staticmethod
#     def release():
#         print u'locker.relese()called.(不需要对象实例）'
#
# def deco(cls):
#     def _deco(func):
#         def __deco():
#             print 'before %s called[%s].'%(func.__name__,cls)
#             cls.acquire
#             try:
#                 return func()
#             finally:
#                 print 'finally'
#                 cls.release()
#             # print 'after %s calles [%s].'%(func.__name__,cls)
#         return __deco
#     return _deco
# @deco(locker)
# def myfunc():
#     print 'myfunc() called'
#
# @deco(locker)
# def myfunc2():
#     print 'myfunc2() called.'
#
# # myfunc()
# # myfunc()
# # myfunc2()
#
# class Next(object):
#     List = []
#     name = 'wu'
#     def __init__(self,low,high):
#         for Num in range(low,high):
#             self.List.append(Num **2)
#             self.name = 'x'
#
#     def __call__(self,Nu):
#         return self.List[Nu]
#
# res = Next(1,5)
# print res(0)
# print res(1)
# print res(2)
# print Next.List
# print Next.name
# print res.name


# Python2--有经典类和新式类
# class A(object):
# #     属性---变量
#     count = 12#类属性
# #     方法---函数
#     def func1(self,name):#self为实例，只能用对象调用
#         self.name = name
#         print self.name
#         print A.count
#     def __init__(self,name,age,salry):
#         self.name = name#实例属性
#         self.age = age
#         self.salry = salry
#
#
#
# a1 = A('lin',25,6000)
# print a1.name
# print a1.age
# a1.func1('haha')
# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def sayHi(self):
#         print 'hello,my name is ',self.name
#
# p = Person('Swaroop')
# p.sayHi()

# class Person:
#     population = 0
#
#     def __init__(self,name):
#         self.name = name
#         print 'initializing %s'%self.name
#         Person.population +=1
#
#     def __del__(self):
#         print '%s saysbye.'%self.name
#         Person.population -= 1
#
#         if Person.population == 0:
#             print 'I\'m the lastone.'
#         else:
#             print 'There are still%d people left.'%Person.population
#
#     def sayHi(self):
#         print 'Hi,my name is %s'%self.name
#
#     def howMany(self):
#         if Person.population == 1:
#             print 'I\'m the only person here.'
#         else:
#             print 'We have %d persons here.'%Person.population
#
# swaroop = Person('lin')
# swaroop.sayHi()
# swaroop.howMany()

class SchooMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print 'Initialized SchooMember:%s'%self.name

    def tell(self):
        print 'Name:%s age:%s'%(self.name,self.age)

class Teacher(SchooMember):
    def __init__(self,name,age,salary):
        SchooMember.__init__(self,name,age)
        self.salary = salary
        print 'Initialized Teacher:%s'%self.name

    def tell(self):
        SchooMember.tell(self)
        print 'Salary:%d'%self.salary

class Student(SchooMember):
    def __init__(self,name,age,marks):
        SchooMember.__init__(self,name,age)
        self.marks = marks
        print 'Initialized Student:%s'%self.name

    def tell(self):
        SchooMember.tell(self)
        print 'Marks:%d'%self.marks

t = Teacher('Mrs.Shrividya',40,30000)
s = Student('Swaroop',22,75)

print

members = [t,s]
for member in members:
   member.tell()

























































































































































































































































































