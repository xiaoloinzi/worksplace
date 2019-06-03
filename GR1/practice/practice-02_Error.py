# encoding=utf-8
from __future__ import division

a = 12
print u"a变量的内存地址：", id(a)
#修改a变量的值
a = 23
print u"修改a变量的值后的内存地址：", id(a)
a = 'hello'
print u'a=hello是字符串的地址',id(a)
a = 'world'
print u'a=world是字符串的地址',id(a)
try:
    for i in range(3):
        for j in range(3):
            if i == 1:
                break
            print i,j
except:
    print 'stop'

try:
    file("hello.txt", "r")#如果文件不存在，引发异常
    print "读文件"
except IOError: #捕获IO异常
    print "文件不存在"
except:#其他异常
    print "程序异常"

#try...finally的使用方法
#try...except后还可以添加一个finally子句。无论异常是否发生，finally子句都会被执行。所有的finally子句通常用于关闭因异常而不能释放的系统资源。
try:
    f = open("test1.txt", "r")
    try:
        print f.read(5)
    except:
        print "读文件异常"
    finally:
        print "释放资源"
        f.close()
except IOError:
    print "文件不存在"
#使用raise抛出异常
#当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行。
#演示raise用法
try:
    s = None
    if s is None:
        print "s 是空对象"
        raise NameError#如果引发NameError异常，后面的代码将不能执行
    print len(s)
except TypeError:
    print "空对象没有长度"

#自定义异常
#python允许程序员自定义异常，用于描述python中没有涉及的异常情况，自定义异常必须继承Exception类，
# 自定义异常按照命名规范以"Error"结尾，显示地告诉程序员这是异常。自定义异常使用raise语句引发，而且只能通过人工方式触发。

class DivisionException(Exception):
    def __init__(self, x, y):
        Exception.__init__ (self, x, y)#调用基类的__init__进行初始化
        self.x = x
        self.y = y

if __name__ == "__main__":
    try:
        x = 3
        y = 2
        if x % y > 0:
    #如果大于0， 则不能被初始化，抛出异常
            print x/y
            raise DivisionException(x, y)
    except DivisionException,div:#div 表示DivisionException的实例对象
            print "DivisionExcetion: x/y = %.2f" % (div.x/div.y)

#assert语句的使用
#assert语句用于检测某个条件表达式是否为真。assert语句又称为断言语句，即assert认为检测的表达式永远为真，if语句中的条件判断都可以使用assert语句检测。





