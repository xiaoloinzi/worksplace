# encoding=utf-8
# open\file都可以打开文件，尽量使用open，python3.0版本后就不用file了
# open(file_name,[,access_mode][bufferinf])打开路径名，最好使用绝对路径，以防查找不到文件
# access_mode=r\w\a
# bufferinf缓存的大小

fp = open('D:\\tmp\\t1.txt','w')
print type(fp)
print fp
fp.write('光荣之路2017APP测试开发班\n')
fp.write('hello world')
fp.close()
fp = open('D:\\tmp\\t1.txt','r')
content = fp.read()
print content
fp.close()
import chardet
fp = open(r'D:\tmp\test.txt')
info = fp.readline()
str = chardet.detect(info)
if str['encoding'] == 'GB2312':
    info = info.decode('gbk')
    print info
else:
    print info
fp.close()
fp = open(r'D:\tmp\test.txt')
info = fp.read()
print chardet.detect(info)
info = info.decode('gbk')
print info
fp.close()
# 隐患：程序执行中间出现异常，导致程序崩溃，没有关闭文件，导致文件泄露
# 解决方法一
try:
    fp = open(r'D:\tmp\test.txt')
    info = fp.read()
    print chardet.detect(info)
    info = info.decode('gbk')
    print info
    raise IOError,'io error 20170507'
except IOError as err:
    print 'err msg:',str(err)
finally:
    fp.close()

# with__enter__ __exit__
with  open(r'D:\tmp\test.txt','r') as fp:
    info = fp.read()
    print chardet.detect(info)
    info = info.decode('gbk')
    print info
print fp.closed
print fp.mode
print fp.name
print fp.softspace

# 4、使用w+向一个文件中写入内容，关闭文件之后，
# 再次使用w+向一个文件中写入内容。使用r+读取文件的所有内容。
# 每次操作的过程中，通过把文件的file.mode打印出来，
# 判断文件是否已close，如果没有close，则调用close。

fp = open(r'D/:\tmp\test1.txt','w+')
fp.write('写入内容1')
print fp.mode
if not fp.closed:
    print fp.closed
    fp.close()

fp = open(r'D:\tmp\test1.txt','w+')
fp.write('写入内容2')
print fp.mode
if not fp.closed:
    print fp.closed
    fp.close()

fp = open(r'D:\tmp\test1.txt','r+')
info = fp.read()
print info
print fp.mode
if not fp.closed:
    print fp.closed
    fp.close()

fName2 = r'D:\tmp\c3.txt'

# read([size])
f2 = open(fName2,'r')
content = f2.read(6)
print content
f2.close()

# readline([size])
fp = open(fName2,'r')
c1 = fp.readline(7)
print c1
fp.close()

# readlines([size]),文件大于8K时才能起效
fp = open(fName2,'r')
contentList = fp.readlines()
print 'list:',contentList
for i in contentList:
    print u'行：',i
fp.close()

# writelines(seq)一次性写入多行，write(str)需要换行符
fp = open(fName2,'a')
conList = ['\nabc\n','def\n','xyz\n']
fp.writelines(conList)
fp.closed


# 5、通过writelines 函数，向文件写入一万行内容，
# 每行的内容包括中文、字母、数字

fp = open(fName2,'w')
str1 = '测试开发 abc'
conList = []
for i in xrange(10001):
    conList.append(str1+str(i)+'\n')
fp.writelines(conList)
fp.closed
fName3 = r'D:\tmp\c5.txt'
# flush()写入硬盘
fp = open/(fName3,'w',65546)
fp.write('abc')
fp.flush()#写入了多少长度的数据，或者间隔了多长时间
fp.close()

next()
fp = open(fName2,'r')
# for i in fp:
#     print i
print '1:',fp.next()
print '2:',fp.next()
print '3:',fp.next()
print fp.tell()
print fp.fileno()
fp.close()
# tell()返回文件操作标记的当前位置，以文件的开头为基准点
fp = open(fName2,'r')
print fp.read(3)
print fp.tell()
fp.close()

# 5、1通过pycharm，写入中文和英文，至少2行，close
# 调用readline方法，直接调用tell方法，显示位置。并且解释位置。
# 一个英文站一个字节，中文站三个字符，换行符是两个字符

fp = open(fName3,'w')
str1 = '测试'
list2 = []
for i in xrange(3):
    list2.append(str1+chr(ord('a')+i)+'\n')
fp.writelines(list2)
fp.close()

fp = open(fName3,'r')
info = fp.readline()
print info
print fp.tell()
fp.close()

# seek(offset[,from])
fp = open(fName2,'r')
str1 = fp.read(6)
print str1
print fp.tell()
fp.seek(4)
str2 = fp.read(9)
print str2
print fp.tell()
fp.close()
#
# # 6、关于seek，读取文件的第2行100次，不少于两种方式。
fp = open(fName2,'r')
str1 = fp.readlines()
for i in xrange(100):
    print i,':',str1[1]
fp.close()
print '-'*40
fp = open(fName2,'r')
str1 = fp.readline()
int1 = fp.tell()
for i in xrange(100):
    fp.seek(int1)
    str2 = fp.readline()
    print i,':',str2
fp.close()
print '-'*80
fp = open(fName2,'r')
fp.readline()
lineNo = fp.tell()
fp.readline()
lineNo2 = fp.tell()
print lineNo-lineNo2
for i in xrange(100):
    fp.seek(lineNo-lineNo2,1)
    c=fp.readline()
    print i,':',c
fp.close()


# truncate(size)把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。
# 如果size比文件的大小还要大，依据系统的不同可能是不改变文件，
# 也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。
fp = open(fName3,'r+')
line = fp.readline()
print '1:',line
fp.truncate()
print fp.tell()
fp.close()
import linecache
# linecache()
# getline(finename,lineno),取文件名和行号
# getlines(finename)取得所有行，以列表的形式存在
# clearcache（）清理缓存内容
# checkcache(filename)更新最新内容到缓存中

fileContent = linecache.getlines(fName3)
print fileContent
line2 = linecache.getline(fName3,2)
print line2
print linecache.updatecache(fName3)

# 7、通过truncate 函数，分别达到如下的效果：
# 1）把一个超过100字节长度的文件，裁剪成50个字节。
# 2）裁剪一个文件，只保留前6行数据
#(1)
fp = open(file)
fp.truncate(50)
fp.close()
# (2)
fp = open(file)
for i in xrange(6):
    fp.readline()
fp.truncate()


fp = open(fName2,'r+')
info1 = fp.read()
print fp.tell()
fp.seek(50)
fp.truncate()
info = fp.read()
print fp.tell()
fp.close()

fp = open(fName2,'r+')
for i in xrange(6):
    line = fp.readline()
fp.truncate()
fp.close()

# 8、通过linecache 模块，把文件的奇数行全部打印出来

line =  linecache.getlines(fName2)
# print line[1::2]
for i in line[::2]:
    print i

# 9、写一个函数，生成一个新文件，新文件删除了原文件中的空行。

txt1 = r'D:\tmp\t1.txt'
# txt2 = r'D:\tmp\t2.txt'
txt3 = r'D:\tmp\t3.txt'
#
def fileL(file1,file2):
    fp1 = open(file1,'r')
    fp2 = open(file2,'w')
    for i in fp1:
        if i == '\n':
            continue
        if i.split():
            fp2.write(i)
    fp1.close()
    fp2.close()
print fileL(txt1)

def func1 (infile,outfile):
    infp = open(infile,'r')
    outfp = open(outfile,'w')
    lines = infp.readlines()
    for i in lines:
        if i.split():
            outfp.write(i)
    infp.close()
    outfp.close()
func1(txt1,txt3)
txtw= r'D:\tmp\newtxt.txt'
fp = open(txtw,'w+')
fp.write('你好')
fp.seek(0)#-----同时读写文件的话，要偏移位置
print fp.read()
fp.close()

fp = open(r'D:\tmp\newtxt1.txt','w')
fp.close()

# 3、读取文件的前两行
# 调用readline()两次
# 使用linecache.getlines(file)[:2]
# 4、读取文件的奇数行
# linecache.getlines(file)[::2]
# 5、在文件中写入一个列表的内容
# list1 = [1,2,3]
# fp.writelines(list1)

# 练习题6：在文件中的0、2、4位置写入当前的文件位置偏移量

fp = open(fName2,'r')
str1 = fp.read()
str2 = '0'+ str1[:2] +'2'+str1[2:4]+'4'+str1[4:]
fp.close()

fp2 = open(r'D:\tmp\txt4.txt','w')
fp2.write(str2)
fp2.close()
# 练习题8：统计一个文件中单词个数
# 文件内容：
# glory road  ,wu lao shi
# file,haha
# women, man, love

with open(r'D:\tmp\txt4.txt','r') as fp:
    str1 = fp.read()
str2 = str1.replace(',',' ').replace('.',' ').replace('!',' ').replace('\n',' ')
str2 = str2.split()
print str2
print len(str2)

# 练习题9：将一个文件的所有单词倒序写入文件中
# hello world
# glory road

list1 = linecache.getlines(r'D:\tmp\txt4.txt')

with open(r'D:\tmp\txt5.txt','r+') as fp:
    for i in list1:
        list2 = []
        for j in i.split():
            list2.append(j[::-1])

        fp.write(' '.join(list2)+'\n')

with open(r'D:\tmp\txt4.txt','r') as fp:
    strList = fp.readlines()
print strList
with open(r'D:\tmp\txt5.txt','w') as fp:
    for i in strList:
        tList = []
        for j in i.split():
            tList.append(j.strip()[::-1])
        fp.write(' '.join(tList)+'\n')

import cPickle as p
# 先p.dump进去的先load出来
# 10、生成一个bookList，存放1000本图书，生成一个animalList，
# 存放4种动物，分别调用dump存放到文件，再调用load方法导出出来。

shopListFile = 'd:\\tmp\\s1.txt'
shopListFile1 = 'd:\\tmp\\s2.txt'
shopList = ['动物1','动物2','动物3','动物4']
fp1 = open(shopListFile,'w+')
for i in xrange(1000):
    fp1.write(str(i)+'图书'+'\n')
fp1.seek(0)
bookList = fp1.readlines()
for i in bookList:
#
#
    fp2 = open(shopListFile1,'a')
    p.dump(shopList,fp2)
    p.dump(bookList,fp2)
    fp2.close()

del shopList
#
fp3 = open(shopListFile1)
storedList = p.load(fp3)
booksList = p.load(fp3)
print u'动物:',storedList
print u'图书：',bookList
fp3.close()

import os
# 对于目录的操作，os
print os.getcwd()
# os.chdir(os.pardir)
print os.getcwd()
print os.curdir
print os.pardir
# os.mkdir(r'D:\tmp\tt')
# os.makedirs(r'd:\tmp\t1\t11\t111')
# 删除目录
# os.remodir(r'D:\tmp\t1\t11')
# os.remove(r'D:\tmp\t1\1.txt')

# 创建一个目录，在目录中创建1个文件，删除目录
# 出错，改错
# 创建一个多层次目录，在目录中创建一个文件，删除多层次目录
# 出错，改错

os.mkdir(r'd:\tmp\t23')
with open(r'd:\tmp\t23\t2.txt','w') as fp:pass
os.removedirs(r'd:\tmp\t23')
os.remove(r'd:\tmp\t23\t2.txt')
os.removedirs(r'd:\tmp\t23')

os.makedirs(r'd:\tmp\t3\t323\t333')
with open(r'd:\tmp\t3\t323\t333\t333.txt','w') as fp:pass
os.removedirs(r'd:\tmp\t3\t323\t333')
os.remove(r'd:\tmp\t3\t323\t333\t333.txt')
os.removedirs(r'd:\tmp\t3\t323\t333')

os.listdir
print os.listdir('D:\\tmp')
os.rename('D:\\tmp\\s1.txt','D:\\tmp\\e1.txt')
print os.stat('D:\\tmp\\e1.txt')
str1 = str(os.system('dir D:\\'))
print str1.decode('gbk')
os.tmpfile()
fp = os.tmpfile()
fp.write('123\nabc')
fp.seek(0)
print fp.read()
fp.close()
#
print os.sep
print os.pathsep
print os.linesep
print os.environ

fileName = 'D:\\tmp\\data.log'
lineList = linecache.getlines(fileName)
print lineList

for i in lineList:
    name = 'D:\\tmp\\'+i[:8]+'.txt'
    if os.path.exists(name):
        with open(name,'a') as fp:
            fp.write(i[14:])
    else:
        with open(name,'w') as fp:
            fp.write(i[14:])





