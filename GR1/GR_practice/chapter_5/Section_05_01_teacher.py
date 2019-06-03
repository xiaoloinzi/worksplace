# # encoding=utf-8
#
# # 1、 将一个正整数分解质因数
# # 质因数就是一个数的约数，并且是质数，
# # 比如8=2×2×2，2就是8的质因数
#
# def fenJieYinShu(n):
#     n=abs(int(n))
#     if n == 1:
#         return u'1没有质因子'
#     print n,u'=',
#     for i in xrange(2,n):
#         while n!=i:
#             if n%i==0:
#                 print '%d *'%i,
#                 n/=i
#             else:
#                 break
#     print n
# fenJieYinShu(4)

# 老师的方法：
# 12 = 2*2*3
# 算法：
# n
# 2~n = i
# 1、如果n可以被i整除
# 2、n=n/i
# 数据结构：
# list1 =[]
# '*'.join()

def primeFactor(n):
    if n <=1:
        return n
    factorList = []
    tmp = n
    for i in xrange(2,n+1):
        if tmp <= 1:
            return '*'.join(factorList)
        if tmp%i==0:
            tmp/=i
            print '---',tmp
            factorList.append(str(i))
        while tmp%i == 0:
            tmp /=i
            print '---',tmp
            factorList.append(str(i))

n = 12 #int(raw_input('input a integer:'))
res = primeFactor(n)
print u'数组%d分解质因子为%d=%s'%(n,n,res)



#
# # 2、 一个字符串中， 分别输出奇数坐标字符或偶数坐标字符， 奇数坐标的一行， 偶数
# # 坐标的一行
#
# def Str(str):
#     return u'奇数坐标字符：'+str[::2]+u'\n偶数坐标字符：'+str[1::2]
#
# print Str('abcdefg')

str1 = 'abcdfghijk'
print str1[::2]
print str1[1::2]








#
# # 3、 统计字符串中的字母、 数字、 其他字符个数
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
#








#
# # 4、 有一个已经排好序的列表。 现输入一个数， 要求按原来的规律将它插入列表中
# list1 = [1,4,5,7,9,33,24,56,8,6,12]
# def Paixu(list,info):
#     list1.sort()
#     print u'排序好的数组：',list1
#     list1.append(info)
#     list1.sort()
#     print u'插入后的数组：',list1
# Paixu(list1,55)

# 数据结构：返回一个列表
# 算法：1、升序，降序，判断
# 2、append在列表末尾
# 3、排序

def sortList(numList):
    num =56 #int(raw_input('input a num:'))
    minIndex = numList.index(min(numList))
    maxIndex = numList.index(max(numList))
    numList.append(num)
    if minIndex <= maxIndex:
        numList.sort()
    else:
        numList.sort(reverse=True)
    return numList
list1 = [1,23,45,45,67]
list2 = [24,4,2,1]
print sortList(list1)
print sortList(list2)

#
# # 5、 统计名字列表中， 各名字的首字母在名字列表中出现的次数
name=['Aaron','Abner','BerAon','christcian','Earl','Geoff','Clare','Cdonis']

def ShouMingzi(name):
    '''
    参数为名字列表，返回值为空，打印出各名字的首字母和在名字列表中出现的次数

    '''
    str1 = ''.join(name)
    dict1 = {}
    for i in range(len(name)):
        sine = name[i][0]
        dict1[sine] = ''
    for key,value in dict1.items():
        print key,str1.count(key)

ShouMingzi(name)
#

# 数据结构：
# 字典的方式：dict1 = {key:value}
# 算法：1、遍历名字列表
# 2、把首字母为key，出现加一
def charNum(listWord):
    dictChar = {}
    for i in listWord:
        if dictChar.has_key(i[0]):
            dictChar[i[0]] +=1
        else:
            dictChar[i[0]] =1
    return dictChar
print charNum(name)

dict1 = charNum(name)
for i ,j in dict1.items():
    print u'姓名以字母%s开头的有：%d人'%(i,j)





# # 6、 字符替换
# # 1） 读入一个字符串
# # 2） 去掉字符串的前后空格
# # 3） 如果字符串包含数字则1替换成a， 2替换成b， 3替换成c， 以此类推
# # 4） 将字符串使用空格进行切分， 存到一个列表， 然后使用*号连接， 并输出
# # 5） 把这些功能封装到一个函数里面， 把执行结果作为返回值
#
# def StrZfu():
#     '''
#     读入一个字符串;去掉字符串的前后空格;如果字符串包含数字则1替换成a，2替换成b，3替换成c，以此类推;
#     将字符串使用空格进行切分，存到一个列表，然后使用*号连接，并输出
#     :return:字符串空格以*为连接的字符串
#     '''
#     from string import maketrans
#     str1 = '123456789'
#     str2 = 'abcdefghi'
#     strb = maketrans(str1,str2)
#     stra = raw_input(u'请输入一个字符串，按回车键结束：');
#     strd = stra.translate(strb)
#     strd = strd.strip(' ')
#     list1 = strd.split(' ')
#     return '*'.join(list1)
#
# print StrZfu()
#


#
# # 7、 找出字符串中出现次数最多的字符， 并输出其出现的位置
#
str1 = 'abcdeffffffgsdefgdfd'

def ZiFu(str1):
    '''
    输入的参数为一句字符串，而后输出出现字次最多的字符和其位置
    :param str1: 字符串
    :return:为空
    '''
    dict1 = {}
    for i in str1:
        if dict1.has_key(i[0]):
            dict1[i[0]] += 1
        else:
            dict1[i[0]] =1

    for key,value in dict1.items():
        if value == max(dict1.values()):
            str2 = key

    print u'出现次数最多的字符：',str2,u'\n出现的位置索引分别是：'
    for j in range(len(str1)):
        if str1[j] == str2:
            print j,
ZiFu(str1)

# 数据结构：列表\字典
# 算法：1、遍历字符串
# 2、count（）同之前的最大值进行比较
def findMaxOccLetter(s):
    macOcc = {}
    #key :value char:[1,2,3]
    maxOccNum = 0
    posList = []
    for i in xrange(len(s)):
        if s.count(s[i]) > maxOccNum:
            macOcc.clear()
            macOcc[s[i]] = [i]
            maxOccNum = s.count(s[i])
        elif s.count(s[i]) == maxOccNum:
            if macOcc.has_key(s[i]):
                macOcc[s[i]].append(i)
            else:
                macOcc[s[i]] = [i]

    return macOcc

print findMaxOccLetter('abcdefgabcabv')




#
# # 8、 找出一段句子中最长的单词及其索引位置， 以字典返回
#
# str1 = '''Youth it is not a matte of rosy cheek suppl cheek ; /
# it is a cheek of the vigor a cheek of the matte , a vigor of the Youth ; /
# it is the state of the deep state of vigor'''
#
# def chaZhao(str):
#     str2 = str.split(' ')
#     maxlen = max(len(word) for word in str2)
#     dict1 ={}
#     for i in xrange(len(str2)):
#         if len(str2[i])==maxlen:
#             if dict1.has_key(str2[i]):
#                 dict1[str2[i]].append(i+1)
#             else:
#                 dict1[str2[i]]=[]
#                 dict1[str2[i]].append(i+1)
#
#     return dict1
#
# print chaZhao(str1)
#








#
# # 9、字母游戏
# # “Pig Latin”是一个英语儿童文字改写游戏，整个游戏遵从下述规则：
# # (1). 元音字母是‘a’、‘e’、‘i’、‘o’、‘u’。字母‘y’在不是第一个字母的情况下，也被视作元音
# # 字母。其他字母均为辅音字母。例如，单词“yearly”有三个元音字母（分别为‘e’、‘a’和最后一个
# # ‘y’）和三个辅音字母（第一个‘y’、‘r’和‘l’）。
# # (2). 如果英文单词以元音字母开始，则在单词末尾加入“hay”后得到“Pig Latin”对应单词。例如，“ask”
# # 变为“askhay”，“use”变为“usehay”。（同上）
# # (3). 如果英文单词以‘q’字母开始，并且后面有个字母‘u’，将“qu”移动到单词末尾加入“ay”后得到
# # “Pig Latin”对应单词。例如，“quiet”变为“ietquay”，“quay”变为“ayquay”。
# # (4). 如果英文单词以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”后得到“Pig Latin”
# # 对应单词。例如，“tomato”变为“omatotay”， “school” 变为“oolschay”，“you” 变为
# # “ouyay”，“my” 变为“ymay ”，“ssssh” 变为“sssshay”。
# # (5). 如果英文单词中有大写字母，必须所有字母均转换为小写。
# # 输入格式:
# # 一系列单词，单词之间使用空格分隔。
# # 输出格式：
# # 按照以上规则转化每个单词，单词之间使用空格分隔。
# # 输入样例：
# # Welcome to the Python world Are you ready
# # 输出样例：
# # elcomeway otay ethay ythonpay orldway arehay ouyay eadyray
#
#
#
# def Pig_Latin(str):
#     list1 = str.lower().split(' ')
#     str2 = ('a','e','i','o','u')
#     str3 = ''
#     for i in range(len(list1)):
#         s = 0
#         if list1[i][0]  in str2:
#              list1[i] = list1[i] + 'hay'
#         elif list1[i][0] == 'q' and list1[i][1] == 'u':
#             list4 = list(list1[i])
#             del list4[:2]
#             list1[i] = ''.join(list4)
#             list1[i] = list1[i] + 'quay'
#         elif list1[i][0] not in str2:
#             for j in range(len(list1[i])):
#                 if list1[i][j]  in str2:
#                     break
#                 if list1[i][j] =='y' and j == 1:
#                     break
#                 else:
#                     list4 = list(list1[i])
#                     s += 1
#                 str3 = list1[i][:s]
#             list4 = list(list1[i])
#             del list4[:s]
#             list1[i] = ''.join(list4)
#             list1[i] = list1[i] + str3 + 'ay'
#     str3 = ' '.join(list1)
#     return str3
#
#
# str1 = 'Welcome to the Python world Are you ready'
# print Pig_Latin(str1)
#

def letterGame(s):
    wordList = s.replace(',',' ').replace('.',' ').split()
    print wordList
    wordListConvert = []
    wordList2 =[]
    for i in wordList:
        wordList2.append(i.lower())
    for word in wordList2:
        if word[0] in ['a','e','i','o','u']:
            word = word +'hay'
            print word
        elif word[:2] == 'qu':
            word = word[2:] + word[:2]+'ay'
            print word
        consonantLetterIdex = -1
        for i in xrange(len(word)):#
            if word[i] not in ['a','e','i','o','u','y'] or (word[0]=='y' and i==0):
                consonantLetterIdex = i
            else:
                break
        if consonantLetterIdex !=-1:
            word = word[consonantLetterIdex+1:]+word[:consonantLetterIdex+1]+'ay'
        wordListConvert.append(word)
    return wordListConvert
print letterGame('Welcome to the Python world Are you ready')









#
#
#
# # 10、 实现字符串的upper、 lower以及swapcase方法
#
#
# str1 = 'abcEFG'
# str2 = 'ABCefg'
#
# def Dxie(str1):
#     '''
#     实现字符串的upper
#     :param str1:
#     :return:
#     '''
#     str2 =''
#     for i in str1:
#
#         if ord(i) >=97 and ord(i)<=122:
#             str2 += chr(ord(i)-32)
#         else:
#             str2 += i
#     return str2
# def Xxie(str2):
#     '''
#     实现字符串的lower方法
#     :param str2:
#     :return:
#     '''
#     str3 =''
#     for i in str2:
#
#         if ord(i) >=65 and ord(i)<=90:
#             str3 += chr(ord(i)+32)
#         else:
#             str3 += i
#     return str3
# print Dxie(str1)
# print Xxie(str2)
#
# def DXxie(str):
#     '''
#     实现字符串的swapcase方法
#     :param str:
#     :return:
#     '''
#     stra =''
#     for i in str:
#         if ord(i) >=65 and ord(i)<=90:
#             stra += chr(ord(i)+32)
#         elif ord(i) >=97 and ord(i)<=122:
#             stra += chr(ord(i)-32)
#         else:
#             stra += i
#     return stra
#
# str4 = 'abc ABC'
# print DXxie(str4)






