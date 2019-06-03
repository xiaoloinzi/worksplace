# encoding=utf-8
__all__=['bar','baz','add']
waz = 5
bar = 10
print u'这是test模块'
def print_func(par):
    newStr = 'Hello :',par
    return newStr

def add(x,y,*args):
    sum = x+y
    if len(args)>0:
        for i in args:
            sum += i
    return sum

def sub(x,y,*args):
    result = x-y
    if len(args)>0:
        for i in args:
            result -= i
    return result
def baz():
    return 'baz'

