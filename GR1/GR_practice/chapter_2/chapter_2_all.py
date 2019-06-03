# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2017/3/30 9:58
# # @Author  : Lin
# # @Site    :
# # @File    : chapter_2_all.py
# # @Software: PyCharm
#
#
# # 1.使用尽可能多的方法实现list去重
#
# import itertools
#
# list1 = [1,7,3,8,3,2,5,6,1,2,3,4]
# list2 = ['a','b','c','d','d','a','b','f']
# list3 = []
# list4 = [1,7,3,8,3,2,5,6,1,2,3,4]
# dict1 = {}
#
# for i in list1:
#     if i not in list3:
#         list3.append(i)
# print list3
#
# list5 = list(set(list1))
# print list5
#
#
# for i in list1:
#     while list1.count(i)>1:
#         del list1[list1.index(i)]
# print list1
#
# list2.sort()
# s = itertools.groupby(list2)
#
# for a,b in s:
#     print a,
#
# c = lambda x,y:x if y in x else x + [y]
# print '\n',reduce(c,[[],]+list4)
#
#
# # 2.成绩等级判断
# # 利用条件运算符的嵌套来完成此题： 学习成绩>=90分的同学用A表示，
# # 60-89分之间的用B表示， 60分以下的用C表示
# while True:
#     try:
#         grade = int(raw_input(u'请输入要查询等级的成绩，按回车键结束：'))
#         if grade >= 90:
#             print grade,u'分，的等级为A'
#         elif grade >= 60 and grade <= 89:
#             print grade,u'分，的等级为B'
#         else:
#             print grade,u'分，的等级为c'
#     except ValueError:
#         print u'输入有误，请重新输入'
#
# # 3.实现数学中多项式求和公式的打印
# # 比如： a6x^6 + a5x^5 + a4x^4 + a3x^3 + a2x^2 + a1x^1 + a0
#
# i = 6
# while i >= 0:
#     if i != 0:
#         print u'a%d'%i+'x^%d'%i,
#         print '+',
#     else:
#         print u'a0'
#     i -=1
#
#
#
# # 4.统计名字列表中， 各名字的首字母在名字列表中出现的次数
#
# name=['foster','foe','lily','mickel','live','moon','ruby','cindy','miya']
# dict1 = {}
#
# for i in name:
#     if dict1.has_key(i[0]):
#         dict1[i[0]] += 1
#     else:
#         dict1[i[0]] = 1
#
# print dict1
#
# for key,value in dict1.items():
#     print u'以姓名为字母',key,u'开头的有：',value
#
#
#
# # 5.输入三个数， 判断是否能构成三角形
# # 能构成三角形三边关系：
# # 三边都大于零
# # 两边之和大于第三边， 两边之差小于第三边
#
# while True:
#     try:
#         a = int(raw_input(u'请输入第一个数来判断是否能构成三角形，按回车键结束：'))
#         b = int(raw_input(u'请输入第二个数来判断是否能构成三角形，按回车键结束：'))
#         c = int(raw_input(u'请输入第三个数来判断是否能构成三角形，按回车键结束：'))
#         if a > 0 and b > 0 and c > 0:
#
#             if a+b>c and a+c>b and b+c>a and a-b<c and a-c<b and b-c<a :
#                 print a,b,c,u'能构成三角形'
#             else:
#                 print a,b,c,u'不能构成三角形'
#         else:
#             print u'请输入的三个数都是大于0的数'
#             continue
#     except ValueError:
#         print u'输入有误，请输入整数！'
#
#
# # 6.实现字典的fromkeys方法
# # 例如：
# # seq = ('name', 'age', 'sex')
# # dict = dict.fromkeys(seq, 10)
# # print "New Dictionary : %s" % str(dict)
# # 结果： New Dictionary : {'age': 10, 'name': 10, 'sex': 10}
#
# def Dict_Fromkey(seq,n):
#     '''
#     传人一个元组，和一个整数值，打印出元组的元素为字典的主键，传入的值为字典的值
#     seq：元组
#     n:字典的值
#     return:返回字典
#     '''
#     if not isinstance(seq,tuple):
#         print u'传入的参数有误'
#     else:
#         dict1 = {}
#         for i in seq:
#             dict1[i] = n
#         return dict1
#
# seq = ('name', 'age', 'sex')
# print 'New Dictionary :',Dict_Fromkey(seq,20)
#
#
# # 7.键盘读入一字符串， 逆序输出
#
# str1 = str(raw_input(u'请输入一字符串，按回车键结束：'))
#
# def Str_Reverse1(string):
#     '''
#     使用切片的倒序排列输出
#     :param string: 需要倒序输出的字符串
#     :return:none
#     '''
#     return string[::-1]
#
#
# def Str_Reverse2(string):
#     n = 1
#     for i in range(len(string)):
#         print string[len(string)-n],
#         n +=1
#     return ''
#
#
# def Str_Reverse3(string):
#     m = 0
#     while m < len(string):
#         m += 1
#         print string[len(string)-m],
#     return  ''
#
#
# def Str_Reverse4(string):
#     return  ''.join(string[i] for i in range(len(string)-1, -1, -1))
#
#
# def Str_Reverse5(string):
#     if len(string) <= 1:
#         return string
#     return Str_Reverse5(string[1:]) + string[0]
#
#
# def Str_Reverse6(string):
#     list1 = []
#     for i in string:
#         list1.append(i)
#     list1.reverse()
#     print list1
#     return ''
#
# print Str_Reverse1(str1)
# print Str_Reverse2(str1)
# print Str_Reverse3(str1)
# print Str_Reverse4(str1)
# print Str_Reverse5(str1)
# print Str_Reverse6(str1)
#
# # 8.读入一个整数n， 输出n的阶乘
#
# while True:
#     try:
#         s = 1
#         n = int(raw_input(u'请输入一个整数，按回车键结束：'))
#         if n == -1:
#             print u'阶乘是0'
#         elif n >= 1:
#             for i in range(1,n+1):
#                 s *= i
#                 print i,
#                 if i != n:
#                     print '*',
#             print u'的阶乘是',s
#         else:
#             print u'你输入的数值没有阶乘，请重新输入！'
#     except ValueError:
#         print u'输入有误，请输入整数'
#
# # 9.打印1/2, 1/3, 1/4,….1/10
#
# for i in range(1,11):
#     print u'1\\%d,'%i,
#
#
# # 10.写一个函数实现一个数学公式
#
# def Triangle_Area(bottom,height):
#     '''
#     计算三角形的面积，并打印出结果
#     :param bottom: 代表三角形的底
#     :param height: 代表三角形的高
#     :return:为空
#     '''
#     area = (bottom*height)/2.0
#     print u'三角形的面积等于：',area
#     return ''
# Triangle_Area(27,3)
#
#
#
# # 11.输入数字a， n， 如a， 4， 则打印a+aa+aaa+aaaa之和
#
# def Stack_Ride(a,n):
#     '''
#     获取用户输入的a,n，，打印出a+aa+aaa+aaaa+....+na的和
#     :param a: 需要进行相加的数值
#     :param n: 相加的次数和a的显示次数
#     :return:为空
#     '''
#     s = 0
#     for i in range(1,n+1):
#         print str(a)*i,
#         s += int(str(a)*i)
#         if i < n:
#             print u'+',
#     print '=',s
#
# while True:
#     try:
#         a = int(raw_input(u'请输入a的值，按回车键结束：'))
#         n = int(raw_input(u'请输入n的值，按回车键结束：'))
#         Stack_Ride(a,n)
#     except ValueError:
#         print u'输入有误，请输入整数！'
#
#
# # 12.求100个随机数之和， 随机数要求为0—9的整数
#
# import random
#
# s = 0
# n = 0
# for i in range(100):
#     s += random.randint(0,9)
#     n +=1
# print u'随机数为0—9中的%d个数的和是'%n,s
#
#
# # 13.要求在屏幕上分别显求1到100之间奇数之和与偶数之和
#
# c = 0
# s = 0
# for i in range(1,101):
#     if i % 2 != 0:
#         c += i
#     elif i % 2 == 0:
#         s += i
# print u'1-100之间的奇数之和是：',s
# print u'1-100之间的偶数之和是：',c
#
#
# # 14.输入10个数， 并显示最大的数与最小的数
#
# def Several_Number(n):
#     '''
#     用户输入n个数，显示输入n个数中最大和最小的数
#     :param n: 键入的多少个数
#     :return:为空
#     '''
#     lista = []
#     for i in range(n):
#         a  = int(raw_input(u'请输入数值，按回车键结束：'))
#         lista.append(a)
#
#     print u'输入的数值中，最大数是：',max(lista)
#     print u'输入的数值中，最小数是：',min(lista)
#
# Several_Number(10)
#
#
# # 15.给一个不多于5位的正整数， 要求： 一、 求它是几位数， 二、 逆序打印出各位数字。
#
# while True:
#     try:
#         a = int(raw_input(u'请输入不多于5位的正整数,按回车键结束：'))
#         if a / 100000 != 0:
#             continue
#         else:
#             print u'输入的数值是%d位数'%len(str(a))
#             print u'逆序显示你输入的数值是：',str(a)[::-1]
#     except ValueError:
#         print u'输入有误，请重新输入！'
#
#
# # 16.求所有的水仙花数
#
# for i in range(100,1000):
#     a = i / 100
#     b = i /10 % 10
#     c = i %10
#     if i == a**3 + b**3 +c**3:
#         print i
#
#
#
#
#
# # 17.编程求s=1!+2!+3!+…..+n!
#
# while True:
#     try:
#         a = int(raw_input(u'请输入1!+2!+3!+…..+n!的n值，按回车键结束：'))
#         s = 1
#         b = 0
#         if a > 0:
#             for i in range(1,a+1):
#                 for n in (1,i):
#                     s *= n
#                 b += s
#             print u'1!+…+…..+%d!='%a,b
#         else:
#             print u'输入有误，请输入大于0的正整数！'
#             continue
#     except ValueError:
#         print u'输入有误，请输入正整数！'

#
# # 18.钞票换硬币
# # 把一元钞票换成一分、 二分、 五分硬币（ 每种至少一枚） ， 有多种换法， 分别有哪些？
#
# a = 0
# print u'换法如下：'
# for i in range(1,93):
#     for n in range(93-i):
#         for s in range(93-n-i):
#             if (i*1 + 2*n + 5*s) == 92:
#                 a +=1
#                 print s+1,u'个五分',n+1,u'个二分',i+1,u'个一分'
#             elif (i*1 + 5*n + 2*s) == 92:
#                 a +=1
#                 print n+1,u'个五分',s+1,u'个二分',i+1,u'个一分'
#             elif (i*2 + 1*n + 5*s) == 92:
#                 a +=1
#                 print s+1,u'个五分',i+1,u'个二分',n+1,u'个一分'
#             elif (i*2 + 5*n + 1*s) == 92:
#                 a +=1
#                 print n+1,u'个五分',i+1,u'个二分',s+1,u'个一分'
#             elif (i*5 + 1*n + 2*s) == 92:
#                 a +=1
#                 print i+1,u'个五分',s+1,u'个二分',n+1,u'个一分'
#             elif (i*5 + 2*n + 1*s) == 92:
#                 a +=1
#                 print i+1,u'个五分',n+1,u'个二分',s+1,u'个一分'
# print u'共有%d种换法'%a

#
# # 19.自己实现在一句话中查找某个单词的算法， 存在返回索引号， 否则返回False
#
# a = raw_input(u'请输入一句英文，按回车键结束：')
# b = raw_input(u'请输入你要查找的单词，按回车键结束：')
# list1 = []
# list1 = a.split(' ')
# i = 0
# c = True
# while c:
#     for j in list1:
#         i += 1
#         if j == b:
#             print u'你找的单词是%s,它是句子中第%d个单词'%(j,i)
#         else:
#             c = False
#             print False
# def StrSuan(a,b):
#     '''
#    在一句话中查找某个单词， 存在返回索引号， 否则返回False
#     :param a: 用户输入的一句话
#     :param b: 要查找的单词
#     :return:查找的单词存在返回索引号，不存在，返回False
#     '''
#     c = 0
#     s = a.split(' ')
#     for i in s:
#         c += 1
#         if b == i:
#             #print i,u'是第%d个单词'%c
#             return c
#     else:
#         return False
#
# a = raw_input(u'请输入一句英文，按回车键结束：')
# b = raw_input(u'请输入你要查找的单词：')
# print StrSuan(a,b)
#
#
#
# # 20.读入一个十进制整数， 实现十进制转二进制算法将其转成二进制数
# # 要求： 不能使用现成进制转换函数， 自己写代码实现

# a = int(raw_input(u'请输入一个十进制的整数，按回车键结束：'))
# list1 = []
# while True:
#     y = a % 2
#     a /= 2
#     if a == 0:
#         break
#     else:
#         list1.append(y)
# list1.append(y)
# list1.reverse()
# print u'转换后的二进制为：'
# for i in list1:
#     print i,
