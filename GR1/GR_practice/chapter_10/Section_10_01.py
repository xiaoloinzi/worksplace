# encoding=utf-8
# 1、实现任意自定义类


# 2 、实现@property 方法


# 3、实现单继承类


# 4、实现多继承类


# 5、实现同时具备类方法、静态方法和实例子方法的一个类


# 6、删除无重复元组中给定的元素，返回新元组


# 8、实现栈类


# 9、实现队列类


# 10、实现任意2种自定义的不同类型适配器


# 1、 类和对象的概念和关系是什么？
# 类：用来描述具有相同属性和方法的对象的集合，它定义了该集合中
# 每个对象所共有的属性和方法，对象是类的实例
#
# 对象：通过类定义的数据结构实例，对象包括两个数据成员（类变量和实例变量）和方法

# 2、 什么样的代码才是面向对象？
# 代码中有创建对象，并通过对象执行方法


# 3、 类的构造方法与成员方法之间有什么区别？
# 每次从类产生实例时，Python都会自动调用构造方法，进行数据初始化
# 创建类的实例后，要通过类的实例进行调用成员方法



# 4、 self关键词的作用是什么？
# 代表实例本身



# 5、 类的构造方法和成员方法之间的区别？
# 创建类的对象时，已经调用构造方法
# 成员方法还需要对象进行调用


# 6、 说出类方法和静态方法的区别？ 分别实现一个类方法和静态方法
# 实例
# 类方法隐含传递的参数是类本身cls，而静态方法无隐含参数

# class lin:
#     age =1
#     def __init__(self,name):
#         self.name = name
#
#     @classmethod
#     def class_func(cls,age):
#         print u'类方法'
#         cls.age=age
#         return cls.age
#
#     @staticmethod
#     def static_func():
#         print u'静态方法'
#
# if __name__=="__main__":
#     f = lin
#     print f.class_func(23)
#     f.static_func()





# 7、 什么是数据封装与隐藏？
# 将对象的数据与操作数据的方法相结合，通过方法将对象的数据与实现细节保护起来，称为封装，
# 外界只能通过对象的方法访问对象，因此封装同时也实现了对象的数据隐藏



# 8、 什么是方法重写， 方法重写的规则是什么？
# 重写是指子类重写父类的成员方法。子类可以改变父类方法所实现的功能，
# 但子类中重写的方法必须与父类中对应的方法具有相同的方法名。也就是说
# 要实现重写，就必须存在继承。
# 简单来讲，就是如果父类的方法不能满足子类的需求，子类就可以重写从父
# 类那继承过来的方法。


# 9、 编写程序片段， 定义表示课程的类Course。
# 课程的属性包括课程名、 编号、 选修课号； 方法
# 包括设置课程名、 设置编号、 设置选修课号以及获取课程名、
# 获取编号、 获取选修课程号， 然后打印输出该对
# 象的课程名、 编号以及选修课号。



# 10、 实现一个多重继承类， 并访问该类

# class Myname(object):
#     def __init__(self):
#         print u'第一个父类'
#
#
# class Myage(object):
#     def __init__(self):
#         print u'第二个父类'
#
#
# class child(Myage,Myname):
#     def Myhands(self):
#         print u'我自己'
#
# s = child()
# s.Myhands()




# 11、请编写一个decorator
# 要求：
# 在函数调用前后打印出'begin call'， 函数执行结束后
# 打印'end call'的字样的日志
# 写出的@log的decorator， 使它既能支持无参数的decorator：
# @log
# def f():
# pass
# 又支持有参数的decorator：
# @log('execute')
# def f():
# pass




# 12、 在不运行情况下给出下面程序执行结果
# #coding=utf-8
# class Parent(object):
# x = 1
# class Child1(Parent):
# pass
# class Child2(Parent):
# pass
# print Parent.x, Child1.x, Child2.x #给出结果
# print id(Parent.x), id(Child1.x), id(Child2.x) #不需要给结果， 只说是否一致
# Child1.x = 2
# print Parent.x, Child1.x, Child2.x #给出结果
# print id(Parent.x), id(Child1.x), id(Child2.x)#不需要给结果， 只说是否一致
# Parent.x = 3
# print Parent.x, Child1.x, Child2.x #给出结果
# print id(Parent.x), id(Child1.x), id(Child2.x)#不需要给结果， 只说是否一致




# 13、 在不运行情况下给出下面程序执行的结果， 并说明为什么？
# classParson(object) :
# def __init__(self, name, f1, f2 = 1) :
# self.name = name
# self.f1 = f1
# self.f2 = f2
# self.__inName = 'jack'
# def f1(self, a) :
# print f1, self.a
# @staticmethod
# def f2(b) :
# print b
# p1 = Parson('joy', 100, 200)
# #print p1.__dict__, p1
# p1.f1(2)
# p1.f2(5)








# 14、 按如下规律打印列表
# 1 ['1*', '2', '3', '4', '5']
# 2 ['1', '2*', '3', '4', '5']
# 3 ['1', '2', '3*', '4', '5']
# 4 ['2', '3', '4*', '5', '6']
# 5 ['3', '4', '5*', '6', '7']
# 6 ['4', '5', '6*', '7', '8']
# ...
# 20 [16, 17, 18, 19, 20*]

# print [eval("'20'+'\*'"),23]






# 15、 写一个函数, 将驼峰命名法字符串转成下划线命名字符串，
#  如GetItem -> get_item， getItem -> get_item。



# 16、 给定一些NxN的矩阵， 对于任意的路线， 定义其【 和】
# 为其线路上所有节点的数字的和， 计算从左上角到右下角的路线和
# 最小值。 每条路线只能从某一点到其周围（ 上下左右） 的点，
# 不可斜行。 例如：
# 4,6
# 2,8 的路线和最小值为 4-2-8 14
# 1,2,3
# 4,5,6
# 7,8,9 的路线和最小值为 1-2-3-6-9 21


# 17、 有两个序列a,b， 大小都为n,序列元素的值任意整形数，
# 无序； 要求：通过交换a,b中的元素， 使[序列a元素的和]与
# [序列b元素的和]之间的差最小。















