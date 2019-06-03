# encoding=utf-8
# 11、返回列表中第二大元素
list1 = [2,1,4,6,3,8,34,911,34,19,20,20]

def printDiEr(list):
    lista = []
    for i in list:
        if i not in lista:
            lista.append(i)
    lista.sort()
    return lista[-2]
print printDiEr(list1)

# 老师的方法：排序--取倒数第二个元素
list1 = [1,2,34,23,45]
list2 = list(set(list1))
list2.sort()
print list2[-2]


# 12、已知一字符串列表list1 = ['a','b','c','d', 'e', 'f', 'g']，
# 对序列的任一子序列list1[start, end]中的元素进行排列组合，
# 有多少种不同的组合， 请分别输出。 （ start >= 0, end <len(list1)）

list1 = ['a','b','c','d', 'e', 'f', 'g']
def PaiLieZuHe(list):
    list2 = [[n,m] for n in list for m in list if n!=m ]
    print list2

PaiLieZuHe(list1[1:5])

# 老师的方法：
# list1[2:6] = ['c','d','e','f']
# 4*3*2*1=24
# 算法：
# 1、每个值都可以替换第一个值
# 2、列表中只有一个元素时，是不可以替换，可以直接返回

def permutate(liststr,low,high):
    if low ==  high:
        print ''.join(liststr)
    else:
        i = low
        while i <= high:
            liststr[low],liststr[i] = liststr[i],liststr[low]
            permutate(liststr,low+1,high)
            liststr[low],liststr[i] = liststr[i],liststr[low]
            i = i+1
def main(resStr,low,high):
    if low >0 and high <len(resStr) and low <= high:
        liststr = resStr[low:high]
    else:
        print u'输入有误'
        return -1
    permutate(liststr,0,len(liststr)-1)

list1 = ['a','b','c','d', 'e', 'f', 'g']
start = 2
end = 6
main(list1,start,end)



# 13、判断一个字符串是否为回文字符串
# 所谓回文字符串， 就是一个字符串， 从左到右读和从右到左读是完全一样的。
# 比如 "level" 、 “aaabbaaa”
str1 = 'levqqel'
str2 = 'aaabbaaa'

def pDuan(str):
    s = len(str)
    n = s/2
    if s%2==0:
        if str[:n]==str[:n-1:-1]:
            return True
        else:
            return False
    else:
        if str[:n]==str[:n:-1]:
            return True
        else:
            return False

print pDuan(str1)
print pDuan(str2)

# 老师的方法：
# 算法：比较正序和逆序是否相等
def checkStr(n):
    if len(n)>=2 and n[:] == n[::-1]:
        return True
    else:
        return False
print checkStr('abc')
print checkStr('aba')




# 14、实现合并同类型的有序列表算法， 要求不能有重复元素

lista = ['1','2','3','4','5']
listb = ['5','6','7','8']
list1 = [1,2,3,4,5]
list2 = [5,6,7,8]


def heBing(listone,listtwo):
    listsine = listone + listtwo
    lists = []
    # listt = []
    for i in listsine:
        if isinstance(i,type(listsine[0])):
            if i not in lists:
                lists.append(i)
        else:
            # listt.append(i)
            print u'输入的列表不是同类型的'
            exit()
    print lists

heBing(lista,listb)

# 老师的方法：先把列表合并，然后再去重，最后再排序
def joinSep(seq1,seq2,*args):
    jSep = seq1 + seq2
    if len(args)>0:
        for i in args:
            jSep += i
        temSep = list(set(jSep))
        temSep.sort()

        if isinstance(jSep,tuple):
            return tuple(temSep)
        elif isinstance(jSep,list):
            return list(temSep)
        elif isinstance(jSep,str):
            return ''.join(temSep)
print joinSep([1,2,3],[2,3,4],[3,4,5])
print joinSep('abc','cde','xyz')


# 15、有4个圆锥塔， 圆心分别为（ 20, 20） 、 （ -20, 20） 、
#  （ -20, -20） 、 （ 20， -20） ，圆半径为10m，
# 见下图。 这4个塔的高度为100m， 塔以外无建筑物。 今输入任一点坐标，
# 求该点的建筑高度（ 塔外的高度为0） ， 结果不需要特别精确，
#  只需要考虑坐标为整数的情况
import math
def JianZhu(x,y):
    if x>0 and y>0:
        l = math.sqrt((x-20)*(x-20)+(y-20)*(y-20))
    elif x<0 and y>0:
        l = math.sqrt((x+20)*(x+20)+(y-20)*(y-20))
    elif x<0 and y<0:
        l = math.sqrt((x+20)*(x+20)+(y+20)*(y+20))
    elif x>0 and y<0:
        l = math.sqrt((x-20)*(x-20)+(y+20)*(y+20))
    if l > 10:
        print u'该点的建筑高度为：0'
    else:
        print u'该点的建筑高度为：100'

JianZhu(22,22)


# 老师的方法：
from math import sqrt
def heigh(x,y):
    r =10
    towerHigh =100
    poinToCenter = abs((abs(x)-20)**2+abs(abs(y)-20)**2)
    print 'poinToCenter=',poinToCenter
    if poinToCenter > r**2:
        return 0
    pointHight = (r-sqrt(poinToCenter))*towerHigh/r
    print 'point hight:',pointHight
    return pointHight
print u'请输入坐标：'
x,y=0,0
x = float(raw_input('x='))
y = float(raw_input('y='))

res = heigh(x,y)
print u'高度是：',res



# 16、一个数如果恰好等于它的因子之和， 这个数就称为完数，
# 例如6的因子为1,2,3， 而6=1+2+3，
# 因此6是完数， 编程找出1000之内的所有完数，
# 并按6 its factors are 1,2,3这样的格式输出

# 因数包括这个数本身而因子不包括,如：比如15的因子是1,3,5 　　
# 而因数为1,3,5,15.完数是指此数的所有因子之和等于此数,例如：28=1+2+4+7+14. 6=1+2+3，

for i in xrange(2,1001):
    s = 0
    sine = ''
    for j in xrange(1,i):
        if i%j==0:
            s += j
            sine += str(j)+','
    if s == i:
        print i,u'its factors are',sine


# 17、使用二分法实现在一个有序列表中查找指定的元素

list1 = [1,4,45,33,5,23,8,9,67,79]

def ErFen(list,n):
    list.sort()
    print list
    f = 0
    e = f+len(list)
    m = (f+e)/2
    while n in list:
        if n == list[m]:
            print n,u'在列表',list,u'的位置是',m
            exit()
        elif n > list[m]:
            m = len(list[m:e])/2
        elif n < list[m]:
            m = len(list[f:m])/2
    print u'没有在列表中找到',n

ErFen(list1,23)

# 老师的方法：
def binarySearch(find,list1):
    low = 0
    high = len(list1)
    while low <=high:
        mid = (low+high)/2
        if list1[mid] == find:
            return mid
        elif list1[mid]>find:
            high = mid-1
        else:
            low = mid +1
    return -1

list1 = [238,343,454,56,67,232,565,98]
list1.sort()
print binarySearch(98,list1)


# 18、分离list1与list2中相同部分与不同部分
list1 = [1,3,45,67,3,5,7]
list2 = [1,3,56,7,9,34,23]
list3 = []
list4 = []
for i in list1:
    if i not in list3:
        list3.append(i)
for i in list2:
    if i not in list4:
        list4.append(i)
listc = [x for x in list3 if x in list4]
listd = [x for x in list3 if x not in list4]+[x for x in list4 if x not in list3]
print u'list1',list1,u'和list2：',list2
print u'相同的部分为：',listc
print u'不相同的部分为：',listd

# 老师的方法：
def listSplit(list1,list2):
    sameList = []
    diffList = []
    for i in list1:
        if i in list2:
            sameList.append(i)
        else:
            diffList.append(i)
    for j in list2:
        if j not in sameList and j not in diffList:
            diffList.append(j)
    print 'diff:',diffList
    print 'same:',sameList

list1 = [1,2,3,4]
list2 = [3,4,5,6]
listSplit(list1,list2)



# 19、找出一个多维数组的鞍点， 即该位置上的元素在该行上最大，
# 在该列上最小， 也可能没有鞍点

list1 = [[1,17,3,9],
         [2,16,4,7],
         [3,18,1,17],
         [4,21,2,8]]

for i in xrange(len(list1)):
    sine = list1[i][0]
    for j in xrange(len(list1[i])):
        if list1[i][j] >= sine:
            sine = list1[i][j]
            s = j
            h = i
    for n in xrange(len(list1)):
        if list1[n][s] < sine:
            break
    else:
        print u'鞍点是',sine,u'在',s,u'列',h,u'行'
        break
else:
    print u'不存在鞍点'

# 老师的方法：算法：1、求行最大的值，
# 2、判断是否是列上最小

def func(matrix):
    flag = 0
    for i,row in enumerate(matrix):
        maxNum = max(row)
        index = row.index(maxNum)
        for j in xrange(len(matrix)):
            if maxNum >= matrix[j][index] and i != j:
                break
        else:
            flag += 1
            print u'第%d行第%d列的%d是鞍点'%(i+1,index+1,maxNum)
        if flag == 0:
            print u'矩阵无鞍点'

matrix = [[8,1,11],[9,5,12],[10,9,23]]
func(matrix)



# 20、写一个函数， 识别输入字符串是否是符合 python 语法的变量名


str1 = '_a$nd'
def bianLian(str):
    list1 = ['and','assert','break','class','coutinue','def','del','elif','else','except',
             'exec','finally','from','for','global','if','import','in','is','lambda','not',
             'or','pass','print','raise','return','try','while','with','yield']
    if str in list1:
        return u'该变量为关键字'
    if str[0].isalpha() or str[0] == '_':
        for i in str:
            if i.isalnum() or i=='_':
                continue
            else:
               return u'不符合 python 语法的变量名'
        return u'符合 python 语法的变量名'
    else:
        return u'不符合 python 语法的变量名'
print bianLian('3_gh')












