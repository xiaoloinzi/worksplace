# encoding=utf-8
for letter in 'Python':
    print '当前的字母',letter

fruits = ['banana','apple','mange']
for fruit in fruits:
    print '当前的水果',fruit
print '通过索引的方式遍历列表的数据'
for index in range(len(fruits)):
    print '当前水果',fruits[index]
print range(10)
for i in range(10):
    print i

#for .....else表示正有的意思：for语句和普通没有任何区别，else会在for语句循环正常执行完的情况下执行（即for不是通过break跳出二中断的）while...else也是一样
print '\nif中以continue结束跳出'
for num in range(10,20):
    for i in range(2,num):
        if num % i == 0:
            j = num / i
            print '%d 等于 %d * %d'%(num,i,j)
            continue
    else:
        print num,'是一个质数'
print '\nif中以break结束跳出'
for num in range(10,20):
    for i in range(2,num):
        if num % i == 0:
            j = num / i
            print '%d 等于 %d * %d'%(num,i,j)
            break
    else:
        print num,'是一个质数'

print '\n以下实例使用了嵌套循环输出2--100之间的素数'
i = 2
while (i < 100):
    j = 2
    while(j <=(i/j)):
        if not(i%j):break
        j = j + 1
    if (j > (i/j)):print i ,'是素数'
    i = i+1

print 'continue'
j = 2
for i in range(10):
    if i!= 0:
        if (i%j)> 0:
            print i,'不能整除2'
            continue
        else:
            print i,'能整除2'
    else:
        print '结束'

