# encoding=utf-8
# 1、打印2000-3000之间被7整除但不被5整除的数，以，(逗号)分隔。
# 输出格式要求：以逗号隔开，最后一位数后面不能出现多余的符号
# 比如：2002, 2009, 2016, 2023

lista = []
for i in range(2000,3001):
    if i % 7 == 0 and i % 5 != 0:
       lista.append(i)
for j in lista:
    if j is lista[-1]:
        print j
    else:
        print j,',',


# 2、输出9*9口诀表

for i in range(1,10):
    for j in range(i,10):
        print i,'*',j,'=',i*j,'\t',
    print '\n',



# 3、计算1-1/2+1/3-1/4+…+1/99-1/100+…直到最后一项的绝对值小于10
# 的-5次幂为止

sine = 1
for i in range(2,10**5+1):
    if float(1.0/i) < float(1.0/10**5):
        break
    elif i%2==0:
        sine -= float(1.0/i)
    else:
        sine += float(1.0/i)
print sine


# 4、编程将类似“China”这样的明文译成密文，密码规律是：用字母表中原
# 来的字母后面第4个字母代替原来的字母，不能改变其大小写，如果超出了字
# 母表最后一个字母则回退到字母表中第一个字母

str1 ='VWXYZwxyz'# 'China'

def ZhuanHuan(str1):
    listb = []
    for i in str1:
        if i.islower():
            if ord(i)+4 > 122:
                listb.append(chr(97))
            else:
                i = chr(ord(i)+4)
                listb.append(i)
        elif i.isupper():
            if ord(i)+4 > 90:
                listb.append(chr(65))
            else:
                i = chr(ord(i)+4)
                listb.append(i)
    print ''.join(listb)

ZhuanHuan(str1)


# 5、输出以下如下规律的矩阵
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20

for i in range(1,5):
    for j in range(1,6):
        sum = i*j
        print sum,
    print



# 6、对一个列表求和，如列表是[4, 3, 6]，求和结果是 [4, 7, 13]，分别是列表
# 的前1，2，3个数的总和

def QiuLhe(lista):
    sine = 0
    list1 = []
    for i in lista:
        sine += i
        list1.append(sine)
    print list1

lista = [4,3,6]
QiuLhe(lista)


# 7、一个字符串 list，每个元素是 1 个 ip，输出出现次数最多的 ip

str1 = "If you do not learn to think when you are young, you may never learn"
list1 = str1.replace(',','').replace('.','').split(' ')
dict1 = {}

for i in list1:
    if dict1.has_key(i):
        dict1[i] += 1
    else:
        dict1[i] = 1

print dict1

for key,value in dict1.items():
    if value == max(dict1.values()):
        print u'出现最多次数的IP是',key


# 8、打印100以内的素数
# 质数（prime number）又称素数。只能被1和其本身整除。根据算术基本定
# 理，每一个比1大的整数，要么本身是一个质数，要么可以写成一系列质数的
# 乘积，最小的质数是2。

lista=[]
for x in xrange(1,100):
    n = 0
    for y in xrange(1,x+1):
        if x % y == 0:
            n = n + 1
    if n == 2 :
        lista.append(x)
print lista



# 9、实现一个简易版的计算器


def Add(x,y):
    '''
    加法
    '''
    return x+y
def Jina(x,y):
    '''
    减法
    '''
    return x-y
def Chen(x,y):
    '''
    乘法
    '''
    return x*y
def Chu(x,y):
    '''
    除法
    '''
    return x/y
print u'选择运算，1：加法，2：减法，3：乘法，4：除法'
sine = raw_input(u'请输入要进行的运算（1/2/3/4)：')
x = float(raw_input(u'请输入第一个数：'))
y = float(raw_input(u'请输入第二个数：'))
if sine == '1':
    print x,'+',y,'=',Add(x,y)
elif sine == '2':
    print x,'-',y,'=',Jina(x,y)
elif sine == '3':
    print x,'*',y,'=',Chen(x,y)
elif sine == '4':
    print x,'/',y,'=',Chu(x,y)
else:
    print u'输入有误！'


# 10、有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的
# 前20项之和

f1 = 1.0
f2 = 2.0
f3 = 0.0
for i in xrange(20):
    f3 += f2/f1
    f2,f1 = f1+f2,f2
print u'数列的前20项之和:%0.2f'%f3


# 11、画等（腰）边三角形（实心、空心）

# 空心
for i in xrange(5):
    if i == 4:
        print '*'
    print '',
for j in xrange(1,5):
    if j == 2 :
        print '*',
    elif  j ==4:
        print '*'
    print '',
for n in xrange(5):
    if n == 0 or n ==1 :
        print '*',
    elif  n ==2:
        print '*'
    print '',

print '\n'
#
# # 实心
for i in xrange(6):
    if i == 4:
        print '*'
    print '',
for j in xrange(1,6):
    if j == 2 :
        print '*',
    elif  j ==3:
        print '*',
    elif  j ==4:
        print '*'
for n in xrange(6):
    if n == 0 or n ==1 :
        print '*',
    elif  n ==2:
        print '*',
    elif  n ==3:
        print '*'
    print '',


# 12、画倒等边三角形

for i in xrange(10):
    if i == 3:
        print '*',
    elif  i ==6:
        print '*',
    elif  i ==9:
        print '*'
    print '',
for j in xrange(1,10):
    if j == 5 :
        print '*',
    elif  j ==8:
        print '*'
    print '',
for n in xrange(6):
    if n ==5:
        print '*'
    print '',


# 13、画直角三角形（实心、空心）

# 空心
for i in xrange(6):
    if i == 0:
        print '*'
for j in xrange(6):
    if j == 0 :
        print '*',
    elif j == 2:
        print '*'
        break
    print '',
for s in xrange(6):
    if s == 0 :
        print '*',
    elif s ==4:
        print '*'
        break
    print '',
for n in xrange(6):
    if n == 0 :
        print '*',
    elif n == 1:
        print '*',
    elif n == 2:
        print '*',
    elif n == 3:
        print '*'
    print '',
print '\n'
# 实心
for i in xrange(6):
    if i == 0:
        print '*'
for j in xrange(6):
    if j == 0 :
        print '*',
    elif  j ==3:
        print '*'
for j in xrange(6):
    if j == 0 :
        print '*',
    elif  j ==3:
        print '*',
    elif  j ==4:
        print '*'
for n in xrange(6):
    if n == 0 or n ==1 :
        print '*',
    elif  n ==2:
        print '*',
    print '',


# 14、用*号输出字母C的图案

for i in xrange(16):
    if i < 4:
        print '*',
    elif i>4 and i< 10:
        print '*'
    elif i > 10:
        print '*',


# 15、打印N，口，H图案

# N
print u'N字'
for i in xrange(60):
    if i == 0:print '*',
    elif i == 12:
        print '*'
        continue
    elif i == 13:print '*',
    elif i == 15:print '*',
    elif i == 23:
        print '*'
        continue
    elif i == 24:print '*',
    elif i == 28:print '*',
    elif i == 34:
        print '*'
        continue
    elif i ==35:print '*',
    elif i == 42:print '*',
    elif i == 45:
        print '*'
        continue
    elif i ==46:print '*',
    elif i == 58:print '*'
    print '',

# 口
print u'\n口字'
for i in xrange(40):
    if i < 5:
        print '*',
    elif i==6:print '\n*',
    elif i == 16:
        print '*'
        continue
    elif i == 17:print'*',
    elif i == 27:
        print '*'
        continue
    elif i > 27 and i<33:print '*',
    print '',

# H
print '\nH字'

for i in xrange(20):
    if i == 0:
        print '*',
    elif i == 6:
        print '*'
        continue
    elif i == 7:
        print '*',
    elif i == 9:
        print '*',
    elif i == 11:
        print '*'
        continue
    elif i == 12:
        print '*',
    elif i == 18:
        print '*'
    print '',


# 16、打印出如图所示的杨辉三角形，要求可以自定义行数

def YangHui(n):
    a = []
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(0)
    for i in range(n):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2,n):
        for j in range(1,i):
            a[i][j] = a[i - 1][j-1] + a[i - 1][j]
    from sys import stdout
    for i in range(n):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print
YangHui(10)


# 17、打印如图所示图案，要求支持指定行数，但行数必须是奇数行

def DaYin(n):
    if n % 2 == 0:
        raise SyntaxError(u'行数只能是奇数')
    from sys import stdout
    for i in range(1,n+1,2):
        for j in range(i):
            stdout.write('*')
            stdout.write(' ')
        print
    for i in range(1,n+1,2):
        for j in range(n-1-i):
            stdout.write('*')
            stdout.write(' ')
        print

DaYin(9)


# 18、要求实现一函数，该函数用于求两个集合的差集，结果集合中包含
# 所有属于第一个集合但不属于第二个集合的元素

lista = [1,2,3,4]
listb = [2,3,5]
tuple1 = (1,2,3,67,8)
tuple2 = (2,3)
set1 = set(tuple1)
set2 = set(tuple2)
def ChaJi(lista,listb):
    '''
    求两个集合的差集,打印所有属于第一个集合但不属于第二个集合的元素
    '''
    listc = []
    for i in lista:
        if i not in listb:
            listc.append(i)
    print u'差集是：',listc
ChaJi(set1,set2)


# 19、找出一段句子中最长的单词及其索引位置，以list返回

str = "If you do not learn to think when you are young."

list1 = str.replace(',','').replace('.','').split(' ')
dicr = {}
#数据结构就是用来存储数据的结构
lista = []
maxlist = [list1[0]]

for i in list1:
    if len(i) > len(maxlist[0]):
        maxlist = []
        maxlist.append(i)
    elif len(i) == len(maxlist[0]):
        maxlist.append(i)
for j in range(len(maxlist)):
    s = str.find(maxlist[j])
    lista.append(s)

print maxlist
print lista


# 20、返回序列中的最大数

a = [1,7,18,10]
b = (1,9,3,10,5)

def Sine(n):
    sine1 = int(n[0])
    for i in n:
        if sine1 < int(i):
            sine1 = i
    print sine1

Sine(a)
Sine(b)



















