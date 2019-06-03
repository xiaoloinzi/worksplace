# encoding=utf-8
#相当于一个函数，：冒号前面的是函数中的参数，：后面的为表达式
#吧这个lambda这个的值赋给一个变量时，这个变量则为一个方法，调用这个方法并给它
#传参数，然后再返回表达式计算的结果
f = lambda x,y,z:x+y+x
print f(1,2,3)
h = lambda x,y,z:x+y+z
print h(1,2,3)