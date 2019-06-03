# encoding=utf-8
#!F:\Python27\python.exe
import  os,time,tempfile,stat,sys
# print "Content-type: text/html"
# print ""
# print "<html><head></head><body>"
# print "Hello World"
# print "</body></html>"
# lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,23],[1,2,3]]
# def change(listVal):
#     valLen = len(listVal[0])
#     newList = []
#     for i in xrange(len(listVal)):
#         for j in xrange(valLen):
#             if i == 0:
#                 newList.append([listVal[i][j]])
#             else:
#                 newList[j].append(listVal[i][j])
#     return newList
# print change(lista)
# import string
# s = '123 4  2       4567822 34555555552555'
# print s.rjust(10)
# print s.rfind('2',1)#返回最后一个的坐标
# print s.find('2',1)#返回第一个的坐标
# print s.index('2',1)
# print s.rindex('2',1)
# print s.expandtabs(1)
# print s.split(' ',1)
# s1 = 'Today is 12 fine day'
# s2 = '22'
# print s1.istitle()
# print s2.istitle()
# print string.atof(s2)
# print string.atol(s2)
# from selenium.webdriver.common.by import By
#
# def find_element_by_id(self,id_):
#     '''
#     find element within this element's children by ID
#     :arg:_id_-ID od child element to locate
#     :param id_:
#     :return:
#     '''
#     return self.find_element(by = By.ID,Value=id_)
# def DXxie(str):
#     stra =''
#     for i in str:
#         if ord(i) >=65 and ord(i)<=90:
#             stra += chr(ord(i)+32)
#             print ord(i)
#         elif ord(i) >=97 and ord(i)<=122:
#             stra += chr(ord(i)-32)
#     print stra
# str4 = 'abcABC'
# Dxie(str4)


# os.makedirs(r'd:\gloryoad1\gloryoad\road\text.txt')
# os.makedirs(r'd:\gloryoad2\gloryoad\road')
#
# os.rmdir(r'd:\gloryoad1\gloryoad\road')
# os.removedirs(r'd:\gloryoad1\gloryoad')
# os.chmod(r'D:\gloryoad1\gloryoad\road\text.txt',stat.S_IWRITE)
# print os.listdir(r'd:\gloryoad1\gloryoad\road')
# os.remove(r'D:\gloryoad1\gloryoad\road\text.txt')
# print os.listdir(r'd:\gloryoad1\gloryoad\road')
# os.rename(r'd:\gloryoad11\gloryoad',r'd:\gloryoad11\gloryoad1')
# os.rename(r'D:\gloryoad1\gloryoad\road\text.txt\text.txt',r'D:\gloryoad1\gloryoad\road\text.txt\text1.txt')
# os.remove(r'D:\gloryoad1\gloryoad\road\text.txt\text1.txt')
# print os.stat(r'D:\gloryoad1\gloryoad\road\text.txt\tr.txt')
# os.utime(r'D:\gloryoad1\gloryoad\road\text.txt\tr.txt',(1375448978,1369735977))
# fileinfo = os.stat(r'D:\gloryoad1\gloryoad\road\text.txt\tr.txt')
# print "access time of gloryroadtest.txt:%s\n mofified time of gloryroadtest.txt:%s"%(fileinfo.st_atime,fileinfo.st_mtime)
# os.system('dir D:\\gloryoad1*.*')
# file = open('ts.txt','wb')
# file = os.tmpfile()
# file.write('h1\n')
# file.write('h2\n')
# file.write('h3\n')
# file.seek(0)
# for i in file:
#     print i
# print file
# file.close()
#
# print '-'*40
#
# print u'输出操作系统的特定的路径分隔符',os.sep
# print u'输出用于分割文件路径的字符串',os.pathsep
# print u'输出当前平台哦用的行终止符',os.linesep
# print os.environ
# print '-'*40
# print os.access(r'D:\gloryoad1\gloryoad\road\text.txt\tr.txt',os.X_OK)
# print os.access(r'D:\gloryoad1\gloryoad\road\text.txt\tr.txt',os.W_OK)
# print os.access(r'D:\gloryoad1\gloryoad\road\text.txt\tr.txt',os.R_OK)
#
# dirList = os.popen('dir d://test0827.txt*.*')
# for i in dirList.readlines():
#     print i
#
# print '-'*40
# for root,dirs,files in os.walk('D:\\gloryoad1',topdown=False):
#     print u'上级目录：',root
#     for name in files:
#         print u'文件名：',os.path.join(root,name)
#     for name in dirs:
#         print u'目录名：',name
#
# print '-'*40
# print os.path.abspath('tr.txt')
# print os.path.split('D:\\worksplace\\GR1\\u2\\tr.txt')
# print os.path.dirname('D:\\worksplace\\GR1\\u2\\tr.txt')
# print os.path.basename('D:\\worksplace\\GR1\\u2\\tr.txt')
# print os.path.exists('D:\\worksplace\\GR1\\u2')
# print os.path.isabs('D:\\worksplace\\GR1\\u2\\tr.txt')
# print os.path.isabs('tr.txt')
# print os.path.isfile('D:\\worksplace\\GR1\\u2\\kong.txt')
# print os.path.isdir('tr.txt')
# print os.path.normpath('d;//worksplace\\GR1')
# print os.path.getsize('D:\\worksplace\\GR1\\u2\\kong.txt')
# print os.path.join('d:\\aa','test0827.txt','a.txt')
# print os.path.join('d:\\aa','D:\\test0827.txt','d:\\a.txt')
# print os.path.splitext('c\\:a.py')
# print os.path.splitext('a.py')
# print os.path.splitdrive('d:\\a.py')
# print os.path.splitdrive('a.py')
# import time
# lasttime = os.path.getatime('D:\\worksplace\\GR1\\u2\\kong.txt')
# print lasttime
#
# formattime = time.localtime(lasttime)
# print formattime
# print time.strftime('%Y-%m-%d %H:%M:%S',formattime)
#
# lastTime = os.path.getctime('D:\\worksplace\\GR1\\u2\\kong.txt')
# print lastTime
# formatTime = time.localtime(lastTime)
# print formatTime
# print time.strftime('%Y-%m-%d %H:%M:%S',formatTime)
# lasTTime = os.path.getmtime('D:\\worksplace\\GR1\\u2\\kong.txt')
# print lasTTime
# formaTTime = time.localtime(lasTTime)
# print formaTTime
# print time.strftime('%Y-%m-%d %H:%M:%S',formaTTime)
# print 'sys'+'-'*40
# print 'The command line arguments are:'
# for i in sys.argv:
#     print i
# print '\n\nThe PYTHONPATH is ',sys.path,'\n'

# counter = 1
# while True:
#     line = sys.stdin.readline()
#     if not line:
#         break
#     print '%s:%s'%(counter,line)
#     counter +=1

# for i in xrange(3):
#     sys.stdout.write(u'gloryroad 光荣之路')
# print '\n','_'*60,'\n'
# for i in xrange(3):
#     sys.stderr.write(u'glory road 光荣之路')
# str = [' 123']
# strs = ' bbog bog bogb '
# stru = 'Zz#n1A'
# str1 = '2A#0'
# str2 = '*bog*bog*bog*'
# dict1 = {}
# print strs.replace('b','')
# for i in xrange(10):
#     dict1[i] = []
# # del dict1[0]
# dict1=[1,2,3,3]
# print dict1.remove(1)
# del dict1[1]
# print len(dict1)
# print dict1[1]
# print strs.strip(' ')
# print strs[::-1]
# str = str[0][::-1]
# print isinstance(' ',str)
# print str1
# # print str1.split('')
# print str2.split('og',0)
# print str1[:1]
# print isinstance(-1,int)
# print len(str2)
# str2 += ' '
# print len(str2)
# print str1[-2:]
# print '*'.join('1234')

list1 = []
# for i in [1,2,3]:
#     list1.append(i)
# file_path = 'D:\\cmp\\1t.txt'
# print ''.join(os.path.split(file_path))
# print os.path.splitext(file_path)[1]
# print time.localtime()#[4]*60 + time.localtime()[5]
# os.makedirs('D:\\dmp\\emp\\smp\\simp\\wmp')
# str1 = 'D:\\dmp\\emp\\smp\\simp\\wmp'
# str3 = str1
# for i in xrange(1,len(str1.split('\\'))+1):
#     file1 = str1.split('\\')[-i] + '.txt'
#     os.chdir(str3)
#     with open(file1,'w') as fp:
#         pass
#     os.chdir(os.pardir)
#     str3 = os.getcwd()

# filename1 = tempfile.mktemp (".txt") #产生临时文件或目录，tempfile.mktemp(suffix='',prefix='tmp'，dir=None)
#                                       # 产生的文件名或目录，默认就是函数里的参数。
# open (filename1, "w").close ()
# filename2 = filename1 + ".copy"
# print filename1, "=>", filename2
# #拷文件
# # os.system ("copy %s %s" % (filename1, filename2))
# if os.path.isfile (filename2): print "Success"

# file_path = 'D:\\cmp'
# os.chdir(file_path)
# with open('score1.txt','w'):
#     pass
# os.system("copy %s %s"%('score1.txt','score2.txt'))
# print os.listdir(file_path)


# def DaLv(n,m):
#
#
#     str1 = n + m
#     return str1
#
# str1 = DaLv(2,2)
# print str1

file_path = 'c:\\a\\b\\c\\'
file1 = '1.py'
def ShChu(file_path,file1):
    os.remove(file_path+file1)
    os.removedirs(file_path)

ShChu(file_path,file1)



# print str.strip()
# print str.strip('*')
# print str.strip('b')
# print strs.strip('b')
# print str1.strip('b')
#
# def yunz(*args):
#     print u'元组的长度：',len(args)
#     print type(args)
#
# yunz('1',2)
# print len(str1)
# print str1.find('b',2,19)
# print type(str1)
# print str1
# print str1.replace('sb','s',-2)
# print str1.replace('z','&')
# print str1.count('bo')
# print '1' not in str1
# print str1[0:1]

# import timeit
#
# start = timeit.default_timer()
# pass
# end = timeit.default_timer()
# print end-start