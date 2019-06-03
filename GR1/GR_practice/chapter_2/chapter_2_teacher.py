# encoding=utf-8
#1、count()>1
#定义一个方法用于去重
# 方法1：
# def listP(listOld):
#     for i in listOld:
#         if listOld.count(i)>1:
#             listOld.remove(i)
#     return listOld
#
# list1 = [1,2,3,3,4,6,4,7,1]
# print list1
# print listP(list1)

# 方法2# dict key的唯一性
# def listP(listOld):
#     value = 1
#     listNew = []
#     dict1 = {}
#     for i in listOld:
#         dict1[i] = value
#     for k in dict1.keys():
#         listNew.append(k)
#     return listNew

# 方法3--set的不能重复
# def listP(listOld):
#     tmpList = list(set(listOld))
#     return tmpList
#
# print list1
# print listP(list1)
# 2.成绩等级判断
# 利用条件运算符的嵌套来完成此题： 学习成绩>=90分的同学用A表示，
# 60-89分之间的用B表示， 60分以下的用C表示
# 3.实现数学中多项式求和公式的打印
# 比如： a6x^6 + a5x^5 + a4x^4 + a3x^3 + a2x^2 + a1x^1 + a0
# 4.统计名字列表中， 各名字的首字母在名字列表中出现的次数
# 5.输入三个数， 判断是否能构成三角形
# 能构成三角形三边关系：
# 三边都大于零
# 两边之和大于第三边， 两边之差小于第三边
# 6.实现字典的fromkeys方法
# 例如：
# seq = ('name', 'age', 'sex')
# dict = dict.fromkeys(seq, 10)
# print "New Dictionary : %s" % str(dict)
# 结果： New Dictionary : {'age': 10, 'name': 10, 'sex': 10}
# 思路：1\定义一个字典，2、遍历序列，每一个值作为key.,3、把key和value赋值给字典
# encoding=utf-8

# def myfromkeys(seq,value=None):
#     """
#
#     :rtype : object
#     """
#     seqDict = {}
#     for i in seq:
#         seqDict[i] = value
#     return seqDict
#
# if __name__ == '__main__':
#     seq = [1,'a',4,'2',5]
#     resDict = myfromkeys(seq, 1)
#     print resDict


# 7.键盘读入一字符串， 逆序输出
# 1、切片，str1[::-1],2、列表的reverse()

# def invertedOrder(ss):
#     c = []
#     n = len(ss)
#     for i in range(n):
#         c.append(ss[i])
#     c.reverse()
#     return ''.join(c)
# s = raw_input(u'请输入字符串')
# print invertedOrder(s)

# 8.读入一个整数n， 输出n的阶乘
# n! = 1*2*3*..*n
# n!= n*(n-1)!
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return factorial(n-1)*n
#
# n = int(raw_input('please input a interge:'))
# print factorial(n)


# 9.打印1/2, 1/3, 1/4,….1/10
#1\遍历的方式打印

# n = 10
# for i in range(2,n+1):
#     if i == n:
#         print '1/%s'%i
#     else:
#         print '1/%s,'%i,


# 10.写一个函数实现一个数学公式
# 11.输入数字a， n， 如a， 4，
# 则打印a+aa+aaa+aaaa之和
# 12.求100个随机数之和， 随机数要求为0—9的整数
# 13.要求在屏幕上分别显求1到100之间奇数之和与偶数之和
# 1、遍历1-100；2、判断是奇数还是偶数；3、把数值加到对应的和里面

# oddNum = 0
# evenNum = 0
# for i in range(1,100):
#     if i%2 == 0:
#         evenNum += i
#     else:
#         oddNum += i
# print oddNum
# print evenNum

# 14.输入10个数， 并显示最大的数与最小的数
# 1、生成一个数字列表；2、针对数字列表，进行排序

# numList = raw_input('input 10 num:').split(',')
# numList = map(int,numList)
#
# numList.sort()
# print u'最小：',numList[0]
# print u'最大：',numList[-1]


# 15.给一个不多于5位的正整数， 要求： 一、 求它是几位数，
#  二、 逆序打印出各位数字。
# 1、使用list的reverse方法，达到逆序的目的

# num = raw_input('input num:')
# print len(num)
# numList = list(num)
# numList.reverse()
# print ''.join(numList)

# 16.求所有的水仙花数
# 1、遍历所有的三位数；2、计算abc同a^3+b^3+c^3是否相等
# import math
#
#
# def myPow(n):
#     return int(math.pow(int(n),3))
# for i in range(100,1000):
#     res = sum(map(myPow,list(str(i))))#把数值当做字符串转换成列表来进行计算，把百位数和个位数分开
#     if res == i:
#         print i




# 17.编程求s=1!+2!+3!+…..+n!
# 1、遍历1-n；2、针对每次遍历的值求阶乘，求和

# def func(n):
#     ret = 1
#     for i in xrange(1,n+1):
#         ret *=i
#     return ret
#
# n = int(raw_input('please input a num:'))
# sum = 0
# for i in range(1,n+1):
#     sum += func(i)
# print sum


# 18.钞票换硬币
# 把一元钞票换成一分、 二分、 五分硬币（ 每种至少一枚） ，
#  有多种换法， 分别有哪些？
# 1、1元=100分，100分-8分=92；假设全部是1分--92个，全是2分--46，全是5分--18个
# penny = 1
# twopenny = 2
# fivepenny = 5
# smacker = 100
# total = 0
# print u'1分\t2分\t5分'
# for p in range(0,93):
#     for t in range(0,47):
#         for f in range(0,19):
#             if p + t*twopenny + f*fivepenny +penny + twopenny + fivepenny == smacker:
#                 print str(p)+'\t'+str(t)+'\t'+str(f)
#                 total += 1
#
# print u'一共有%d种换法'%total

# 19.自己实现在一句话中查找某个单词的算法， 存在返回索引号，
# 否则返回False
def indexWord(wordStr,word):
    dictWord = {}
    dictWord[word]=[]
    listWord = wordStr.split(' ')
    for i in range(len(listWord)):
        if listWord[i] == word:
            dictWord[word].append(i)
    if len(dictWord[word]) > 0:
        return dictWord[word]
    return False

words ='''Youth is not a time of life; it is a state of mind;
  it is not a matter of rosy cheeks, red lips and supple knees;
  it is a matter of the will, a quality of the imagination,
  a vigor of the emotions;
  it is the freshness of the deep springs of life.'''
print indexWord(words,'matter')




# 20.读入一个十进制整数， 实现十进制转二进制算法将其转成二进制数
# 要求： 不能使用现成进制转换函数， 自己写代码实现
# num = int(raw_input('please input a num:'))
#
# list1 = []
# if num <= 1:
#     print u'二进制：%d'%num
# else:
#     while num > 1:
#         list1.append(str(num%2))
#         num /=2
#     list1.append(str(num))
#     list1.reverse()
#     print u'二进制：',
#     octNum = ''.join(list1)
#     print octNum
