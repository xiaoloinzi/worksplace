# encoding=utf-8

int1 = int(raw_input(u'请输入月份：'))
def TuZi(n):
    f2 = 1
    f1 = 1
    sum = 0
    for i in range(3,n+1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f3
s = TuZi(int1)
print int1,u'个月有%d兔子'%s