# encoding=utf-8
#普通字符串
s1 = 'ab\ndr'
print s1
print type(s1)

#原始字符串
s2 = r'adf\ndr'#字符串前面加r,字符转义符不起作用
print s2
print type(s2)

#Unicode字符串
s3 = u'sdf\ndr'#从类型上吧Unicode字符串和普通字符串区分开来
print s3
print type(s3)

#转义符以”\"反斜线开头的为转义符
#\（在行尾为换行），然后在括号、中括号，大括号中的换行不需要反斜线进行换行
s4 = 'dfdrer\
df'
print s4

#\\两个反斜杠为转义\
s5 = 'abc\\'
print s5

#转义单引号\'
s6 = 'e\'e'
print '转义单引号',s6

#转义双引号\"
s7 = 'e\"e'
print '转义双引号',s7
#转义换行\n
s8 = 'e\ne'
print '转义换行',s8

#转义制表符\t
s9 = 'e\te'
print '转义制表符',s9

#转义为空\r，前面的数据为空
s10 = 'e\ra'
print '转义为空，前面的数据为空',s10
#写一个字符串a显示所有转义字符的效果，字符串b为不转义字符的效果
#
print '验证转义起效和失效，区别是在前面加"r"'
a = 'Im\'nice\tok\"the\nright\"\\ok\r'
b = r'I\rm\'nice\tok\"the\nright\"\\ok'
c = r'''Im\'nice\tok\"the\nright\"\\ok'''
a1 = '''\\\\'\"\n\t\r\\'''
print '转义起效:\n',a
print '转义失效:',b
print a1


#+ * [] [::] in
b1 = 'abc'
b2 = 'def'
print '字符串通过+ 进行连接',b1 + b2
print '字符串使用*字符进行多倍输出',b1 *2
print b1[1]
print b1[::2]
if 'c' in b1:
    print 'c在b1中'

#对于给定的字符串，HelloPython抽取偶数字符，
# 别切判断hello是否在字符串中
str1 = 'HelloPython'
str2 = ''
for i in str1[1::2]:
    str2 += i
print str2
str3 = 'hello'
# for s in str3:
#     if s in str2:
#         print s
if str3 in str2:
    print str3,u'存在',str2,u'中'
else:
    print str3,u'不存在',str2,u'中'

# strip([chars])清除字符串，不指定chars时会自动清除头尾合其他符号，chars为指定的符号
s11 = 'boy boy boy   '
print s11
print s11.strip()
s12 = '*boy boy boy *'
print s12
print s12.strip('*')

#lstrip([chars])清除左边的符号，生成新的字符串，使用时，需要一个变量来重新定义
print s12.lstrip('*')
#rstrip([chars])清除右边的符号
print s12.rstrip('*')
# 题目3：给定字符串：’  Keep on going, never give up.  ’,
# 去掉字符串首尾的空格以及标点符号.
#思路：使用str.strip().strip('.')，或str.strip('. '),strip可以一次去掉多个符号，则调用一次就可以
str1 = '  Keep on going, never give up. '
#可以先赋值给另外的变量再输出
str2 = str1.strip('. ')
print str1.strip('. ')

#改变字符串的大小写，转换小写：s.lower(),转换为大写：s.upper()
s13 = 'Glory Road'
# print s13.lower()
# print s13.upper()

#在字符串中寻找某个子串
#s.find(substr,[start],[end]),返回字符串存在开始的长度，如果没有找到，返回-1
#
print s13.find('oa')
print s13.find('abc')

#s.replace(oldstr,newstr,[count])count表示替换多少次
print s13.replace(' ','-')
#
#s.split([sep])不指定以空格做切割，指定以指定的字符做切割,一般不单独使用，使用后生成列表
print s13.split()
print s13.split('R')
#
# #把列表转换成字符串 .join()
#
list7 = s13.split()
print '---**---'.join(list7)

#题目4：给定字符串，’  Keep on going, never give up.  ’,
# 判断里面是否有小写字符，如果有则报错退出
#思路：指定用一个变量存储字符串，
# 1、遍历这个字符串，
# 2、同小写字符进行比较
#2.1'a'<=char <='z'
#2.2 char.islower()
#2.3 ord('a') <= ors(char) <= ord('z')
str11 = '  Keep on going, never give up.  '
str12 =str11.strip('. ')
str12 = str12.replace(',','')
str12 = str12.split()
str12 = ''.join(str12)
for i in str12:
    if i.islower():#调用.islower()进行判断是否为小写
        print i,u'有错误'
        break

print str12
#ord的演示
print ord('a')
print ord('z')
#.islower()演示
s8 = 'ab'
print s8.islower()#返回布尔值

