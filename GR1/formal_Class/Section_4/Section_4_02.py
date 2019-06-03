# encoding=utf-8
tup1 = ()
print type(tup1)
tup2 = (123)
tup3 = (123,)#一个元组的一定要加逗号
tup4 = ('abc')
print type(tup2),tup2
print type(tup3),tup3,len(tup3)
print type(tup4),len(tup4)



# 对于如下的元组：
tup1 = ('physics', 'chemistry', 1997, [198,987,27], 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
# 1、访问元组tup1中的数据
# 2、对tup1进行切片操作
# 3、把元组tup1和tup2进行链接组合，形成一个新的元组
# 4、删除元组tup2中的元素或者删除元组

for i in tup1:
    if isinstance(i,list):
        for j in i:
            print j
    else:
        print i
print tup1[::-1]

tup3 = tup1 + tup2
print tup3

# del tup2
# print tup2

# 5、列出你知道的元组支持的运算符
# 6、列出你知道的，元组支持的内置函数
# 7、遍历如下的元组：

tup12 = (1,2,3,4)
tup11 = (5,6,7,8)
print tup11+tup12
print tup11*2
print max(tup11)
print min(tup11)
print len(tup11)
print 5 in tup11
print cmp(tup11,tup12)
print tup11 is tup12
print str(tup11)
print list(tup11)
print tup11 == tup12
zoo = ('wolf', 'elephant', 'penguin')
new_zoo = ('monkey', 'dolphin', zoo)

for s in zoo:
    print s
for n in new_zoo:
    if isinstance(n,tuple):
        for d in n:
            print d
    else:
        print n


# 递归
def printTup(tup):
    for i in tup:
        if isinstance(i,tuple):
            printTup(i)
        else:
            print i

tup01 = ('physics', 'chemistry', 1997,[198,987,27], 2000)
# 对第4个元素，修改成[198,987,27,123,12]，
# 为何元组不能修改，但是里面的列表可以修改

tup01[3].extend([123,12])#内存地址没有改变，可以对元组进行更改
print tup01
























