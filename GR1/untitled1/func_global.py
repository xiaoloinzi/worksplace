#encoding=utf-8
def func():
    global x
    print(" x is ",x)
    x = 2
    print("changed local x to ",x)
x = 50
func()
print("value of x is",x)
# global语句被用来声明x是全局的——因此，当我们在函数内把值赋给x的时候，这个变化也反映在我们
# 在主块中使用x的值的时候。
# 你可以使用同一个global语句指定多个全局变量。例如global x, y, z。