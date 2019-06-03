# encoding=utf-8
import os,sys,shutil

with open('D:\\tmp\\t1.txt','r') as fp:
    pass
#with 语句不能被捕获异常，with下面的子句能被捕获异常

class opened(object):
    def __init__(self,fileName):
        self.handle = open(fileName)
    def __enter__(self):
        print 'enter __enter__ method'
        return self.handle
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print 'No Exception'
            self.handle.close()
        else:
            print "Exception occured!"
            print "Exception type:",exc_type
            print "Exception value:",exc_val
            print 'exc_tb:',exc_tb
            self.handle.close()
            return False
with opened('D:\\tmp\\t1.txt') as fp:
    for line in fp.readlines():
        print line
    raise Exception('bad imput')


def finFile(arg,dirname,files):
    print '***********************'
    print arg
    print dirname
    print files

os.path.walk('D:\\Apache24',finFile,(1,2))

# 6、使用os.path.walk,在每个目录下面，分别打印文件名 和
# 目录名，用列表的方式存储及打印

def finFile1(arg,dirname,files):
    print '***********************'
    # print arg
    # print dirname
    # print files
    filelist = []
    dirlist = []
    for i in files:
        if os.path.isfile(os.path.join(dirname,i)):
            filelist.append(i)
        else:
            dirlist.append(i)
    print 'root:',dirname
    print 'filelist:',filelist
    print 'dirlist:',dirlist
#
os.path.walk('D:\\Apache24',finFile1,(1,2))


# break、return
# sys.exit()可以指定一个值进行退出，默认值为0
# sys.argv---获取从外部传过来的参数
# 标准输入--sys.stdin--对应的是在cmd界面进行操作

count = 1
while True:
    line = sys.stdin.readline()
    if not line:
        break
    print '%s:%s'%(count,line)
    count += 1

sys.stdout.write()
sys.stderr.write()--错误信息
sys.stdout.write('glory road!')
sys.stderr.write('glory road!')

shutil.copyfile('D:\\tmp\\t22\\t1.txt','D:\\tmp\\t21\\t2.txt')
shutil.move('D:\\tmp\\t22\\t1.txt','D:\\tmp\\t22\\t6.txt')
shutil.copy('D:\\tmp\\t22\\t2.txt','D:\\tmp\\t22\\t1.txt')
shutil.copytree('D:\\tmp\\t22','D:\\tmp\\t29')

# 7、已经存在文件tmp\t1\t1.txt
# 复制该文件到tmp\t2\t2.txt
# 移动文件tmp\t1\t1.txt 到tmp\t2
# 拷贝文件tmp\t2\t1.txt 到tmp\t1
# 通过copytree 拷贝tmp 目录为tmp2
# 通过os.walk 遍历 tmp2 目录并且打印
shutil.copyfile('D:\\tmp\\t1\\t1.txt','D:\\tmp\\t2\\t2.txt')
shutil.move('D:\\tmp\\t1\\t1.txt','D:\\tmp\\t2')
shutil.copy('D:\\tmp\\t2\\t1.txt','D:\\tmp\\t1')
shutil.copytree('D:\\tmp','D:\\tmp2')

for i,j ,s in os.walk('D:\\tmp2'):
    print i
    print j
    print s
    print '***********'