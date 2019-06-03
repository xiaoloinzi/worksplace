#encoding=utf-8
#return 语句用来从一个函数返回。即跳出函数，我们也可以选从函数返回一个值
def maximum(x,y):
    if x > y:
        return x
    else:
        return y
print(maximum(9,3))
#maximum 函数返回参数中的最大值，在这里是提供给函数的数，它使用简单的if。。。else语句来找出较大的值，然后返回那个值
#注意，没有返回值的return语句等价于return None，None是python中表示没有任何东西的特殊类。例如，如果一个变量的值为None，可以表示它没有值
#除非你提供你自己的return语句，每个函数都在尾部暗含有return，None语句，通过运行print someFunction，你可以明白这一点，函数someFunction没有使用return语句
#如同：
# def someFunction()：
# pass