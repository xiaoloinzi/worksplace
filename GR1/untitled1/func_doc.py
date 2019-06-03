#encoding=utf-8
def printMax(x,y):
    '''prints the maximum of two numbers,
    The two values must be integers.'''
    x = int(x)#convert to intrgers if possible
    y = int(y)
    if x > y:
        print(x,"is maximum")
    else:
        print(y,"is maximum")
printMax(2,3)
print(printMax.__doc__)
# 在函数的第一个逻辑行的字符串是这个函数的 文档字符串 。注意，DocStrings也适用于模块和类，我们会
# 在后面相应的章节学习它们。
# 文档字符串的惯例是一个多行字符串，它的首行以大写字母开始，句号结尾。第二行是空行，从第三行开
# 始是详细的描述。 强烈建议 你在你的函数中使用文档字符串时遵循这个惯例