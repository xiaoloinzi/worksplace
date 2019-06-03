# encoding=utf-8
import random,os
# 1、实现自己的数学模块mymath，提供有4个函数，分别为加减乘除，
# 在B模块中调用A模块的函数。
# 把当前的py文件当做B模块,mymath作为A模块
# import mymath
#
# print mymath.add(1,2)
# print mymath.division(2,4)
# print mymath.ride(4,8)
# print mymath.sub(9,3)




# 2、实现自己的字符串模块mystr，里面有方法：isdigit,strip,
# join,split
# import mystr
# str3 = '\n\t abc ccc\n\t '
# print mystr.Strip(str3)
# str4 = '*bay *bay*'
# print mystr.Strip(str4,'*')
# print mystr.Split('bbog bog bogbb','bb',-2)
# print mystr.Join(['abc','xyz','glory road'])
# print mystr.Join(['abc','123','oj'],'*')
# print mystr.Isdigit('109')

# 3、构建一个模块的层级包
# 在当前的目录下面建立和当前文件同级的package：p1，
# 在p1下面建立两个模块分别为，p11和p12，

# import p1
# print p1.p11.b
# print p1.p12.a


# 4、实现一个除法函数，并处理异常

# def subError(x,y):
#     try:
#         return x/y
#     except ZeroDivisionError,e:
#         return u'除法异常'
#
# if __name__=='__main__':
#     print subError(4,0)


# 5、引发一个异常，并将它抛除到上层函数，上层函数捕获该异常并处理

# def boHuoError():
#     '''
#     用户输入非数值，则把异常抛出到上层函数处理，输入0则捕获异常进行处理
#     :return:
#     '''
#     try:
#         num = int(raw_input('请输入一个数值：'))
#         numnoe = 4/num
#
#         return numnoe
#     except ZeroDivisionError,e:
#         return e
#
# if __name__=='__main__':
#     print boHuoError()




# 6、实现字符串、列表、元组和set之间互相转换

# def printSet(sep):
#     print u'原始序列：',sep
#     print u'转换成set：',set(sep)
#
# if __name__=="__main__":
#     str1 = '1112345'
#     str2 = 'ababcdfb'
#     list1 = ['1','2','1','4','5','2']
#     list2 = [1,2,3,1,2,3,4,5,6,7,6]
#     tuple1 = ('1','2','1','4','5','2')
#     tuple2 = (1,2,3,4,2,3,1,2,6)
#     printSet(str1)
#     printSet(str2)
#     printSet(list1)
#     printSet(list2)
#     printSet(tuple1)
#     printSet(tuple2)



# 7、结合set对象，统计某个list出现的重复元素个数

# def ChongFu(list1):
#     '''
#     计算有重复的元素个数
#     :param list1:
#     :return:
#     '''
#     ste1 = set(list1)
#     sun = 0
#     for i in ste1:
#         if list1.count(i)>1:
#             sun +=1
#     print u"重复元素个数：",sun
#
# if __name__=="__main__":
#     list1 = ['1','1','2','1','1','4','5','2','6','6','7','6']
#     ChongFu(list1)


# 8、定义一个元组，向元组中添加元素或者修改已有元素，并捕获异常

# def fixTuple(tuple1):
#     '''
#     向元组中添加元素或者修改已有元素，并捕获异常
#     :param tuple1:
#     :return:
#     '''
#     try:
#         print u'修改前的元组',tuple1
#         tuple1[1]=3
#     except TypeError,e:
#         print u'元组修改元素异常：',e
#
#
# def addTuple(tuple2):
#     '''
#     向元组中添加元素,并捕获异常
#     :param tuple1:
#     :return:
#     '''
#     try:
#         print u'添加前的元组',tuple2
#         tuple2 = tuple2+(8,)
#         print u'添加后的元组',tuple2
#     except TypeError,e:
#         print u'元组添加元素异常：',e
#
# if __name__=="__main__":
#     tuple1 = (1,2,3,4,5)
#     tuple2 = ('1','2','3','4','5')
#     fixTuple(tuple1)
#     addTuple(tuple2)

# 9、删除无重复元组中给定的元素

# def DeleteTuple(tuple):
#     '''
#     删除无重复元组中给定的元素
#     :param tuple:
#     :return:
#     '''
#     try:
#         del tuple[1]
#         print tuple
#
#     except TypeError,e:
#         print u'删除无重复元组中给定的元素：',e
# if __name__=="__main__":
#     tuple1 = (1,2,3,4,5)
#     DeleteTuple(tuple1)


# 10、有一个ip.txt，里面每行是一个ip，实现一个函数，
# ping 每个ip的结果，把结果记录存到ping.txt中，
# 格式为ip:0或ip:1 ，0代表ping成功，1代表ping失败

# def pingIP(ippath,pingpath):
#     with open(ippath,'a+') as fp:
#         fp.writelines('192.168.1.101'+'\n')
#         fp.write('120.123.12.1'+'\n')
#         fp.write('192.168.1.1'+'\n')
#         fp.write('1@.1@.1.104'+'\n')
#         fp.seek(0)
#         line = fp.readlines()
#     for i in line:
#         msg = os.system('ping '+ i.strip())
#         print msg
#         with open(pingpath,'a') as fp:
#            fp.write(i.strip()+':'+ str(msg)+'\n')
#
# if __name__=="__main__":
#     ippath = 'D:\\tmp\\ip.txt'
#     pingpath = "D:\\tmp\\ping.txt"
#     pingIP(ippath,pingpath)




# 11、实现DOS命令执行功能，接受输入命令并执行，然后把执行结果和
# 返回码打印到屏幕

# str1 = raw_input('please input command ：')
# str2 = os.popen('%s'%str1)
# for i in str2:
#     print i.decode('gbk')


# 12、求一个n*n矩阵对角线元素之和


# def SumOfDiagonalElements(lista):
#     try:
#         n = len(lista)
#         m,num,str1= 0,0,0
#         for i in xrange(len(lista)):
#             if len(lista) != len(lista[i]):
#                 raise IndexError(u'不是n*n矩阵列表!')
#             if not isinstance(list1[i][n-1],(int,float)):
#                 raise TypeError(u'对角元素不是数值，不能进行计算!')
#             if not isinstance(lista[i][m],(int,float)):
#                 raise TypeError(u'对角元素不是数值，不能进行计算!')
#             if lista[i][n-1]!= lista[i][m]:
#                 num += lista[i][n-1]+ lista[i][m]
#             if lista[i][n-1]== lista[i][m]:
#                 str1 = lista[i][m]
#             n -=1
#             m += 1
#         print u'对角线元素之和：',
#         return num+str1
#     except Exception,e:
#         return e
#
# list1 = [[1,2,3,4,5],[5,6,7,8,9],[1,2,3,4,5],[5,6,7,8,9],[5,6,7,8,9]]
# list4 = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]
# list2 = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,'2']]
# list3 = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7]]
# print SumOfDiagonalElements(list1)
# print SumOfDiagonalElements(list4)
# print SumOfDiagonalElements(list2)
# print SumOfDiagonalElements(list3)



# 13、输入一个数组，最大的与第一个元素交换，最小的与最后一个元素
# 交换，输出数组

# def ExchangeElement(list1):
#     try:
#         maxnum = max(list1)
#         minnum = min(list1)
#         dict1 = {x:list1[x] for x in xrange(len(list1))}
#         print u'初始列表：',list1
#         for key,value in dict1.items():
#             if value==maxnum:
#                 dict1[key] = dict1[0]
#                 dict1[0] = maxnum
#             if value==minnum:
#                 dict1[key] = dict1[len(list1)-1]
#                 dict1[len(list1)-1] = minnum
#         print u'交换后列表：',
#         return list(dict1.values())
#     except Exception,e:
#         return e
# list1 = [6,1,8,3,5,7,98,34,67,156,23,56,12,12]
# print ExchangeElement(list1)


# 14、平衡点，一个数组，有一个数字左边所有的数字加起来的总和等于
# 这个数右边所有数字的总和，请输出这个数以及坐标


# def LeftRightSum(listr):
#     try:
#         for i in xrange(len(listr)):
#             if sum(listr[:i]) == sum(listr[i+1:]):
#                 print u'左右两边之和相等的数是：',listr[i],
#                 print u'，坐标是：',
#                 return i
#         return u'没有一个数字左边所有的数字加起来的总和等于这个数右边所有数字的总和'
#     except Exception,e:
#         return e
# lista = [2,1,6,4,8,0,9,6,4,3,2,5,7,6,8,9,13,45,34]
# list1 = [1,3,2,4,2,4,6]
# print LeftRightSum(list1)
# print LeftRightSum(lista)



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



# 16、 输入一个数组， 实现一个函数， 让所有奇数都在偶数前面


# def OddevenArrangement(lista):
#     try:
#         list1 = []
#         list2 = []
#         for i in lista:
#             if i%2==0:
#                 list1.append(i)
#             if i%2 != 0:
#                 list2.append(i)
#         list1.sort()
#         list2.sort()
#         list1.extend(list2)
#         return list1
#     except Exception,e:
#         print u'非法参数：',e
#
# lista = [2,1,6,4,8,0,9,6,4,3,2,5,7,6,8,9,13,45,34]
# listb = [2,1,'d',4,'d',0,9,6,4,3,2,5,7,6,8,9,13,45,34]
# tuple1 = (1,2,5,3,7,35,8,5)
#
# print OddevenArrangement(lista)
# print OddevenArrangement(listb)
# print OddevenArrangement(tuple1)


# 17、 lista=['a','abc','d','abc','fgi','abf']，
# 寻找列表中第一次出现次数最多的第一个字母， 出现了几次


# lista=['d','abc','d','abc','fdgi','abdf','de','dr','ag']
#
# def appearsMostfirstLetter(lista):
#     try:
#         dict1 = {}
#         for i in lista:
#             if dict1.has_key(i[0]):
#                 dict1[i[0]] += 1
#             else:
#                 dict1[i[0]] = 1
#         num = max(dict1.values())
#         s = [i[0] for i in lista]
#         for i in s:
#             if s.count(i) == num:
#                 return u'第一次出现次数最多的第一个字母：%s ，出现了%d次'%(i,num)
#     except Exception,e:
#         print u'非法参数：',e
# print appearsMostfirstLetter(lista)



# 18、 请输入星期几的第一个字母来判断一下是星期几， 如果第一个字母
# 一样， 则继续判断第二个字母
# Monday, Tuesday, Wednesday,
# Thursday, Friday, Saturday, Sunday




# 19、 有一堆100块的石头， 2个人轮流随机从中取1-5块，
# 谁取最后一块就谁win， 编程实现此过程

# def printWinMan():
#     try:
#         n = 100
#         while True:
#             for i in xrange(1,3):
#                 num = random.randint(1,5)
#                 n = n - num
#                 print i,u'取得数量：',num,u'，剩余数量:',n
#                 if n == 0 or n<0:
#                     return u'win man：'+str(i)
#     except Exception,e:
#         return u'非法参数：',e
# print printWinMan()


# 20、 实现一个方法， 判断一个正整数是否是2的乘方，
# 比如16是2的4次方，返回True； 18不是2的乘方， 返回False。
# 要求性能尽可能高




