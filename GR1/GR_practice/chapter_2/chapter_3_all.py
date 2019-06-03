#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 11:19
# @Author  : Lin
# @Site    : 
# @File    : chapter_3_all.py
# @Software: PyCharm
# 1、打印N，口，H图案
# 提示：
# 先再草稿纸上画画要打印的图案，注意观察横纵坐标的特点，从中找到解题的思路

# list1 = ['00000000000', '10000000001','10100000001', '10001000001', '10000010001', '10000000101','10000000001',]
# list2 = ['000000000', '111111111','100000001', '100000001','100000001','111111111']
# list3 = ['0000000','1000001','1000001','1111111','1000001','1000001']
#
# print u'N的图案：'
# for line1 in list1:
#     for a in line1:
#         if a == '0':
#             print ' ',
#         else:
#             print '*',
#     print
#
# print u'\n口的图案：'
# for line2 in list2:
#     for b in line2:
#         if b == '0':
#             print ' ',
#         else:
#             print '*',
#     print
#
# print u'\nH的图案：'
# for line3 in list3:
#     for c in line3:
#         if c == '0':
#             print ' ',
#         else:
#             print '*',
#     print


# 2、一个字符串中，分别输出奇数坐标字符或偶数坐标字符
# 要求：奇数坐标一行，偶数坐标一行

# str1 = 'abcdefghijklmn'
#
# def Str_str(str1):
#     '''
#     传入一个字符串，输出分别输出奇数坐标字符或偶数坐标字符
#     :param str1: 字符串
#     :return:为空
#     '''
#     dict1 = {}
#     dict2 = {}
#     for i,j in enumerate(str1):
#         if i == 0:
#            dict1[i] = j
#         elif i % 2 == 0:
#             dict1[i] = j
#         else:
#             dict2[i] = j
#     print u'奇数坐标字符：',dict2,u'\n偶数坐标字符：',dict1
# Str_str(str1)


# 3、统计字符串中的字母、数字、其他字符个数

# str1 = 'abcd123,456efg.?@#hijk789你好'
#
# def StrInta(str1):
#     '''
#     统计字符串中的字母、数字、其他字符个数
#     :param str1: 需要统计的字符串
#     :return:返回值为空
#     '''
#     list1 = []
#     list2 = []
#     list3 = []
#
#     for i in str1:
#         if i.isdigit():
#             list1.append(i)
#         elif i.isalpha():
#             list2.append(i)
#         else:
#             list3.append(i)
#     print u'数字的个数是%d个，分别为：'%len(list1),list1,\
#         u'\n字母的个数是%d个，分别为：'%len(list2),list2,\
#         u'\n其他字符的个数是%d个，分别为：'%len(list3),list3
# StrInta(str1)


# 4 、有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# list1 = [1,4,5,7,9,33,24,56,8,6,12]
# list1.sort()
# print u'排序好的数组：',list1
# int1 = int(raw_input(u'请输入一个数：'))
# list1.append(int1)
# list1.sort()
# print u'插入后的数组：',list1




# 5、统计名字列表中，各名字的首字母在名字列表中出现的次数

# name=['Aaron','Abner','BerAon','christcian','Earl','Geoff','Clare','Cdonis']
#
# def ShouMingzi(name):
#     '''
#     参数为名字列表，返回值为空，打印出各名字的首字母和在名字列表中出现的次数
#
#     '''
#     str1 = ''.join(name)
#     dict1 = {}
#     for i in range(len(name)):
#         sine = name[i][0]
#         dict1[sine] = ''
#     for key,value in dict1.items():
#         print key,str1.count(key)
#
# ShouMingzi(name)


# 6、字符替换
# 1）读入一个字符串
# 2）去掉字符串的前后空格
# 3）如果字符串包含数字则1替换成a，2替换成b，3替换成c，以此类推
# 4）将字符串使用空格进行切分，存到一个列表，然后使用*号连接，并输出
# 5）把这些功能封装到一个函数里面，把执行结果作为返回值

# def StrZfu():
#     '''
#     读入一个字符串;去掉字符串的前后空格;如果字符串包含数字则1替换成a，2替换成b，3替换成c，以此类推;
#     将字符串使用空格进行切分，存到一个列表，然后使用*号连接，并输出
#     :return:字符串空格以*为连接的字符串
#     '''
#     from string import maketrans
#     str1 = '123456789'
#     str2 = 'abcdefghi'
#     # strc = 'shdhj123sds2'
#     strb = maketrans(str1,str2)
#     stra = raw_input(u'请输入一个字符串，按回车键结束：');
#     strd = stra.translate(strb)
#     strd = strd.strip(' ')
#     list1 = strd.split(' ')
#     return '*'.join(list1)
#
# print StrZfu()





# 7、找出字符串中出现次数最多的字符，并输出其出现的位置

# str1 = 'abcdeffffffgsdefgdfd'
#
# def ZiFu(str1):
#     '''
#     输入的参数为一句字符串，而后输出出现字次最多的字符和其位置
#     :param str1: 字符串
#     :return:为空
#     '''
#     dict1 = {}
#     for i in str1:
#         if dict1.has_key(i[0]):
#             dict1[i[0]] += 1
#         else:
#             dict1[i[0]] =1
#
#     for key,value in dict1.items():
#         if value == max(dict1.values()):
#             str2 = key
#
#     print u'出现次数最多的字符：',str2,u'\n出现的位置索引分别是：'
#     for j in range(len(str1)):
#         if str1[j] == str2:
#             print j,
# ZiFu(str1)






# 8、找出一段句子中最长的单词及其索引位置，以字典返回

# def ZiDian(str1):
#     list1 = str1.split(' ')
#     dict1 = {}
#     str1 = list1[0]
#     for i in range(len(list1)):
#         if len(list1[i]) >  len(str1):
#             str1 = list1[i]
#             j = i
#     dict1[j] = str1
#     print dict1
#
# str1 = raw_input(u'请输入一段句子，按回车键结束：')
# ZiDian(str1)




# 9、字母游戏
# “Pig Latin”是一个英语儿童文字改写游戏，整个游戏遵从下述规则：
# (1). 元音字母是‘a’、‘e’、‘i’、‘o’、‘u’。字母‘y’在不是第一个字母的情况下，
# 也被视作元音字母。其他字母均为辅音字母。例如，单词“yearly”有三个元音字母（分别为
# ‘e’、‘a’和最后一个‘y’）和三个辅音字母（第一个‘y’、‘r’和‘l’）。
# (2). 如果英文单词以元音字母开始，则在单词末尾加入“hay”后得到“Pig Latin”对应单词。
# 例如，“ask”变为“askhay”，“use”变为“usehay”。（同上）
# (3). 如果英文单词以‘q’字母开始，并且后面有个字母‘u’，将“qu”移动到单词末尾加
# 入“ay”后得到“Pig Latin”对应单词。例如，“quiet”变为“ietquay”，“quay”变为“ayquay”。
# (4). 如果英文单词以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”后得
# 到“Pig Latin”对应单词。例如，“tomato”变为“omatotay”， “school” 变为
# “oolschay”，“you” 变为“ouyay”，“my” 变为“ymay ”，“ssssh” 变为“sssshay”。
# (5). 如果英文单词中有大写字母，必须所有字母均转换为小写。
# 输入格式:
# 一系列单词，单词之间使用空格分隔。
# 输出格式：
# 按照以上规则转化每个单词，单词之间使用空格分隔。
# 输入样例：
# Welcome to the Python world Are you ready
# 输出样例：
# elcomeway otay ethay ythonpay orldway arehay ouyay eadyray


# str1 = 'Welcome to the Python world Are you ready'
# str1 = str1.lower()
# list1 = str1.split(' ')
# str3 = ''
# for i in range(len(list1)):
#     s = 0
#     if list1[i][0]  in ('a','e','i','o','u'):
#          list1[i] = list1[i] + 'hay'
#     elif list1[i][0] == 'q' and list1[i][1] == 'u':
#         list4 = list(list1[i])
#         del list4[:2]
#         list1[i] = ''.join(list4)
#         list1[i] = list1[i] + 'quay'
#     elif list1[i][0] not in ('a','e','i','o','u'):
#         for j in range(len(list1[i])):
#             if list1[i][j]  in ('a','e','i','o','u'):
#                 break
#             else:
#                 list4 = list(list1[i])
#                 s += 1
#             str3 = list1[i][:s]
#         list4 = list(list1[i])
#         del list4[:s]
#         list1[i] = ''.join(list4)
#         list1[i] = list1[i] + str3 + 'ay'
#
#
# str3 = ' '.join(list1)
# print str3









# 10、实现字符串的upper、lower以及swapcase方法

# def StringUpper(str1):
#     '''
#     StringUpper(str1)将字符串中的小写字母转为大写字母
#     :param str1:需要转换的字符串
#     :return:返回值为空
#     '''
#     str1 = list(str1)
#     list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
#              'p','q','r','s','t','u','v','w','x','y','z']
#     list2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
#              'P','Q','R','S','T','U','V','W','X','Y','Z']
#     for i in range(len(str1)):
#         for j in range(len(list1)):
#             if str1[i]==list1[j]:
#                 str1[i] = list2[j]
#                 break
#     for n in str1:
#         print n,
#
# def StringLower(str2):
#     '''
#     StringLower(str1)转换字符串中所有大写字符为小写
#     :param str1:需要转换的字符串
#     :return:返回值为空
#     '''
#     str2 = list(str2)
#     list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
#              'p','q','r','s','t','u','v','w','x','y','z']
#     list2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
#              'P','Q','R','S','T','U','V','W','X','Y','Z']
#     for i in range(len(str2)):
#         for j in range(len(list2)):
#             if str2[i]==list2[j]:
#                 str2[i] = list1[j]
#                 break
#     for n in str2:
#         print n,
#
# def StringSwapcase(str3):
#     '''
#     StringSwapcase(str3) 方法用于对字符串的大小写字母进行转换
#     :param str1:需要转换的字符串
#     :return:返回值为空
#     '''
#     str3 = list(str3)
#     list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
#              'p','q','r','s','t','u','v','w','x','y','z']
#     list2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
#              'P','Q','R','S','T','U','V','W','X','Y','Z']
#     for i in range(len(str3)):
#         for j in range(len(list2)):
#             if str3[i]==list2[j]:
#                 str3[i] = list1[j]
#                 break
#             elif str3[i]==list1[j]:
#                 str3[i] = list2[j]
#                 break
#     for n in str3:
#         print n,
# #
# str1 = "this is string example....wow!!!";
# str2 = 'my name is @Lin Chunlian @#'
# str3 = 'MY NAME IS L$$IN Chunlian @#!'
# StringUpper(str2)
# print '\n'
# StringLower(str3)
# print '\n'
# StringSwapcase(str3)





# 11、实现字符串的find方法
# find() 方法检测字符串中是否包含子字符串 str ，
# 如果指定 beg（开始） 和 end（结束） 范围，
# 则检查是否包含在指定范围内，
# 如果包含子字符串返回开始的索引值，否则返回-1。

# def StringFind(str,beg=0,end=len(str)):




# 12、实现字符串的isalpha方法
#  isalpha() 方法检测字符串是否只由字母组成。





# 13、实现字符串的isdigit方法
# isdigit() 方法检测字符串是否只由数字组成。




# 14、实现字符串的isalnum方法
# isalnum() 方法检测字符串是否由字母和数字组成。




# 15、实现字符串的join方法
# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。




# 16、实现字符串的replace方法
#  replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，
# 如果指定第三个参数max，则替换不超过 max 次。






# 17、实现字符串的split方法
#split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串






# 18、实现字符串的strip方法
# 删除 string 字符串末尾的指定字符（默认为空格）.




# 19、报数问题：有n个人围成一圈，顺序排号。从第一个人开始报数
# （从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位

# 20、由单个字母组成的list，从键盘读入两个整数m、n（n>m），打印
# 出list[m,n]之间的字母能组成的所有n-m+1位不同的字符串。



