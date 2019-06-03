#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/8 11:34
# @Author  : Lin
# @Site    : 
# @File    : inherit.py
# @Software: PyCharm
class SchoolMenber:
    '''Represents any school member.'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)'% self.name
    def tell(self):
        '''Tell my datails.'''
        print 'Name :%s Age:%s' % (self.name,self.age)
class Teacher(SchoolMenber):
    '''Represents  teacher.'''
    def __init__(self,name,age,salary):
        SchoolMenber.__init__(self,name,age)
        self.salary = salary
        print '(Initialized Teacher :%s)'%self.name
    def tell(self):
        SchoolMenber.tell(self)
        print 'Salary:"%d"'%self.salary
class Student(SchoolMenber):
    def __init__(self,name,age,marks):
        SchoolMenber.__init__(self,name,age)
        self.marks = marks
        print '(Initialized Student:%s)'%self.name
    def tell(self):
        SchoolMenber.tell(self)
        print 'Marks:"%d"'%self.marks
t = Teacher('Mrs.Shrividya',40,30000)
s = Student('Swaroop',22,75)
print #prints a blank line

members = [t,s]
for member in members:
    member.tell()#works for both Teacher and Students
