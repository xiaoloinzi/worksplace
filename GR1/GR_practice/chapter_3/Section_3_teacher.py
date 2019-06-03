# encoding=utf-8
# encoding=utf-8
# 1、打印2000-3000之间被7整除但不被5整除的数，以，(逗号)分隔。
# 输出格式要求：以逗号隔开，最后一位数后面不能出现多余的符号
# 比如：2002, 2009, 2016, 2023
# 1、遍历2000-30000的数，然后进行判断，打印出符合条件的数值

lista = []
for i in range(2000,3001):
    if i % 7 == 0 and i % 5 != 0:
       lista.append(i)
for j in lista:
    if j is lista[-1]:
        print j
    else:
        print j,',',
#老师的方法
for i in xrange(2000,3001):
    if i%7 == 0 and i%5!=0:
        if i +7 >3000:
            print '%s'%(i)
        else:
            print '%s,'%(i)


# 2、输出9*9口诀表

for i in range(1,10):
    for j in range(i,10):
        print i,'*',j,'=',i*j,'\t',
    print '\n',
# 老师的方法：
# 1、1*1=1
# 2*1 =2 2*2 =4.。。。。
# 算法：1、遍历从1--9
# 2、对于N,从1到N
for i in xrange(1,10):
    for j in xrange(1,i+1):
        print i,'*',j,'=',i*j,
    print



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

# 老师的方法：
# 算法：1、e=1.0/100000,1.0/n>=e则不对n进行处理，否则n = n+1或n= n-1
n = 2
e = 1.0 / 100000
result = 1
while 1.0/n >=e:
    if n%2 ==0:
        result -=1.0/n
    else:
        result +=1.0/n
    n+=1
print n
print result


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


# 老师的方法：abcdefg--efghijl
# 算法:1、使用ASCII去运算：A-Z：65~90；a-z:97~122；
# 2、把一个人字符转换为ASCII码，小写字符要与122座判断，大写要与90做判断，没有越界：用chr(ord(x)+4)
# 越界：97+ord(x)+4-122-1
# 3、大写字符：越界：65+ord(x)+4-90-1

import string
str = raw_input('please input string')
newStr = ''
for s in str:
    if s in string.lowercase:#判断是否为小写
        if ord(s)+4 >122:
            newStr +=chr(97+ord(s)+4-122-1)
        else:
            newStr +=chr(ord(s)+4)
    elif s in string.uppercase:
        if ord(s)+4>90:
            newStr +=chr(65+ord(s)+4-90-1)
        else:
            newStr +=chr(ord(s)+4)
print 'new string:',newStr





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

# 老师的方法
# 算法：1、规律：倍数规律；2、从行的维度取遍历；3、从每行的列维度去遍历 j*i

def makeMatrix(rowNum,colNum):
    for i in xrange(1,rowNum+1):
        for j in xrange(1,colNum+1):
            print '%5s'%str(j*i),
        print

makeMatrix(4,5)


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

# 老师的方法：
# 算法：1、统计列表中元素的次数用count；2、把相同的最多次数需要统计
# 3、次数count；ip=[]，相同IP可能有多个，所以需要用列表取维护

listIP = ['192.168.2.3', '10.2.3.45', '124.56.78.3',
            '192.168.2.3', '124.56.78.3', '10.2.78.2',
            '124.56.78.3', '1.2.3.2', '124.56.78.3',
            '10.2.3.45','10.2.3.45','10.2.3.45']


maxOccurTimes = 0
maxOccurIP = []

for ip in listIP:
    if listIP.count(ip) > maxOccurTimes and ip not in maxOccurIP:
#         如果判断一个新的元素。。。
        maxOccurIP = []
        maxOccurIP.append(ip)
        maxOccurTimes = listIP.count(ip)
    elif listIP.count(ip) == maxOccurTimes and ip not in maxOccurIP:
        maxOccurIP.append(ip)

print '%s occurs %d times '%(str(maxOccurIP),maxOccurTimes)








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

# 老师的做法：
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y
def div(x,y):
    if y != 0:
        return  x/(y*1.0)
    else:
        return -1

x = int(raw_input('x='))
y = int(raw_input('y='))
print 'x+y=',add(x,y)
print 'x-y=',sub(x,y)
print 'x*y=',mul(x,y)
print 'x/y=',div(x,y)


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


# 老师的做法：
# 算法：1、星号的规律：1,3,5,7,9以奇数的规律在走
# 2、空格的规律：20,19,18,17,16
# 实心的

def printTrigle(n):
    for i in xrange(n):
        print ' '*(20-i),'*'*(2*i+1)
printTrigle(5)

# 空心：算法：1、第一行和最后一行全是*号；
# 2、中间的行，除了第一和最后一个*号，其余为空格

def printHollowTriangle(n):
    for i in xrange(1,n+1):
        if i ==1:
            print ' '*20,'*'
            continue
        elif i == n:
            print ' '*(20-i),'*'*(2*i)+1
            break

        else:
            print ' '*(20-i),'*',' '*(2*i-3),'*'

printHollowTriangle(5)




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

# 老师的方法：
# 算法：1、星星：5,3,1；2、空格：0,1,2

def printRegularTriangle(n):
    for i in xrange(n):
        print ' '*(20+i),'*'*(2*n-1-2*i)

printRegularTriangle(10)



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

# 老师的方法：
# 算法：1、星星：1,2,3，4

# 实心
def printTriangle(n):
    for i in xrange(1,n+1):
        print '*'*i
printTrigle(10)

# 空心：1、第一和第二和最后要全部打印，其他的打印第一个和最后一个

def printTriangle(n):
    for i in xrange(1,n+1):
        if i <= 2 or i == n:
            print '*'*i
        else:
            print '*'+' '*(i-2)+'*'

printTriangle(10)






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


# 老师的方法
# N思路：用* 表示，1、有行和列；2、第一列和最后一列，有* 号
#3、横坐标和纵坐标相等，有*
#4、用两个for循环，得到横河列

for i in xrange(5):
    for j in xrange(5):
        if j == 0 or j==4 or i==j:
            print '*',
        else:
            print ' ',
    print

# 口思路：1、第一行和最后一行是*；2、第一列和最后一列是*
# 3、表示行，j表示列

for i in xrange(5):
    for j in xrange(5):
        if i ==0 or i ==4 or j ==0 or j==4:
            print '*',
        else:
            print ' ',
        print
# H思路：1、第一列和最后一列是* ；2、中间一行全是*；3、i表示行，j表示列
for i in xrange(5):
    for j in xrange(4):
        if j ==0 or j==3:
            print '*',
            continue
        if i ==2 and j<3:
            print '*',
            continue
        print ' '
    print




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

# 老师的思路：
# 思路：1、list1[i]=list2[i-1]+list2[i-2]
# 2、list1的值是根据list2的值求得的

def printArray(n):
    oneLine = [0,1]
    for i in xrange(1,n+1):
        if i == 1:
            print 1
            continue
        tmpList = []
        for j in xrange(1,i+1):
            if j ==1 or j ==i:
                tmpList.append(1)
                print 1,
            else:
                e = oneLine[j-2]+oneLine[j-1]
                tmpList.append(e)
                print e,
        oneLine = tmpList[:]
        print

printArray(10)







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

# 老师的做法
# 思路：1、函数来求解，参数为行数，并且是奇数
# 2、1~(n/2+1),*是以2递增
# 3、从（n/2+1)~n，*以2递减
def printStar(n):
    x =0
    for i in xrange(n/2+1):
        print '*'*(2*i+1)
        x = 2*i+1
    for i in xrange(n/2):
        print '*'*(x-2*(i+1))

printStar(9)



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
# 老师的方法
def diffList(list1,list2):
    resultList = []
    for i in list1:
        if i not in list2:
            resultList.append(i)
    return resultList

list1 =[1,2,'a','vvf',4,6]
list2 = [2,4,7,8,9]

print diffList(list1,list2)

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

# 老师的方法：直接使用max()

















