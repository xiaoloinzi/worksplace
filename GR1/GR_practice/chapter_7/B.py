# encoding=utf-8
import random
# import Section_07_all
#
#
# def ride(x,y):
#    return Section_07_all.division(x,y)
# print ride(6,3)
# print Section_07_all.add(1,2)


# tuple1 = (1,2)
# del tuple1[1]
# print tuple1
# def RealiZationreplace(stru,oldstr,newstr,num= 0):
#     start = 0
#     strc = ''
#     if not isinstance(oldstr,str):
#         raise TypeError(u'被替换的子字符串必须是字符串类型')
#     end = len(oldstr)
#     if not isinstance(newstr,str):
#         raise TypeError(u'要替换对象不是字符串类型')
#     if not isinstance(num,int):
#         raise TypeError(u'替换参数需要是一个整数 ')
#     if oldstr not in stru or num == 0 or num < 0:
#         return stru
#     if num > stru.count(oldstr):
#         num = stru.count(oldstr)
#     while num != 0:
#         if stru[start:end] == oldstr:
#             strc += newstr
#             start +=len(oldstr)
#             end +=len(oldstr)
#             num -=1
#         else:
#             strc += stru[start:start+1]
#             start +=1
#             end +=1
#
#     return strc+stru[start:]
#
# print RealiZationreplace('bbog bog bogg','g','3',6)


# def replace(sourceStr,oldStr,newStr):
#     if len(sourceStr) == 0:
#         return ''
#     oldStrLen = len(oldStr)
#     newStrList = []
#     start = 0
#     while True:
#         if sourceStr[start:start+oldStrLen] == oldStr:
#             newStrList.append(newStr)
#             start += oldStrLen
#             if start >= len(sourceStr)-1:
#                 break
#
#         else:
#             newStrList.append(sourceStr[start])
#             if start == len(sourceStr)-1:
#                 break
#             else:
#                 start +=1
#     return ''.join(newStrList)
# print replace('cdefcdef','ef','x')

# n = int(raw_input('input people number:'))
# step = 1
# out = 0
# orderList = range(1,n+1)
# while step:
#     if len(orderList) == 1:
#         print u'最后留下来的是%d号游戏者'%orderList[0]
#         break
#     out +=1
#     if step> len(orderList):
#         step = 1
#     if out%3 == 0:
#         outIndex = orderList[step-1]
#         print orderList
#         orderList.remove(orderList[step-1])
#         print u"当前出局的是第%d号游戏者"%outIndex
#         step -=1
#     step += 1

# def BaoShu(n):
#     if not isinstance(n,int):
#         raise TypeError(u'请输入大于‘0’的正整数')
#     if n < 0:
#         raise AttributeError(u'请输入大于‘0’的正整数')
#     if n == 0:
#         raise AttributeError(u'请输入大于‘0’的正整数')
#     dict1 = {}
#     list1 = []
#     s = 1
#     for i in xrange(n):
#         dict1[i+1] = []
#         list1.append(i)
#     while len(dict1) > 1:
#         for i in list1:
#             if 3 not in dict1[i+1]:
#                 dict1[i+1].append(s)
#                 print dict1
#
#             else:
#                 del dict1[i+1]
#                 list1.remove(i)
#             if s == 3:
#                 s = 1
#             else:
#                 s += 1
#         list1 = list1
#     print u'最后留下是原来的号数为：',
#     return dict1.keys()
# print BaoShu(220)
# 请用python编写一个地址簿的小程序。地址簿能接受命令行的输入（如姓名，地址，电话，电子邮箱）
# 然后可以列举地址簿的信息，也可以把地址簿的信息导出到指定文件。
# 这个笔试题有大神会做吗？



# try:
#     print a
# except NameError,e:
#     print u'定义变量异常'
print random.randint(1,5)

