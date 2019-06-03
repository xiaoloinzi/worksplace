# encoding=utf-8
'''
兔子在出生两个月后就可以生新的兔子，一对兔子一个月能生出一堆兔
子，如果所有的兔子都不死，一年以后可以繁殖多少对兔子

'''

def tuzi(n):
    f0 = 1
    f1 = 1
    list1 = [1,1]
    for i in xrange(n):
        f2 = f0 + f1
        f0 = f1
        f1 = f2
        list1.append(f2)
    return list1
if __name__=='__main__':
    print tuzi(10)



















