# encoding=utf-8

def func(n,a,b,c):
    if n == 1:
        print a,'->',c
    else:
        func(n-1,a,c,b)
        func(1,a,b,c)
        func(n-1,b,a,c)
def func2(n,a,b,c):
    for i in xrange(n-1):
        print a,'->',b
    print a,'->',c
    for i in xrange(n-1):
        print b,'->',c

if __name__=="__main__":
    n = int(raw_input("请输入层数："))
    func(n,'a','b','c')


# 习题：假定这个条件没有，写一个函数，完成汉诺塔问题求解
















