# encoding=utf-8
import os,time,shutil
from datetime import datetime
# 11. 查找某个目录下是否存在某个文件名

file_path = 'D:\\tmp'
str1 = raw_input(u'输入你要查找的文件：')
for i in os.listdir(file_path):
    if i == str1+'.txt' or str1== i:
        print u'存在文件：',i
        exit()
else:
    print u'找不到你要查找的文件'

# 老师的方法：os.walk()

list1 = list(os.walk('D:\\tmp'))
fileName = 't23.txt'
dirName = 'test0827.txt'
for root,dirs,files in list1:
    if dirName in dirName:
        print '%s dir exist'%dirName
    if fileName in files:
        print '%s file exist'%fileName
        print root+files


# 12. 用系统命令拷贝文件
file_path = 'D:\\cmp'
os.chdir(file_path)
with open('score1.txt','w'):
    pass
os.system("copy %s %s"%('score1.txt','score2.txt'))
print os.listdir(file_path)

# 老师的方法：os.system('copy')
os.system('copy D:\\tmp\\t23.txt D:\\tmp\\t999.txt')


# 13.输入源文件所在路径和目标目录路径， 然后实现文件拷贝功能

file1 = raw_input(u'请输入源文件的路径（不同目录之间请用"\\"隔开：')
file2 = raw_input(u'请输入目标的路径（不同目录之间请用"\\"隔开：')
shutil.copy(file1,file2)
shutil.copytree(file1,file2)

# 老师的方法：
# 1、读取源文件
# 2、写入文件

def copy(resF,desF):
    resF = os.path.normpath(resF)
    desF = os.path.normpath(desF)
    if not os.path.exists(resF):
        print 'file not exists'
        return False
    elif resF == desF:
        print 'desF error'
        return False
    elif os.path.exists(desF):
        while True:
            print u'覆盖%s吗？(y/n)'%desF,
            inputVar = raw_input().lower()
            if inputVar == 'n':
                print u'文件已存在，复制0个文件'
                return False
            elif inputVar == 'y':
                os.remove(desF)
                break
            else:
                continue
    with open(resF) as fp:
        content = fp.read()
    with open(desF,'w') as fp:
        fp.write(content)
    print u'已复制一个文件'
    return True

if __name__=='__main__':
    copy('D:\\tmp\\t23.txt','D:\\tmp\\t1234.txt')




# 14.遍历某个目录下的所有图片， 并在图片名称后面增加_xx
str1 = ('.bmp','.jpg','.jpeg','.png','.gif')
file_path = 'D:\\cmp'
os.chdir(file_path)
for i in os.listdir(file_path):
    if os.path.splitext(i)[1] in str1:
        print os.path.splitext(i)[0]
        os.rename(i,os.path.splitext(i)[0]+'_xx'+os.path.splitext(i)[1])

# 老师的方法：
# 1、找到文件：os.walk()
# 2、修改文件的名称--os.rename()
rootPath = 'D:\\tmp'
picEnds = ['.jpg','.jpdg','.bpm','.png','.gif']
for root,dirs,files in os.walk(rootPath):
    for f in files:
        if os.path.splitext(f)[1] in picEnds:
            fileName = os.path.join(root,f)
            fSplit = os.path.splitext(fileName)
            newFile = fSplit[0]+'_xx'+fSplit[1]
            os.rename(fileName,newFile)


# 15、 遍历指定目录下的所有文件， 找出其中占用空间最大的前3个文件

file_path = 'D:\\cmp\\'
dict1 = {}
for i in os.listdir(file_path):
    dict1[i] = [os.path.getsize(file_path+i)]
print sorted(dict1.items(),key=lambda e:e[1],reverse=True)[:3]

# 老师的方法：
# 数据结构：
# {fileName：size}
# 算法：
# 1、os.walk()遍历指定的目录
# 2、得到每个文件的占用空间大小存储在字典中
# 3、sorted进行排序
def findMax(dirPath):
    fileSizeDict = {}
    if os.path.exists(dirPath):
        for root,dirs,files in os.walk(dirPath):
            for f in files:
                filePath = os.path.join(root,f)
                fileSizeDict[filePath] = os.path.getsize(filePath)
        fileList = sorted(fileSizeDict.items(),key=lambda i:i[1],reverse=True)
        return fileList[:3]
    else:
        print 'die not exists'
        return -1
if __name__=='__main__':
    rootDir = 'D:\\tmp'
    print findMax(rootDir)


# 16、 过滤py源码中的#注释， 另存为文件result.py， 并执行result.py，
# 断言是否执行成功

file_path = 'D:\\cmp\\py.py'
os.chdir('D:\\cmp\\')
with open(file_path,'r') as fp:
    lista = fp.readlines()
    for i in lista:
        for j in i:
            if j != '#':
                with open('result.py','a') as xf:
                    xf.write(j)

            else:
                with open('result.py','a') as xf:
                    xf.write('\n')
                break
assert not os.system('python %s'%('result.py')),u'断言'

# 老师的方法：
# 1、把注释去掉--1）保留第一行的编码注释，2）去掉#为开始的注释；3）去掉#不是开始的注释
# 2、写一个新的文件
# 3、执行文件并进行断言

def fileerFile(filePath,desFile):
    if os.path.exists(filePath):
        with open(filePath) as fp:
            contentList = fp.readlines()
        with open(desFile,'w') as fp:
            fp.write('#encoding=utf-8\n')
            for line in contentList:
                try:
                    indexVal = line.index('#')
                    code = line[:indexVal]
                except:
                    fp.write(line+'\n')
                else:
                    if code is not '':
                        fp.write(code+'\n')
filePath = 'D:\\tmp\\z.py'
desFile = 'D:\\tmp\\result.py'
fileerFile(filePath,desFile)
res = os.system('python %s'%desFile)
assert res == 0



# 17、 文件访问， 提示输入数字 N 和文件 F, 然后显示文件 F 的前 N 行.

stra = raw_input(u'如果文件及前n行，以逗号隔开：')
strb = stra.split(',')
num1 = 0
for i in xrange(int(strb[1])):
    with open(strb[0],'r') as fp:
        fp.seek(num1)
        print fp.readline()
        num1 = fp.tell()

# 老师的方法：
def visitFile(fileName, lineNum):
    if os.path.exists(fileName):
        with open(fileName) as fp:
            contentList = fp.readlines()
        return ''.join(contentList[:lineNum])
    else:
        print 'file not exists'

print visitFile('D:\\tmp\\t23.txt',5)



# 18、 从命令行接受1个路径如： c:\a\b\c\1.py, 实现1个函数创建
# 目录a\b\c,创建文件1.py， 实现1个函数删除已创建的目录及文件

file_path = 'c:\\a\\b\\c'
file1 = '1.py'
def ChJian(file_path,file1):
    os.makedirs(file_path)
    os.chdir(file_path)
    list1 = ['import os \n',"file1 = r'\\1.py'\n","file_path = r'c:\\a\\b\\c'\n",
'def ShChu(file_path,file1):\n'
'    os.remove(file_path+file1)\n',
'    os.removedirs(file_path)\n',
'ShChu(file_path,file1)']
    with open(file1,'w') as fp:
        for i in list1:
            fp.write(i)
ChJian(file_path,file1)

os.system('python c:\\a\\b\\c\\1.py')

# 老师的方法：
# 算法：
# os.path.dirname()--得到路径名
# os.makedirs(dir)--创建路径
# os.remove()--删除文件
# os.removedirs()--删除多层文件


# 19、 有一个ip.txt， 里面每行是一个ip， 实现一个函数，
# ping 每个ip的结果， 把结果记录存到ping.txt中，
# 格式为ip:0或ip:1 ， 0代表ping成功， 1代表ping失败

with open('D:\\cmp\\ip.txt','a') as fp:
    for i in xrange(50):
        fp.write('192.168.1.'+str(i)+'\n')

def PingIp(ipfile,pingfile):
    with open(ipfile,'r') as fp:
        # strIp = fp.readlines()
        for i in fp.readlines():
            with open(pingfile,'a') as xf:#没有必要放到循环中，浪费性能
                if os.system("ping %s"%i):
                    xf.write(i.strip()+':1'+'\n')
                else:
                    xf.write(i.strip()+':0'+'\n')

file1 = 'D:\\cmp\\ip.txt'
file2 = 'D:\\cmp\\ping.txt'
PingIp(file1,file2)

# 老师的方法：
# 算法：
# ret = os.system('ping xxxx')--执行文件中ip，并返回值进行判断
def pingIP(ipFile,resFile):
    with open(ipFile) as fp:
        ipList = fp.readlines()
    with open(resFile) as fp:
        for i in ipList:
            command = 'ping '+i.strip()
            ret = os.system(command)
            fp.write(i.strip()+':'+str(ret)+'\n')
ipFile = 'D:\\tmp\\ip.txt'
resFile = 'D:\\tmp\\ping.txt'
pingIP(ipFile,resFile)



# 20、 实现DOS命令执行功能， 接受输入命令并执行，
# 然后把执行结果和返回码打印到屏幕

str1 = raw_input(u'输入命令：')
str2 = os.popen(str1).readlines()
for i in str2:
    print i.decode('gbk')

# 老师的算法：
# ret = os.system()
def func1():
    while True:
        sysCmd = raw_input('input the cmd(exit:e')
        if sysCmd == 'e':
            ret = os.system(sysCmd)
            print 'the return of cmd %s is %d'%(sysCmd,ret)
        else:
            break
        func1()


# 21、 文件访问
# 访问一存在多行的文件， 实现每隔一秒逐行显示文本内容的程序，
# 每次显示文本文件的 5行, 暂停并向用户提示“ 输入任意字符继续” ，
# 按回车键后继续执行， 直到文件末尾。显示文件的格式为：
# [当前时间] 一行内容， 比如：
# [2016-07-08 22:21:51] 999370this is test0827.txt
with open('D:\\cmp\\ip.txt') as fp:
    info = fp.readlines()
    num = 0
    for i in info:
        if num%5==0 and num != 0:
            stra = raw_input(u'输入任意字符继续：')
        formatTime = time.localtime()
        str1 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        time.sleep(1)
        print '[',str1,']',i
        num +=1


# 老师的算法：
# 1、读取文件，列表存储
# 2、判断是否满五行
# 3、显示内容
def printFile(filePath):
    with open(filePath) as fp:
        contentList = fp.readlines()
    times = 0
    for i in contentList:
        if times%5 == 0 and times:
            while raw_input(u'请输入任意字符继续：'.encode('utf-8')) == '':
                continue
            times = 0
            continue
        else:
            now = datetime.now()
            print '['+now.strftime('%Y-%m-%d %H:%M:%S')+']'+i,
            time.sleep(1)
            times +=1
    print u'文件已读完'
filePath = 'D:\\tmp\\t23.txt'
printFile(filePath)



