# encoding=utf-8
import  string
s1 = 'ABC'
print s1.lower()
s2 = 'abc'
print s2.upper()
s3 = 'AbC eFg'
print s3.swapcase()
s4 = 'i love glory road!'
print s4.capitalize()
s5 = 'study python'
print s5.title()
s6 = 'sstudy psython'
print string.capwords(s6)
# 实现 字符串的upper（str)\lower(str)

str1 = 'abc'
str2 = 'ABC'
def Dxie(str1):
    str2 =''
    for i in str1:

        if ord(i) >=97 and ord(i)<=122:
            str2 += chr(ord(i)-32)
        else:
            str2 += i
    print str2
def Xxie(str2):
    str3 =''
    for i in str2:

        if ord(i) >=65 and ord(i)<=90:
            str3 += chr(ord(i)+32)
        else:
            str3 += i
    print str3
Dxie(str1)
Xxie(str2)

def DXxie(str):
    stra =''
    for i in str:
        if ord(i) >=65 and ord(i)<=90:
            stra += chr(ord(i)+32)
        elif ord(i) >=97 and ord(i)<=122:
            stra += chr(ord(i)-32)
        else:
            stra += i
    print stra
str4 = 'abc ABC'
print str4
DXxie(str4)
# 字符串对齐；格式化输出；s.ljust(width,[fillchar])
s = '123abc'
print s.ljust(10,'*')
print s.ljust(10)
# rjust
print s.rjust(10)
print s.rjust(10,'*')
# 2、显示学生的如下的信息：name、sex、age、school ，
# 其中name按照15个字符长度显示，sex 10个字符长度，age 5个字符长度，
# school 15个字符长度，并且都是左对齐，录入不少于5个学生的信息。
str1 = 'name'
str2 = 'sex'
str3 = 'age'
str4 = 'school'
print str1.ljust(15),str2.ljust(10),str3.ljust(5),str4.ljust(15)

list1 =[['Linux','m','12','guangzzhou1'],['python','F','11','guangzzhou2'],
['java','m','22','guangzzhou3'],['C#','F','10','guangzzhou5'],
['ruby','m','32','guangzzhou4']]


for i in xrange(len(list1)):
    for j in xrange(len(list1[i])):
        if j==0:
            print list1[i][j].ljust(15),
        elif j==1:
            print list1[i][j].ljust(10),
        elif j==2:
            print list1[i][j].ljust(5),
        elif j==3:
            print list1[i][j].ljust(15)

print 'name'.ljust(15),'sex'.ljust(10),'age'.ljust(5),'school'.ljust(15)

print 'Linux'.ljust(15),'m'.ljust(10),'12'.ljust(5),'guangzzhou1'.ljust(15)

# center()中间对齐
print str1.center(18,'*')
# zfill--右对齐，使用0填充
print str1.zfill(10)
print str1.rjust(10,'0')













