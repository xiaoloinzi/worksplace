# encoding=utf-8
#并没显式的读取文件，而是利用迭代器每次读取下一行。
for i in open('test1.txt'):
    print i
# 生成器函数在Python中与迭代器协议的概念联系在一起。
# 简而言之，包含yield语句的函数会被特地编译成生成器。
# 当函数被调用时，他们返回一个生成器对象，这个对象支持迭代器接口。
# 函数也许会有个return语句，但它的作用是用来yield产生值的。
# 不像一般的函数会生成值后退出，生成器函数在生成值后会自动挂起并暂停他们的执行和状态，
# 他的本地变量将保存状态信息，这些信息在函数恢复时将再度有效
def g(n):
    for i in range(n):
        yield i**2
for i in g(5):
    print i,':',
t = g(5)
for i in range(5):
    print '\n',t.next(),
# 在运行完5次next之后，生成器抛出了一个StopIteration异常，迭代终止。
# 再来看一个yield的例子，用生成器生成一个Fibonacci数列：
def fab(max):
    a,b = 0,1
    while a< max:
        yield a
        a,b = b,b+a
for i in fab(20):
    print i ,','