# encoding=utf-8
# 1、从键盘输入两个数，并比较其大小，直到输入e/E退出程序

def BiJiao(n,m):
    '''
    比较n,m和大小，返回比较值
    :param n: 为比较的第一个数
    :param m: 为比较的第二个数
    :return:返回比较值(为空)
    '''
    if n>m:
        print n,u'比',m,u'大'

    else:
        print n,u'比',m,u'小'
while True:
    int1 = raw_input(u'请输入要比较的第一个数：')

    if int1 == 'e' or int1 == 'E':
        exit()
    int2 = raw_input(u'请输入要比较的第二个数：')
    if int2 == 'e' or int2 == 'E':
        exit()
    int1 = float(int1)
    int2 = float(int2)
    BiJiao(int1,int2)


# 老师的方法：
# 思路：
# 浮点数不能比较相等，只能比较精度
while True:
    a = raw_input('plz input a:').strip()
    if a == 'E' or a== 'e':
        print u'程序退出'
        exit()
    b = raw_input('pla input B:').strip()
    if b == 'E' or b== 'e':
        print u'程序退出'
        exit()
    a = int(a)
    b = int(b)
    if a>b:
        print 'a>b'
    elif a==b:
        print 'a=b'
    else:
        print 'a<b'








# 2、请写一个函数，第一个参数为一个字母，另外一个参数为一个数字n，请返回这个字
# 母后的第n个字母，如果达到字母表的末尾，则从头开始选取字母(a-z:97-122;A-Z:65-90)

import string
def xuanQuZiMu(m,n):
    dup = n%26
    if len(m)>=2 or m not in string.letters:
        raise TypeError(u'输入值不是一个字母')
    elif m.islower():
        if ord(m)+dup > 122:
            sine = chr(ord(m)+dup-122+97-1)
            print m,u'返回%d个字母是%s'%(n,sine)
        else:
            sine = chr(ord(m)+dup)
            print m,u'返回%d个字母是%s'%(n,sine)
    elif m.isupper():
        if ord(m)+dup > 90:
            sine = chr(ord(m)+dup-90+65-1)
            print m,u'返回%d个字母是%s'%(n,sine)
        else:
            sine = chr(ord(m)+dup)
            print m,u'返回%d个字母是%s'%(n,sine)


xuanQuZiMu('s',237)

# 老师的方法
# 思路：1、判断字母是小写还是大写字母；2、n%26取余；3、是否越界，z,Z
# 4、ord \chr
def encodeLetten(letter,n):
    if isinstance(n,int) and n >0:
        n = n%26
    else:
        return -1
    if ord(letter)>=97 and ord(letter) <= 122:
        if ord(letter)+n>122:
            return chr(97+ord(letter)+n-122-1)
        else:
            return chr(ord(letter)+n)
    elif ord(letter)>=65 and ord(letter) <= 90:
        if ord(letter)+n>90:
            return chr(65+ord(letter)+n-90-1)
        else:
            return chr(ord(letter)+n)
    else:
        return -1


print encodeLetten('a',2)
print encodeLetten('X',4)


# 3、分别输出字符串中奇数坐标和偶数坐标的字符
str1 = 'return codecs.utf_8_decode(input, errors, True'
print u'偶数坐标的字符为：',str1[1::2]
print U'奇数坐标的字符为：',str1[::2]

# 老师的思路：
str1 = 'abcdefghijklmn'
print str1[::2]#奇数
print str1[1::2]#偶数





# 4、写程序输出如下图

def FanHui(int1):
    FanHui=[[1]]
    for i in xrange(2, int1+1):
        FanHui.append([1]*i)
        for j in xrange(1, i-1):
            FanHui[i-1][j] = FanHui[i-2][j]+FanHui[i-2][j-1]
    return FanHui

def printFanHui(zuo, you1):
    sine1 = len(zuo[-1])*you1
    for f in zuo:
        result = []
        for g in f:
            result.append('{0:^{1}}'.format(str(g), you1))
        print('{0:^{1}}'.format(''.join(result), sine1))
chang = FanHui(12)
sine = len(str(chang[-1][len(chang[-1])//2]))+3
printFanHui(chang, sine)

# 老师的思路：
def printArray(n):
    oneLine = [0,1]
    for i in xrange(1,n+1):
        if i == 1:
            print ' '*2*(n-i)+str(1)
            print
            continue
        tmpList = []
        for j in xrange(1,i+1):
            if j ==1:
                tmpList.append(1)
                print ' '*2*(n-i)+str(1),
            elif j ==i:
                tmpList.append(1)
                print '  '+str(1),
            else:
                e = oneLine[j-2]+oneLine[j-1]
                tmpList.append(e)
                print '  '+str(e),
        oneLine = tmpList[:]
        print

printArray(10)



# 5、 将一个多重嵌套的列表的元素进行互换， 存到另一个同等维度的嵌套列表中，
# 例如：[[1,2,3],[4,5,6]]互换后变成[[1,4],[2,5],[3,6]]

list1 = [[1,2,3,4,0],[4,5,6,7,9],['a','b','c','d','e'],[1,2,3,7,10]]


def LiebiaoZhuanhuan(list):
    list2 = []
    sine1 = len(list1[0])
    sine2 = len(list1)
    for i in xrange(sine2):#0,1
        for j in xrange(sine1):#0,1,2
            if i == 0:
                list2.append([list1[i][j]])
            else:
                list2[j].append(list1[i][j])
    print list2

LiebiaoZhuanhuan(list1)


# 6、 有一个3 x 4的矩阵， 要求编程求出其中值最大的那个元素的值， 以及
# 其所在的行号和列号， 矩阵可以通过嵌套列表来模拟

list1 = [[1,42,43,4],
         [15,120,77,80],
         [9,120,'z',12],
        [9,10,6,120]]

def ZuiDalbiao(list):
    sine1 = len(list)
    sine2 = len(list[0])
    sine3 = list[0][0]
    for i in xrange(sine1):
        for j in xrange(sine2):
            if list[i][j] > sine3:
                sine3 = list[i][j]
                h = i+1
                l = j+1
    print u'最大的元素：',sine3,u'在第',h,u'行,第',l,u'列'

ZuiDalbiao(list1)
# 老师的思路：1、[[1,2,3,4],[2,2,3,4],[3,3,4,5]];2、最大值可能有多个
# 3、如何表述最大值：值所在的位置，使用字典最合适{值：[(1,4),(2,4)....]}
# 枚举类型
def maxMatrix(mylist):
    maxDIct = {}
    for index,li in enumerate(mylist):
        for i,e in enumerate(li):
            if len(maxDIct)==0:
                maxDIct[e] = [(index+1,i+1)]
            else:
                if maxDIct.keys()[0] < e:
                    maxDIct.clear()
                    maxDIct[e]= [(index+1,i+1)]
                elif maxDIct.keys()[0] ==e:
                    maxDIct[e].append((index+1,i+1))
    return maxDIct
print maxMatrix(list1)



# 7、递归实现列表求和

list1 = [1,2,[2,[3,4],[5,6,7],20],8,9,[10,11],12]

def ListAdd(list1):
    sine = 0
    for i in list1:
        if isinstance(i,list):
            sine +=ListAdd(i)
        else:
            sine += i
    return sine
print ListAdd(list1)

# 老师的方法：
# 在一个函数中自己调用自己
# list1=[1,2,3]
# func(list1)=1+func([2,3])

def getListSum(listVar):
    if len(listVar)>1:
        return listVar[0]+getListSum(listVar[1:])
    else:
        return listVar[0]

list1 = [1,2,3,4,5]

# 8、打印斐波拉契数列前n项
# 0,1,1,2,3,5,8,13

n = 20
def FeiboLaqi(n):
    for i in xrange(n+1):
        if i == 0 or i == 1:
            f0 = 0
            f1 = 1
            print i,
        else:
            f2 = f0 + f1
            print f2,
            f0 = f1
            f1 = f2
    return ''

print FeiboLaqi(n)


# 9、检查ipV4的有效性， 有效则返回True， 否则返回False

import re
strip = '255.255.255.256'

def ipJianChack(ip):
   sine = r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?' \
             r'[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4]' \
             r'[0-9]|[01]?[0-9][0-9]?)\b'
   if re.match(sine,ip):
      return True
   else:
      return False

print ipJianChack(strip)

# 老师的做法：ipv4:192.168.1.11
# 算法：
# 1、点切割的结果
# 2、每个值是否在[0-255]之间

def checkIP(ip):
    if len(ip.split('.'))==4:
        for i in ip.split('.'):
            if int(i) <0 or int(i)>255:
                return False
        return True
    return False

if __name__=='__main__':
    print checkIP('12.3.45.66')
    print checkIP('23.1.34')


# 10、检测密码强度
# c1 : 长度>=8
# c2: 包含数字和字母
# c3: 其他可见的特殊字符
# 强： 满足c1,c2,c3
# 中: 只满足任一2个条件
# 弱： 只满足任一1个或0个条件

import re

str1 = '123@#$%@#ASS$^^'
s = r'\s'
c2 = r'[0-9]&[a-z]&[A-Z]'
c3 = r'\S'

for i in str1:
    if re.match(s,i):
        print u'不能输入为空的字符'
        break
else:
    if len(str1)>=8:
        if re.match(c2,str1) and re.match(c3,str1):
            print u'密码设置为强'
        elif re.match(c2,str1) or re.match(c3,str1):
            print u'密码设置为中'
        else:
            print u'密码设置为弱'

# 老师的做法：
# 算法：
# 1、[True,True,True]把判断的结果存在列表中
# 2、list.count(x)判断密码的强度

def checkPw(password):
    lengthFlag = False
    alphnumFlag = False
    otherFlag = False
    if len(password) >=8:
        lengthFlag =True
    numFlag =False
    alpFlag = False
    for letter in password:
        if letter in string.digits:
            numFlag = True
        elif letter in string.letters:
            alpFlag = True
    alphnumFlag = numFlag and alpFlag

    resultList = []
    resultList.append(lengthFlag)
    resultList.append(alphnumFlag)
    resultList.append(otherFlag)
    if resultList.count(True) == 3:
        print u'强密码'
    elif resultList.count(True) ==2:
        print u'中密码'
    else:
        print u'弱密码'




