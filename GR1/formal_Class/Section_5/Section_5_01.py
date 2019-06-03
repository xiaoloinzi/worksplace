# encoding=utf-8
str1 = 'sdfhjsdhf'
str2 = u'fdsf'
str3 = r'\\\nhfdsjh\t'
print str3
print 'I love python! I am %10d years old'%18#%长度d
print 'I love python! I am %10s years old'%'18'
print 'I love %-10s! I am %10d years old'%('python',18)
# -为左对齐
print 'aaa%10faaaa'%2.34567#10个字符
print 'aaa%.2faaaa'%2.34567
print '%c'%68#输出ASCII码
# 2、显示学生的如下的信息：name、sex、age、school ，
# 其中name按照15个字符长度显示，sex 10个字符长度，age 5个字符长度，
# school 15个字符长度，并且都是左对齐，录入不少于5个学生的信息。
print '%-15s%-10s%-5s%-15s'%('name','sex','age','school')

print '%-15s%-10s%-5d%-15s'%('Linux','m',12,'guangzzhou1')
print '%-15s%-10s%-5d%-15s'%('python','F',11,'guangzzhou2')
print '%-15s%-10s%-5d%-15s'%('java','m',22,'guangzzhou3')
print '%-15s%-10s%-5d%-15s'%('C#','F',10,'guangzzhou5')
print '%-15s%-10s%-5d%-15s'%('ruby','m',32,'guangzzhou4')

# 转义符：
a = 12
#续行符
if a==1\
    :
    print 'ok'
else:
    print 'failed'
#\n \\,\',\",\t,\r
print 'abc\ntf'

# 2、列出大家所知道的字符串支持的运算符，并且写出来
print u'运算符有*，+，[],[:],not in ,in'
str1 ='1234'
str2 = 'abcd'
print '%s'%(str1+str2)
print '%s'%str1*3
print str1[3]
print str1[::-1]
if '4' in str1:
    print 4
else:
    print 'not in'
if '4' not in str1:
    print 4
else:
    print 'not in'
print cmp(str1,str2)
print r'%s\n'%str1

#strip([chars]):行首和行尾的不可见的字符清理掉或指定字符
a = '  glory road'
print a
print a.strip()
s = '**bay* boy **'
print s
print s.strip('*')
#定义一个字符串，首尾都包含如下字符：换行符、制表符、空格。调用strip
#函数，并且打印执行前后的字符串内容
str3 = '\n\t abcccc\n\t '
print str3
print str3.strip()
print str3.strip('\n\t ')
print str3.strip('\n\t c')
# lstrip([chars])
# rstrip([chars])
print s.lstrip('*')
print s.rstrip('*')

# 实现字符串的strip方法. 只要能去掉如下四种字符即可\t \r \n ' '

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
print funcSrip(str3,'*')

def strips(sourceStr,chars=None):
    pSeq = chars
    if chars is None:
        pSeq = [' ','\t','\r','n']
    start = 0
    last = len(sourceStr)-1
    s = e =0
    while True:
        if start > last:
            return ''
        if s and e:
            return sourceStr[start:last+1]
        if sourceStr[start] not in pSeq:
            s = 1
        else:
            start +=1
        if sourceStr[last] not in pSeq:
            e =1
        else:
            last -=1

print strips('\r\t ab  c \r\t ')
print strips('\t ab  c \t\n ','a')

















