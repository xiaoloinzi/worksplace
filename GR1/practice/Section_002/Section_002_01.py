# # encoding=utf-8
# import time
# def printme(str):
#     '''
#     打印传入的字符串到标准显示设备上
#     :param str: 传入的字符串
#     :return:none
#     '''
#     print time.time(),':',str
#     return
#
# print printme(u'周末快乐')
#
# #无参参数
# def SayHello():
#     '''
#
#     :return:none
#     '''
#     print 'Hello World!'# block belonging to the function
#
# print SayHello()
#
#
# #传递指定个必备参数
# def info(name,age,tel):
#     print 'name:',name,',age:',age,',tel:',tel
#     print 'name:'+name+',age:'+str(age)+',tel:'+tel
#
# print info('lin',25,'18824133049')

# #传不可变对象
# def ChangeNum(num):
#     #global num
#     num +=1
#     print u'自定义函数中的num =',num
#
# #定义变量num，赋初始值为10
# num = 10
# ChangeNum(num)
# print u'函数调用后Num = ',num
#
# def ChengeList(list1):
#     list1.append('newStr')
#     print u'函数中的list1',list1
#
# #定义list1
# list2 = [1,2,3]
# print u'调用函数前的list1：',list2
# ChengeList(list2)
# print u'调用函数后的list1：',list2


# #传可变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end([1,2,3])
print add_end(['x','y','z'])
print add_end()
print add_end()
print add_end()

# #函数应该坚持参数的类型
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-1)
print my_abs('x')

# #有参数函数，命名参数
#
def sum(a,b,c):
    return a*100+b*10+c

print sum(3,c=1,b=2)

def say(message,times = 1):
    print message * times

say('gloryroad!')
say(u'万岁！', 3)



























