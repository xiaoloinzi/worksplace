# encoding=utf-8
#rb只读，以二进制的方式读写文件
#wb只写，以二进制的方式读写文件
#ab追加写，以二进制的方式读写文件
#xb只写，以二进制的方式读写文件
filePath = 'D:\\worksplace\\GR1\\test1.txt'
f = open(filePath,'r+')
stra = 'a'
f.write(stra)
print stra
f.close
#
filePath = 'D:\\worksplace\\GR1\\test1.txt'
f = open(filePath,'w+')#先清除所有数据，再进行相应的操作
stra = 'abcd'
f.write(stra)
#strb = f.read()
#print strb
f.close

filePath = 'D:\\worksplace\\GR1\\test1.txt'
f = open(filePath,'a+')
stra = '11122'
#print f.read()
print f.write(stra)
#
# f.close
#现有一个文本内容
#this is the first line in the file;
#this is the second line in the file;
#this is the forth line in the file;
#要求在该文件内容的第三行增加this is the third line in the file;
# 写入本文件中
#使用open函数将内容写入另外一个文件中，并且在文件结尾署上自己的名子(中文)’
#格式插入的数据独占一行
filePath = 'D:\\worksplace\\GR1\\test1.txt'
f = open(filePath,'a+')
stre = 'this is the third line in the file;'
strw = f.write('\n'+stre)
f.close()
filePath = 'D:\\worksplace\\GR1\\test1.txt'
f = open(filePath,'r')
filePath2 = 'D:\\worksplace\\GR1\\test2.txt'
f2 = open(filePath2,'a+')
for i in f.readlines():
   f2.write(i)
f2.write('\n'+u'林春莲')
f.close()
f2.close()
#方法思路：
#1、定义一个插入的语句'this is the third line in the file;'
#2、读取文件，写文件
#3、度文件-》修改文件内容-》内容写入到读取的文件中
#4、读取文件

sentense = 'this is the third line in the file;'
file1 = 'D:\\worksplace\\GR1\\test1.txt'
file2 = 'D:\\worksplace\\GR1\\test2.txt'
f1 = open(file1,'r')
f1Result = f1.readlines()
f1.close()
f1Result.insert(2,sentense+'\n')

f1 = open(file1,'w')
f1.writelines(f1Result)
f1.close()
f2 = open(file2,'w')
f2.writelines(f1Result)
f2.write('\n'+u'我的名字是：林春莲')

f2.close()
