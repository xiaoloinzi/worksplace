# encoding=utf-8
#2、创建一个类，在类中使用__a定义一个属性，
# 针对这个类，创建一个对象，对象给属性__a赋值为1。
# class class_a:
#     def __init__(self):
#         #self.xx定义属性
#         self.__a = None#以双下划线开头的表示类的私有成员（ __foo） ；
# b = class_a()
# print b.__a = 1#私有属性不能访问
class TestClass:
    def __init__(self):
        self.atrr = 1
        self.__a = 2

b = TestClass()
print b.atrr



