# encoding=utf-8
import os,time,sys
print os.sep
print os.pathsep
fileName = "D:\\cmp\\c3.txt"
print os.access(fileName,os.W_OK)
print os.access(fileName,os.R_OK)
print os.access(fileName,os.X_OK)


#  1、不使用\,组装一个路径，并且新建一个文件，写入’hello world’
#
# 2、新建一个文件，并且判断其具备哪些权限，打印出来


os.makedirs("D:"+os.sep+"cmt"+os.sep)
with open("D:"+os.sep+"cmt"+os.sep+'ti.txt','w') as fp:
    fp.write('hello world')
print u'写：',os.access("D:"+os.sep+"cmt"+os.sep+'ti.txt',os.W_OK)
print u'读：',os.access("D:"+os.sep+"cmt"+os.sep+'ti.txt',os.R_OK)
print u'执行：',os.access("D:"+os.sep+"cmt"+os.sep+'ti.txt',os.X_OK)


filePath = 'D:'+os.sep+'cmt'+os.sep+'t2'
if not os.path.exists(filePath):#程序是可重入的
    os.mkdir(filePath)
fileName = filePath+os.sep + 't2.txt'
with open(fileName,'w') as fp:
    fp.write('Hello World')
with open(fileName,'r') as fp:
    print fp.read()
print os.access(fileName,os.W_OK)
print os.access(fileName,os.R_OK)
print os.access(fileName,os.X_OK)
#

# os.popen--执行系统命令，获取返回的值，存到一个文件句柄中，可以像操作文件一样使用
dirList = os.popen('dir D:\\tmp')
for i in dirList.readlines():
    print i.decode('gbk')

# 3、运行ipconfig，之后显示其中所有的ipv4 地址;

# 方法一：
dirList = os.popen('ipconfig')
for i in dirList.readlines():
    if 'IPv4'+' 地址'.encode('gbk') in i:
        print i.decode('gbk')
# 方法二：
dirList = os.popen('ipconfig')
for i in dirList.readlines():
    if 'IPv4' in i:
        print i.decode('gbk')
# 老师的方法：
dirList = os.popen('ipconfig')
for i in dirList.readlines():
    if 'IPv4 地址' in i.decode('gbk'):
        print i.decode('gbk').encode('utf-8')

# os.walk(top,topdown=True,oneerror=None,follwlinks=False)遍历指定的路径
# i=目录名，j=文件夹名，k=文件名
for i ,j,k in os.walk("D:\\tmp"):
    print i
    print j
    print k
    print '**********************'
print type(os.walk("D:\\tmp"))#<type 'generator'>生成器

# 4、遍历一个多级目录，打印出每一个文件或者文件夹的大小。
file_path = "D:\\tmp"
for filepath ,filejia,file1 in os.walk(file_path):
    print filepath,':',os.path.getsize(filepath)
    print filejia
    print file1
    for i in filejia:
        filesize = os.path.getsize(filepath+'\\'+i)
        print ' 文件夹%s size %s'%(i,filesize)
    print u'文件：---'
    for j in file1:
        filesize1 = os.path.getsize(filepath+'\\'+j)
        print ' 文件%s size %s'%(j,filesize1)
    print '-'*40
# os.path.getsize(name)获得文件的大小，如果那么是目录返回0L,
# 如果那么代表的目录或文件不存在，则会报WindowsError异常

os.path.abspath()
print os.path.abspath('D:\\tmp\\t1')
print os.path.abspath('c3.txt')
print os.getcwd()

# os.path.split(path)--以反斜杠为切割的标准，最后的文件夹后面没有反斜杠也会被当做文件进行切割
# print os.path.split('D:\\worksplace\GR1\\formal_Class\\Section_6')
# 1、 针对如下的三种目录分别做split 切割，其中c12是目录：
# D:\tt4\c12
# D:\tt4\c12\
# D:\tt4\c12\t1.txt
# 2、返回如下文件的绝对路径:
# t1.txt
# D:/tt4/c12/t1.txt

print os.path.split('D:\tt4\c12')
print os.path.split('D:\\tt4\\c12\\')
print os.path.split('D:\\tt4\\c12\\t1.txt')
print os.path.abspath('t1.txt')
print os.path.abspath('D:/tt4/c12/t1.txt')

# # os.path.dirname --返回目录的名称
# print os.path.dirname('D:\\tmp\\t1')
# # os.path.basename()--返回文件的名称,文件夹后面以反斜杠结尾的，返回空。一样是以反斜杠为切割标准的
# print os.path.basename('D:\\tmp\\t1')
# # os.path.exists()判断文件或目录是否存在
# print os.path.exists('D:\\tmp\\t1')
# # os.path.isabs()判断是否是绝对路径
# print os.path.isabs('D:\\tmp\\t1')
# print os.path.isabs('t1.txt')

# 3、针对如下的参数，分别返回dirname 和 basename，其中c12 是目录
# D:\tt4\c12
# D:\tt4\c12\
# D:\tt4\c12\t1.txt
# 4、分别针对一个文件，和带路径的文件，调用isabs函数
print os.path.dirname('D:\\tt4\\c12')
print os.path.dirname('D:\\tt4\\c12\\')
print os.path.dirname('D:\\tt4\\c12\\t1.txt')
print os.path.basename('D:\\tt4\\c12')
print os.path.basename('D:\\tt4\\c12\\')
print os.path.basename('D:\\tt4\\c12\\t1.txt')
print os.path.isabs('D:\\tmp\\t1.txt')
print os.path.isabs('t1.txt')

# os.path.isfile()判断是否是文件
print os.path.isfile('D:\\tmp')
print os.path.isfile('D:\\tmp\\c3.txt')
# os.path.isdir()判断是否是目录
print os.path.isdir('D:\\tmp')
print os.path.isdir('D:\\tmp\\c3.txt')
# os.path.normpath()转换为适应相应平台的路径格式
print os.path.normpath('D:/tmp/c3.txt')
# os.path.join()连接目录

print os.path.join('D:\\tmp','t1','t1.txt')
# 5、针对一个在当前工作目录的文件，以及一个不在当前工作目录的文件，
# 调用isfile函数，均只指定文件名称。针对目录调用isfile函数
# 6、调用isdir函数，同上
# 7、分别针对一个存在的文件，以及一个不存在的文件，调用getsize函数
# 8、通过join方法，打印出如下的文件名：D:\tt4\c12\t2\t2.txt
print os.getcwd()
print os.path.isfile('Section_06_02.py')
print os.path.isfile('t1.txt')
print os.path.isfile('D:\worksplace\GR1\formal_Class\Section_6')
#
print os.path.isdir('Section_06_02.py')
print os.path.isdir('t1.txt')
print os.path.isdir('D:\worksplace\GR1\formal_Class\Section_6')
#
print os.path.getsize('D:\\cmp\\ttt.txt')
print os.path.getsize('D:\\cmp\\c3.txt')
print os.path.join('D:\\tt4','c12','t2','t2.txt')

# os.path.splitext()切割扩展名，以最后一个“.”号做切割
print os.path.splitext('D:\\cmp\\c3.txt')
print os.path.splitext('D:\\cmp\\c3')
# os.path.splitdrive()切割驱动器
print os.path.splitdrive('D:\\cmp\\c3.txt')

# atime：access time 上一次做存取的时间
# ctime：change time 改变文件的时间，改变文件名称等的时间，或者新建的时间点
# mtime：modify time 修改文件的时间--做自动化时调用查看日志的时间，是否被更改

lasttime = os.path.getatime('D:\\cmp\\c3.txt')
print lasttime
formatime = time.localtime(lasttime)
print formatime
print time.strftime('%Y-%m-%d %H:%M:%S',formatime)

# 9、分别针对一个不带绝对路径的文件，和带绝对路径的文件，
# 还有一个没有后缀的文件，调用os.path.splitext 函数

print os.path.splitext('D:\\cmp\\c3.txt')
print os.path.splitext('c3.txt')
print os.path.splitext('D:\\cmp\\c3')

# 10、新建一个文件，之后保存，10秒之后给文件新加内容保存，
# 10s之后修改文件内容保存。分别调用获取atime、ctime、mtime的函数，
# 并且打印出来他们的格式化时间。


filepath = 'D:\\cmp\\'
with open(filepath+'time2.txt','w'):
    pass
time.sleep(10)
with open(filepath+'time2.txt','w') as fp:
    fp.write('第一次加内容')
time.sleep(10)
with open(filepath+'time2.txt','a') as fp:
    fp.write('\n'+'第二次加内容')

atime1 = os.path.getatime('D:\\cmp\\time2.txt')
ctime1 = os.path.getctime('D:\\cmp\\time2.txt')
mtime1 = os.path.getmtime('D:\\cmp\\time2.txt')

aformatime = time.localtime(atime1)
cformatime = time.localtime(ctime1)
mformatime = time.localtime(mtime1)

print u'atime:',time.strftime('%Y-%m-%d %H:%M:%S',aformatime)
print u'ctime:',time.strftime('%Y-%m-%d %H:%M:%S',cformatime)
print u'mtime:',time.strftime('%Y-%m-%d %H:%M:%S',mformatime)

for i in sys.argv:
    print i

# 1、关于带参数的python 脚本，判断脚本的第一个参数是否是--help，
# 如果是的话，打印帮助信息，信息自定义。

# if sys.argv[1] == '--help':
#     print '''this is help '''
# else:
#     print 'no help'

if len(sys.argv) > 2 or len(sys.argv) == 1:
    print ' wrong params,help info:'
    print ' --help:show help info'
    print ' xxxx'
if sys.argv[1]=='--help':
    print 'help info'
    print '--help:show help info'
    print '  xxx'
else:
    print 'error '







