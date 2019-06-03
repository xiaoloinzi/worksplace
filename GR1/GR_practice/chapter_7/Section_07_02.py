# encoding=utf-8
import random,os,math
# 11、实现DOS命令执行功能，接受输入命令并执行，然后把执行结果和
# 返回码打印到屏幕

str1 = raw_input('please input command ：')
str2 = os.popen('%s'%str1)
for i in str2:
    print i.decode('gbk')


# 12、求一个n*n矩阵对角线元素之和


def SumOfDiagonalElements(lista):
    try:
        n = len(lista)
        m,num,str1= 0,0,0
        for i in xrange(len(lista)):
            if len(lista) != len(lista[i]):
                raise IndexError(u'不是n*n矩阵列表!')
            if not isinstance(list1[i][n-1],(int,float)):
                raise TypeError(u'对角元素不是数值，不能进行计算!')
            if not isinstance(lista[i][m],(int,float)):
                raise TypeError(u'对角元素不是数值，不能进行计算!')
            if lista[i][n-1]!= lista[i][m]:
                num += lista[i][n-1]+ lista[i][m]
            if lista[i][n-1]== lista[i][m]:
                str1 = lista[i][m]
            n -=1
            m += 1
        print u'对角线元素之和：',
        return num+str1
    except Exception,e:
        return e

list1 = [[1,2,3,4,5],[5,6,7,8,9],[1,2,3,4,5],[5,6,7,8,9],[5,6,7,8,9]]
list4 = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]
list2 = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,'2']]
list3 = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7]]
print SumOfDiagonalElements(list1)
print SumOfDiagonalElements(list4)
print SumOfDiagonalElements(list2)
print SumOfDiagonalElements(list3)

# 老师的方法：
# 1 2 3
# 4 5 6
# 7 8 9
# 1、i == j (左边开始)
# 2、i+j = n-1
# 0 2=n-1
# 1 1
# 2 0
def sumMatrix(matrix):
    if len(matrix)==0:
        return None
    mLen = len(matrix[0])
    sum = 0
    for i in xrange(0,mLen):
        for j in xrange(0,mLen):
            if i == j or (i+j)==mLen-1:
                sum += matrix[i][j]
    return sum
if __name__=='__main__':
    matrix = list4 = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]
    print sumMatrix(matrix)



# 13、输入一个数组，最大的与第一个元素交换，最小的与最后一个元素
# 交换，输出数组

def ExchangeElement(list1):
    try:
        maxnum = max(list1)
        minnum = min(list1)
        dict1 = {x:list1[x] for x in xrange(len(list1))}
        print u'初始列表：',list1
        for key,value in dict1.items():
            if value==maxnum:
                dict1[key] = dict1[0]
                dict1[0] = maxnum
            if value==minnum:
                dict1[key] = dict1[len(list1)-1]
                dict1[len(list1)-1] = minnum
        print u'交换后列表：',
        return list(dict1.values())
    except Exception,e:
        return e

if __name__=='__main__':
    list1 = [6,1,8,3,5,7,98,34,67,156,23,56,12,12]
    print ExchangeElement(list1)

# 老师的方法：
array = [2,34,54,33,12,123]
lenArray = len(array)
max = max(array)
min = min(array)
maxIndex = array.index(max)
if maxIndex !=0:
    array[0],array[maxIndex] = max,array
minIdex = array.index(min)
if minIdex != lenArray-1:
    array[-1],array[minIdex] = min,array[-1]
print array


# 14、平衡点，一个数组，有一个数字左边所有的数字加起来的总和等于
# 这个数右边所有数字的总和，请输出这个数以及坐标


def LeftRightSum(listr):
    try:
        for i in xrange(len(listr)):
            if sum(listr[:i]) == sum(listr[i+1:]):
                print u'左右两边之和相等的数是：',listr[i],
                print u'，坐标是：',
                return i
        return u'没有一个数字左边所有的数字加起来的总和等于这个数右边所有数字的总和'
    except Exception,e:
        return e
lista = [2,1,6,4,8,0,9,6,4,3,2,5,7,6,8,9,13,45,34]
list1 = [1,3,2,4,2,4,6]
print LeftRightSum(list1)
print LeftRightSum(lista)

# 老师的方法：

def add(a,b):
    return a+b
def findBalance(listNum):
    for i in xrange(len(listNum)):
        if reduce(add,listNum[:i],0) == reduce(add,listNum[i+1:],0):
            print 'position:',i
            print 'value:',listNum[i]
            break


# 15、 将单词表中由相同字母组成的单词归成一类， 每类单词按照单词的
# 首字母排序， 并按每类中第一个单词字典序由大到小排列输出各个类别。
# 输入格式： 按字典序由小到大输入若干个单词， 每个单词占一行，
# 以end结束输入。
# cinema
# iceman
# maps
# spam
# aboard
# abroad
# end
# 输出格式： 一类单词一行， 类别间单词以空格隔开。
# aboard abroad
# cinema iceman
# maps spam

def danCi():
    '''
    将单词表中由相同字母组成的单词归成一类， 每类单词按照单词的
    首字母排序， 并按每类中第一个单词字典序由大到小排列输出各个类别。
    输入格式： 按字典序由小到大输入若干个单词， 每个单词占一行，
    '''
    list1 = []
    dict1 = {}
    str1 = ''
    while str1 != 'end':
        str1 = raw_input(u'按字典序由小到大输入若干个单词,以end结束输入:').strip()
        if str1 != 'end':
            list1.append(str1)
    # list1 = ['cinema','iceman','maps','spam','aboard','abroad']
    for i in list1:
        str1 = list(i)
        str1.sort()
        keystr = ''.join(str1)
        if keystr in dict1:
            dict1[keystr].append(i)
        else:
            dict1[keystr]=[i]
    ste = sorted(dict1.items(),key=lambda e:e[1][0],reverse=True)
    for x in ste:
        for v in x[1]:
            print v,
        print

if __name__=='__main__':
    danCi()

# 老师的方法：
# 算法：{}
def wordToAlph(word):
    wordList = list(word)
    wordList.sort()
    return tuple(wordList)

def findSameWord(wordsList):
    classifyDict = {}
    for i in wordsList:
        alphTup = wordToAlph(i)
        if classifyDict.has_key(alphTup):
            classifyDict[alphTup].append(i)
        else:
            classifyDict[alphTup] = [i]
    return classifyDict.values()

def main():
    wordsList = []
    print u'输入'
    while True:
        s = raw_input()
        if s.lower()=='end':
            break
        wordsList.append(s)
    classfyList = findSameWord(wordsList)
    classfyList = sorted(classfyList,key=lambda j:j[0])
    print u'输出'
    for i in range(len(classfyList)):
        classfyList[i] = sorted(classfyList[i],key= lambda  :i[0])
        print ' '.join(classfyList[i])

if __name__=='__mian__':
    main()



# 16、 输入一个数组， 实现一个函数， 让所有奇数都在偶数前面


def OddevenArrangement(lista):
    try:
        list1 = []
        list2 = []
        for i in lista:
            if i%2==0:
                list1.append(i)
            if i%2 != 0:
                list2.append(i)
        list1.sort()
        list2.sort()
        list1.extend(list2)
        return list1
    except Exception,e:
        print u'非法参数：',e

lista = [2,1,6,4,8,0,9,6,4,3,2,5,7,6,8,9,13,45,34]
listb = [2,1,'d',4,'d',0,9,6,4,3,2,5,7,6,8,9,13,45,34]
tuple1 = (1,2,5,3,7,35,8,5)

print OddevenArrangement(lista)
print OddevenArrangement(listb)
print OddevenArrangement(tuple1)

# 老师的方法：

def func(listNum):
    oddList = []
    evenList = []
    for i in listNum:
        if i%2 ==1:
            oddList.append(i)
        else:
            evenList.append(i)
    return oddList + evenList

if __name__=='__main__':
    print func([1,2,3,4,5,6,7,8])


# 17、 lista=['a','abc','d','abc','fgi','abf']，
# 寻找列表中第一次出现次数最多的第一个字母， 出现了几次


lista=['d','abc','d','abc','fdgi','abdf','de','dr','ag']

def appearsMostfirstLetter(lista):
    try:
        dict1 = {}
        for i in lista:
            if dict1.has_key(i[0]):
                dict1[i[0]] += 1
            else:
                dict1[i[0]] = 1
        num = max(dict1.values())
        s = [i[0] for i in lista]
        for i in s:
            if s.count(i) == num:
                return u'第一次出现次数最多的第一个字母：%s ，出现了%d次'%(i,num)
    except Exception,e:
        print u'非法参数：',e
print appearsMostfirstLetter(lista)

# 老师的方法：
lista=['a','abc','d','abc','fgi','abf']
str1 = ''.join(lista)
set1 = set(str1)
dict1 = {}
for i in set1:
    count = str1.count(i)
    if dict1.has_key(count):
        dict1[count].append(i)
    else:
        dict1[count] = [i]
list2 = dict1.keys()
list2.sort(reverse=True)
print u'次数最多的是:',dict1[list2[0]],u'，次数是：',list2[0]

# 18、 请输入星期几的第一个字母来判断一下是星期几， 如果第一个字母
# 一样， 则继续判断第二个字母
# Monday, Tuesday, Wednesday,
# Thursday, Friday, Saturday, Sunday

def printweek(strone):
    '''
    请输入星期几的第一个字母来判断一下是星期几， 如果第一个字母
    一样， 则继续判断第二个字母
    '''
    if strone.lower() == 'm':
        return u'星期一'
    if strone.lower() == 'w':
        return u'星期三'
    if strone.lower() == 'f':
        return u'星期五'
    if strone.lower() == 't':
        strtwo  = raw_input(u'请输入第二个字母：')
        if strtwo.lower() == 'u':
            return u'星期二'
        elif strtwo.lower() == 'h':
            return u'星期四'
        else:
            return u'不存在的日期'
    if strone.lower() == 's':
        strtwo  = raw_input(u'请输入第二个字母：')
        if strtwo.lower() == 'u':
            return u'星期日'
        elif strtwo.lower() == 'a':
            return u'星期六'
        else:
            return u'不存在的日期'

if __name__=='__main__':
    print printweek('w')
    print printweek('T')

# 老师的方法
import calendar

list1 = []
for i in calendar.day_name:
    list1.append(i.lower())
print list1

def judge(strList,startStr):
    retStr = []
    count = 0
    for i in strList:
        if i.startswith(startStr.lower()):
            count += 1
            retStr.append(i)
    return count,retStr

if __name__ == '__main__':
    while True:
        input = raw_input('please input the first char:')
        if input.lower() == 'exit':
            break
        ret = judge(list1,input)
        if ret[0] == 1:
            print 'This is ',ret[1][0]
        elif ret[0] == 2:
            input2 = raw_input('please input the second char:')
            subStr = input + input2
            ret2 = judge(list1,subStr)
            if ret2[0]==1:
                print 'This is ',ret2[1][0]
            else:
                print 'input error ,your input is ',subStr
        else:
            print 'input error ,your input is ',input



# 19、 有一堆100块的石头， 2个人轮流随机从中取1-5块，
# 谁取最后一块就谁win， 编程实现此过程

def printWinMan():
    try:
        n = 100
        while True:
            for i in xrange(1,3):
                num = random.randint(1,5)
                n = n - num
                print i,u'取得数量：',num,u'，剩余数量:',n
                if n == 0 or n<0:
                    return u'win man：'+str(i)
    except Exception,e:
        return u'非法参数：',e
print printWinMan()

# 老师的方法：

import random

sum = 0
while True:
    print 'sum == %d'%sum
    if sum < 100:
        first = random.randint(1,5)
        print 'first get %d'%first
        sum += first
        if sum < 100:
            second = random.randint(1,5)
            print 'second get ',second
            sum += second
        else:
            print 'first win'
            break
    else:
        print 'second win'
        break
print sum

# 20、 实现一个方法， 判断一个正整数是否是2的乘方，
# 比如16是2的4次方，返回True； 18不是2的乘方， 返回False。
# 要求性能尽可能高

def printChenf(num):
    '''
    判断一个正整数是否是2的乘方
    :param num: 传入一个正整数
    :return:
    '''
    # print (9&9-1)==0
    return (num&num-1)==0

if __name__ == '__main__':
    print printChenf(18)
    print printChenf(16)

# 老师的方法：
def func(num):
    if num < 1:
        return False
    while num > 1:
        if num%2 == 1:
            return False
        else:
            num /= 2
    return True

print func(2046)
print func(2048)




# 9、 编写程序片段， 定义表示课程的类Course。 课程的属性包括课程
# 名、 编号、 选修课号； 方法包括设置课程名、 设置编号、 设置选修课
# 号以及获取课程名、 获取编号、 获取选修课程号， 然后打印输出该对
# 象的课程名、 编号以及选修课号。

class Course(object):
    def __init__(self,curriculum,number,elective):
        self.__curriculum = curriculum
        self.__number = number
        self.__elective = elective

    @property
    def curriculum(self):
        return self.__curriculum

    @curriculum.setter
    def curriculum(self,curriculum):
        self.__curriculum = curriculum

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self,number):
        self.__number = number

    @property
    def elective(self):
        return self.__elective

    @elective.setter
    def elective(self,elective):
        self.__elective = elective

if __name__=='__main__':
    obj = Course(u'计算机',23,456)
    print obj.curriculum,obj.elective,obj.number
    obj.curriculum=u'英语'
    obj.elective=78
    obj.number=55


# 老师的方法：


#     print obj.curriculum,obj.elective,obj.number
# 10、 实现一个多重继承类， 并访问该类

class A(object):
    countA = 1
    def __init__(self,name):
        self.name = name
        print 'class A'
        A.countA += 1

    def printcount(self):
        print 'countA:',A.countA

    def printname(self):
        return self.name

class B(object):
    def __init__(self):
        print 'class B'

class C(A,B):
    def __init__(self,name):
        A.__init__(self,name=name)
        B.__init__(self)

    def printB(self):
        return self.name

if __name__=='__main__':
    obj = C('guarong')
    print obj.name
    obj.printcount()
    print obj.printname()
    print obj.printB()

# 11、请编写一个decorator
# 要求：
# 在函数调用前后打印出'begin call'， 函数执行结束后打印'end call'的字
# 样的日志
# 写出的@log的decorator， 使它既能支持无参数的decorator：
# @log
# def f():
# pass
# 又支持有参数的decorator：
# @log('execute')
# def f():
# pass

class A(object):
    def __init__(self):
        print 'class A def printA'

def log(ss):
    def ww(func):
        def wrapper(*agrs,**kwagrs):
            print 'begin call'
            ste = func(*agrs,**kwagrs)
            print 'end call'
            return ste
        return wrapper
    ss()
    return ww

@log
def now():
    print 'begin call'

@log(A)
def now():
    print 'begin call'
now()
