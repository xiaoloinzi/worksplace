#encoding=utf-8
#函数取得的参数是你提供给函数的值，这样的函数就可以利用这些值，做一些事情，这些参数就像变量一样
#只不过它们的值是在我们调用0函数的时候定义的，而非在函数本身内赋值
#参数在函数定义的圆括号对内定义，用逗号分割，当我们调用函数的时候，我们以同样的方式取值，注意我们使用过的术语，函数中的参数名称为形参，二你提供给函数调用的值称为实参
def printMax(a,b):
    if a > b:
        print("%d is maximum"%a)
    elif a == b:
        print("%d 和 %d 相等"%(b,a))
    else:
        print("%d is maximum"%b)
print(printMax(3,4))
x = 2
y = 2
printMax(y,x)
# 这里，我们定义了一个称为printMax的函数，这个函数需要两个形参，叫做a和b。我们使
# 用if..else语句找出两者之中较大的一个数，并且打印较大的那个数。
# 在第一个printMax使用中，我们直接把数，即实参，提供给函数。在第二个使用中，我们使用变量调用
# 函数。 printMax(x, y)使实参x的值赋给形参a，实参y的值赋给形参b。在两次调用中，printMax函
# 数的工作完全相同