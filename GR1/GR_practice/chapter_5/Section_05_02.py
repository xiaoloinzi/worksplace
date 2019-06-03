# encoding=utf-8
# 11、 实现字符串的find方法
# 可在指定字符串范围内查找子字符串出现的位置
# S.find(substr,[start,[end]])必须先有start才能有end
import string


def RealiZationFind(stru,substr,*args):
    if len(args) > 2:
        raise OverflowError(u'指定参数范围有误!')
    if len(args) == 1:
        if isinstance(args[0],int):
            start = args[0]
        else:
            raise TypeError (u'输入的范围值只能是正整数')
    if len(args) == 2:
        if isinstance(args[0],int):
            start = args[0]
            if isinstance(args[1],int):
                end = args[1]
            else:
                raise TypeError (u'输入的范围值只能是正整数')
        else:
            raise TypeError (u'输入的范围值只能是正整数')
    else:
        start = 0
        end = len(stru)
    if start > end:
        raise OverflowError(u'开始索引不能大于结束的索引！')

    if not isinstance(substr,str):
        return -1

    if substr not in stru[start:end+1] or len(substr)==0:
        return -1
    for i in xrange(start,end+1):
        if stru[i:i+len(substr)]  == substr:
            return i
    return -1
print RealiZationFind('ancdefg','cd',1,6)

# 老师的方法：
# find(sourceStr,subStr)
# -1
# >=0
def find(sourceStr,subStr):
    if subStr not in sourceStr or len(subStr) == 0:
        return -1
    for i in xrange(len(sourceStr)):
        if sourceStr[i:i+len(subStr)] == subStr:
            return i
print find('abcabc','ab')#0
print find('abc','d')#-1



# 12、 实现字符串的isalpha方法
# 该函数的作用是，如果S中所有字符都是由字母组成，
# 并且S的长度最小为一，则返回True否则返回False

def RealiZationIsalphe(strs):
    if len(strs) <=0:
        return False
    if not isinstance(strs,str):
        raise AttributeError(u'输入值得属性不是字符串！')
    num = len(strs)
    sine = 0
    for i in strs:
        if 'a' <= i <=  'z' or 'A' <= i<=  'Z':
           sine +=1
    if sine == num:
        return True
    else:
        return False

print RealiZationIsalphe('A')


# 13、 实现字符串的isdigit方法
# s.isdigit()函数的作用是，如果S中所有的字符都是由数字组成，
# 并且S至少有一个字符，则返回True，否则返回False

def RealiZationIsdigit(strs):
    '''
    s.isdigit()函数的作用是，如果S中所有的字符都是由数字组成，
    并且S至少有一个字符，则返回True，否则返回False
    :param strs: 字符串
    :return:False or True
    '''
    if len(strs) <=0:
        return False
    if not isinstance(strs,str):
        raise AttributeError(u'输入值得属性不是字符串！')
    num = len(strs)
    sine = 0
    for i in strs:
        if 48 <= ord(i) <= 57:
           sine +=1
    if sine == num:
        return True
    else:
        return False

print RealiZationIsdigit('10@9')

# 老师的方法：使用ASCII码进行比较，直接使用字符比较
def isdigital(judgestr):
    for i in judgestr:
        if i <'0' or i > '9':
            return False
    return True
print isdigital('ABC123')#False
print isinstance('1234')#True


# 14、 实现字符串的isalnum方法
# S.isalnum()函数的作用是，如果S中所有的字符都是由字母或数字组成，
# 并且S至少有一个字符，则返回True，否则返回False

def RealiZationIsalnum(strs):
    if len(strs) <=0:
        return False
    if not isinstance(strs,str):
        raise AttributeError(u'输入值得属性不是字符串！')
    num = len(strs)
    sine = 0
    for i in strs:
        if 'a' <= i <=  'z' or 'A' <= i<=  'Z'or 48 <= ord(i) <= 57:
           sine +=1
    if sine == num:
        return True
    else:
        return False

print RealiZationIsalnum('')

# 老师的方法：
# string.digits

def isalnum(sourceStr):
    for i in sourceStr:
        if i not in string.digits and i not in string.letters:
            return False
        return True
print isalnum('123')
print isalnum('123abc')
print isalnum('!23dd')


# 15、 实现字符串的join方法
# 将列表拼接为字符串，
def RealiZationjoin(lista,stra=''):
    str1 = lista[0]
    if not isinstance(lista[0],str):
            raise TypeError(u'只有字符串才能进行拼接')
    if not isinstance(stra,str):
        raise TypeError(u'连接词表示字符串')
    for i in xrange(1,len(lista)):
        if not isinstance(lista[i],str):
            raise TypeError(u'只有字符串才能进行拼接')
        str1 += stra + lista[i]
    return str1
print RealiZationjoin(['1234','3','4'],'*')

# 老师的方法：
# join(strList,joinLetter=' ')

def join(strList,jionLetter=' '):
    joinedStr = ''
    for i in strList:
        if joinedStr == '':
            joinedStr = str(i)
        else:
            joinedStr = joinedStr + jionLetter + str(i)
    return joinedStr
print join(['abc','xyz','glory road'])
print join(['abc','123','oj'],'*')


# 16、 实现字符串的replace方法
# 实现替换字符串的指定内容，S.replace(oldstr,newstr,[count])
def RealiZationreplace(stru,oldstr,newstr,num= 0):
    start = 0
    strc = ''
    if not isinstance(oldstr,str):
        raise TypeError(u'被替换的子字符串必须是字符串类型')
    end = len(oldstr)
    if not isinstance(newstr,str):
        raise TypeError(u'要替换对象不是字符串类型')
    if not isinstance(num,int):
        raise TypeError(u'替换参数需要是一个整数 ')
    if oldstr not in stru or num == 0 or num < 0:
        return stru
    if num > stru.count(oldstr):
        num = stru.count(oldstr)
    while num != 0:
        if stru[start:end] == oldstr:
            strc += newstr
            start +=len(oldstr)
            end +=len(oldstr)
            num -=1
        else:
            strc += stru[start:start+1]
            start +=1
            end +=1

    return strc+stru[start:]

print RealiZationreplace('bbog bog bogb','b','3',4)

# 老师的方法：
# replace(sourceStr,oldStr,newStr)
def replace(sourceStr,oldStr,newStr):
    if len(sourceStr) == 0:
        return ''
    oldStrLen = len(oldStr)
    newStrList = []
    start = 0
    while True:
        if sourceStr[start:start+oldStrLen] == oldStr:
            newStrList.append(newStr)
            start += oldStrLen
            if start > len(sourceStr)-1:
                break

        else:
            newStrList.append(sourceStr[start])
            if start == len(sourceStr)-1:
                break
            else:
                start +=1
    return ''.join(newStrList)
print replace('cdcdef','cd','xx')

# 17、 实现字符串的split方法
# 可以用指定的字符串将字符串进行分割，S.split([sep,[maxsplit]])

def RealiZationsplit(strs,stru,num=-1):
    start = 0
    strc = ''
    lista = []
    if not isinstance(strs,str):
        raise TypeError(u'被分割值只能是字符串类型！')
    if not isinstance(stru,str):
        raise TypeError(u'指定值只能是字符串类型！')
    if not isinstance(num,int):
        raise TypeError(u'分割次数只能是正整数')
    end = len(stru)
    sine = len(stru)
    int1 = num
    if num == 0:
        return strs

    if num >= strs.count(stru) or num < 0:
        num = strs.count(stru)
    while num != 0:
        if strs[start:end] == stru:
            if start == 0 or start-1 == 0 or end==len(strs)-1:
                lista.append(strc)
            else:
                lista.append(strc)
                strc = ''
            start += sine
            end += sine
            num -= 1
        else:
            strc += strs[start]
            start += 1
            end += 1
    lista.append(strs[start:])
    if int1 >= strs.count(stru) or int1 < 0:
        if len(stru) == 1 and stru+stru == strs[-2:]:
            lista.append('')
    return lista
print RealiZationsplit('bbog bog bogbb','bb',-2)


# 老师的方法：
# split(sourceStr,splitStr)

def split(sourceStr,splitStr=None):
    if splitStr is None:
        pSqe = [' ','\t','\n','\f','\v','\r']
        stringList = list(sourceStr)
        for i in range(len(stringList)):
            if stringList[i] in pSqe:
                stringList[i] = ' '
                if i+1 < len(stringList) and stringList[i+1] in pSqe:
                    stringList[i] = ''
        sourceStr = ''.join(stringList)
        splitStr = ' '
    tmp = ''
    length = len(splitStr)
    result = []
    i = 0
    while i <= len(sourceStr) -1:
        if sourceStr[i:i+length] == splitStr:
            result.append(tmp)
            tmp = ''
            i += length
        else:
            tmp += sourceStr[i]
            i += 1
    result.append(tmp)
    return result
print split('abccdefg','cde')
print split('abc abc\tabc\fabc\nabc')
print split('absdssbd','b')

# 18、 实现字符串的strip方法
#可以将字符串的左右空格等空白内容或指定的字符串去除，并返回处理后的结果，
# 但原字符串未被改变。

def funcSrip(str,str1='\t\n\r '):
    for i in xrange(len(str)):
        if str[i] not in str1:
            break
    str2 = str[::-1]
    for j in xrange(len(str)):
        if str2[j] not in str1:
            break
    return str[i:-j]

str3 = '\n\t abc ccc\n\t '
print funcSrip(str3)
str4 = '*bay *bay*'
print funcSrip(str4,'*')



# 19、 报数问题： 有n个人围成一圈， 顺序排号。 从第一个人开始报数（ 从1到3报数）
# ， 凡报到3的人退出圈子， 问最后留下的是原来第几号的那位

def BaoShu(n):
    if not isinstance(n,int):
        raise TypeError(u'请输入大于‘0’的正整数')
    if n < 0:
        raise AttributeError(u'请输入大于‘0’的正整数')
    if n == 0:
        raise AttributeError(u'请输入大于‘0’的正整数')
    dict1 = {}
    list1 = []
    s = 1
    for i in xrange(n):
        dict1[i+1] = []
        list1.append(i)
    while len(dict1) > 1:
        for i in list1:
            if 3 not in dict1[i+1]:
                dict1[i+1].append(s)

            else:
                del dict1[i+1]
                list1.remove(i)
            if s == 3:
                s = 1
            else:
                s += 1
        list1 = list1
    print u'最后留下是原来的号数为：',
    return dict1.keys()
print BaoShu(220)

# 老师的方法：
n = int(raw_input('input people number:'))
step = 1
out = 0
orderList = range(1,n+1)
while step:
    if len(orderList) == 1:
        print u'最后留下来的是%d号游戏者'%orderList[0]
        break
    out +=1
    if step> len(orderList):
        step = 1
    if out%3 == 0:
        outIndex = orderList[step-1]
        print orderList
        orderList.remove(orderList[step-1])
        print u"当前出局的是第%d号游戏者"%outIndex
        step -=1
    step += 1


# 20、 由单个字母组成的list， 从键盘读入两个整数m、 n（ n>m） ，
# 打印出list[m,n]之间的字母能组成的所有n-m+1位不同的字符串

list1 = ['a','b','c','d','e','f','g','h']
def DaYinZuHe(list1):
    m = int(raw_input(u'请输入组合开始的整数：'))
    n = int(raw_input(u'请输入组合结束的整数：'))
    if n<m:
        raise AttributeError(u'结束的整数必须大于开始的整数！')
    print u'由单个字母组成的list：',list1
    str1 = ''
    list2 = []
    list3 = []
    for i in list1[m:n]:
        for j in list1[m:n]:
            if i != j :
                str1 +=i + j
                list2.append(str1)
                list3 = list(str1)
                list3.remove(i)
                str1 = ''.join(list3)
        str1 = ''
    print u'list[%d,%d]之间的字母能组成的所有不同的字符串:'%(m,n)
    return list2
print DaYinZuHe(list1)


# 老师的方法：
# [a,b,c,d,e] 0,2
# a b c
# 3*2 = 6
# i = 0
# [a,b,c]1,2
# [b,c]
# [c,b]
# [a,b,c][a,c,b]
# i = 1
# [b,a,c]
# [b,a,c][b,c,a]
# i = 2
# [c,b,a][c,a,b]

def permutate(strList,low,high):
    global flag,start,end
    if flag:
        start = low
        end = high+1
        flag = 0
    if low == high:
        print ''.join(strList[start:end])
    else:
        i = low
        while i<= high:
            strList[low],strList[i]=strList[i],strList[low]
            permutate(strList,low+1,high)
            strList[low],strList[i]=strList[i],strList[low]
            i += 1
           #abc
           #a bc cb
            #b bc ca
            #c ba ab
flag = 1
start = 0
end = 0
permutate(['a','b','c','d','e'],0,2)


