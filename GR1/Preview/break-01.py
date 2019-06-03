# encoding=utf-8
#break语句用来终止循环语句，即循环条件没有false条件或者序列还没完全递归完
#也会被停止执行循环语句，break语句用在while或for中，记住是跳出循环，如果是嵌套循环，break会停止执行最深的循环，并开始执行下一行代码
for letter in 'Python':
    if letter == 'h':
        break
    print 'Current Letter:',letter

var = 10
while var > 0:
    print 'current variable value:',var
    var = var -1
    if var == 5:
        break
print u'结束'
