# encoding=utf-8
# s.rfind(substr,[start,[end]])
s = 'bay bay bay girl girl girl'
print s.find('bay')
print s.rfind('bay',1)
print s.rfind('bay',1,7)

# s.rindex(substr,[start,[end]])
print s.rindex('bay',1)

# s.replace(oldstr,newstr,[count])
print s.replace('ba','Lin',1)
# s.expandtabs([tabsize])把制表符换成空格,默认8个
s1 = '1\t2\t\t3'
print s1
print s1.expandtabs()
print s1.expandtabs(2)


# 实现方法：replace(sourcestr,oldstr,newstr)
s1 = 'bay bay bay girl girl girl'

def replace(sourcestr,oldstr,newstr):
    sourcestr1 = ''
    a = len(oldstr)
    n = 0
    for i in xrange(n,len(sourcestr)):
        if sourcestr[i:i+a] == oldstr:
            sourcestr1 += newstr

        else:
            sourcestr1 +=sourcestr[i]
    return sourcestr1
print replace(s1,'bay','keyi')

# 算法：1、找到oldstr；
# 2、for i in sourcestr,
#2.1相等：

def strReplace(sourcestr,oldstr,newstr):
    if len(sourcestr)==0:
        return ''
    oldstrLength = len(oldstr)
    newstrlength = len(newstr)
    newStrlist = []
    start = 0
    while True:
        if sourcestr[start:start+oldstrLength]== oldstr:
            newStrlist.append(newstr)
            start = start+oldstrLength
        else:
            newStrlist.append(sourcestr[start])
            if start == len(sourcestr)-1:
                break
            else:
                start +=1
    return ''.join(newStrlist)

print strReplace(s1,'bay','lini')

# s.split([sep,[maxsplit]])
s = '1 2 3 4 5 6 7 8'
print s.split()
print s.split(' ',2)
# s.splitlines([keepends])专门指定换行符进行分割
s1 = '1\n2\n'
print s1.splitlines()
print s1.splitlines(True)
print s1.split('\n')


def splitlines(st,keepends = False):
    retList = st.strip('\n').split('\n')
    if keepends:
        return map(lambda x:x+'\n',retList)
    return retList
print splitlines(s1)
print splitlines(s1,True)

# s.rsplit()
print s.rsplit(' ',2)

# s.join()
myList = ['Brazil','Russia','India','China']
print ' '.join(myList)
print '--*--'.join(myList)

# s.startwith()返回True或False
name = 'wulao'
print name.startswith('wu')
print name.startswith('wu1')

# s.endwith()是否以判断的字符进行结尾
print name.endswith('lao')

# s.isalpha()字符串都是由字母组成并至少有一个字母
print 'abc'.isalpha()
print ''.isalpha()
print 'au18'.isalpha()

# s.isalnum()字符串中都是由字母或者数字组成，并至少有一个字母或字母
print '123'.isalnum()
print ''.isalnum()
print 'abc1'.isalnum()

# s.isdigit()都是由数字组成，并至少有一个数字且为整数
print '123'.isdigit()
print ''.isdigit()
print '123a'.isdigit()
print '12.23'.isdigit()

# s.isspace()
print ' '.isspace()
print ''.isspace()
print '\t'.isspace()
print '     '.isspace()

# s.islower()判断是否全部字母为小写，并且有一个字母
print 'qwe'.islower()
print 'aaAA'.islower()
print 'a1'.islower()
print '123'.islower()
print ',.'.islower()

# s.isupper()判断是否全部字母为大写，并且有一个字母
print 'ABC'.isupper()
print 'Abc'.isupper()
print '123.788A'.isupper()
print 'abc*&'.isupper()
print 'ABC&*^'.isupper()

# s.istitle()判断首字母是不是大写,其他的字母为小写
print 'Abc ABc'.istitle()
print 'abc 123'.istitle()
print 'I love Python'.istitle()
print 'Glory Road!'.istitle()
import string

# string.maketrans(from,to)
# s.translate(map)
mapTable = string.maketrans('123','abc')
s = '123abc123abc'
print s.translate(mapTable)
# 统计字符串中的字母、数字、其他字符个数
s = r'jfsdkdfj892374893728djsfhds8676sfkjdk#^$$><?'

dn = 0
an =0
on = 0
for i in s:
    if i.isdigit():
        dn +=1
    elif i.isalpha():
        an += 1
    else:
        on += 1
print dn,' ',an,' ',on

# 实现字符串的join方法。
def join(strList,joinLetter=''):
    joinedStrig =''
    for i in strList:
        if joinedStrig == '':
            joinedStrig = str(i)
        else:
            joinedStrig = joinedStrig+joinLetter + str(i)
    return joinedStrig

print join(['1','2','ba','cc'],' ')

# int(),float(),long()
s = '18'
print int(s)
print string.atoi('011',8)
print string.atoi('0X11',16)
print string.atol('11')
print string.atof('1.2333333')

# ord()把字母转换为对应的ASCII，chr()把十进制的数字转换为字符

# s.encode([encodeing--编码类型],[errors--])编码函数，s.decode()解码

str = 'this is a string'
s1 = str.encode('base64','strict')#ignore--出现异常不会崩溃，会继续往下走
print s1
print 'decode:',s1.decode('base64','strict')


















