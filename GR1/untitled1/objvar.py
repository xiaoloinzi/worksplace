#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/8 10:58
# @Author  : Lin
# @Site    : 
# @File    : objvar.py
# @Software: PyCharm
class Person:
    '''Represents a person'''
    population = 0
    def __init__(self,name):
        '''Initializes the person's data.'''
        self.name = name
        print'(Initializing %s)'%self.name
        #when this person is created ,he/she
        #adds to the population
        Person.population += 1
    def __del__(self):
#         还有一个特殊的方法__del__，它在对象消逝的时候被调用。对象消逝即
# 对象不再被使用，它所占用的内存将返回给系统作它用。在这个方法里面，我们只是简单地
# 把Person.population减1
        '''I am dying.'''
        print'%s says bye.'%self.name
        Person.population -= 1
        if Person.population == 0:
            print 'I am the last one'
        else:
            print 'There are still %d people left.'%Person.population
    def sayHi(self):
        '''Greeting by the person.
        Really ,that all it does'''
        print 'Hi,my name is %s'%self.name
    def howMany(self):
        '''Prints the current population'''
        if Person.population == 1:
            print 'I am the only person here'
        else:
            print 'We have %d person here.'%Person.population

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()
del swaroop#当对象不再被使用时，__del__方法运行，但是很难保证这个方法究竟在 什么时候 运行。如果你想要指
# 明它的运行，你就得使用del语句，就如同我们在以前的例子中使用的那样
#不做这个操作，则kalam的值先被弃用
swaroop.sayHi()
swaroop.howMany()