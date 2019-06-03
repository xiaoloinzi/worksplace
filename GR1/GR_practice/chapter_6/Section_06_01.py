# # encoding=utf-8
import os,time,shutil
# 1.基础题：
# 检验给出的路径是否是一个文件：
# 检验给出的路径是否是一个目录：
# 判断是否是绝对路径：
# 检验给出的路径是否真地存:
file_path ='D:\\tmp\\t23\\t2.txt'
if os.path.isfile(file_path):
    print u'给出的路径是一个文件！'
if not os.path.isdir(file_path):
    print u'给出的路径不是一个目录！'
if os.path.isabs(file_path):
    print u'给出的路径是绝对路径！'
if os.path.exists(file_path):
    print u'给出的路径是真地存'


# 2.返回一个路径的目录名和文件名
file_path ='D:\\tmp\\t23\\t2.txt'
print u'目录名：',os.path.split(file_path)[0],u'文件名：',os.path.split(file_path)[1]

# 3.分离文件名与扩展名
print u'分离t2.txt的文件名与扩展名：'
print os.path.splitext('t2.txt')


# 4.找出某个目录下所有的文件， 并在每个文件中写入“ gloryroad”
file_path ='D:\\tmp\\'
for i in os.listdir(file_path):
    if os.path.isfile(file_path+i):
        with open(file_path+i,'a') as fp:
            fp.write('\ngloryroad')


# 算法：
# os.walk()--root,dirs,files
# os.path.walk()

dirpath = "D:\\tmp"
for root,dirs,files in os.walk(dirpath):
    for f in files:
        filepath = os.path.join(root,f)
        with open(filepath,'a') as fp:
            fp.write('gloryroad')




# 5.如果某个目录下文件名包含txt后缀名， 则把文件后面追加写一行“被我找到了！ ”
file_path ='D:\\tmp\\t1\\'

for i in  os.listdir(file_path):
    if os.path.isfile(file_path+i):
        if os.path.splitext(i)[1] == '.txt':
            with open(file_path+i,'a') as fp:
                fp.write('\n被我找到了！')

# 老师：
# 算法：
# os.walk()
# root,dirs,files
# 1)newName
# 2)os.rename
# dirpath = 'D:\\tmp\\t2'
# for root,dirs,files in os.walk(dirpath):
#     for f in files:
#         filepath = os.path.join(root,f)
#         if f.endswith('.txt'):
#             fileName,expandName = os.path.splitext(f)
#             newFileName = os.path.join(root,fileName+u'被我找到了'.encode('gbk')+expandName)
#             os.rename(filepath,newFileName)
#             print newFileName
dirPath = 'e:\\tmp\\t2'
for root,dirs,files in os.walk(dirPath):
    for f in files:
        filePath = os.path.join(root,f)
        if f.endswith('.txt'):
            # fileName,expandName = os.path.splitext(f)
            # newFileName = os.path.join(root,fileName+u'被我找到了'.encode('gbk')+expandName)
            # os.rename(filePath, newFileName)
            # print newFileName
            with open(filePath, 'a') as fp:
                fp.write(u'被我找到了'.encode('gbk'))

# 6. 命题练习:
# 1） 一个目录下只有文件（ 自己构造） ， 拷贝几个文件（ 手工完成）
# 2 ） 用listdir函数获取所有文件， 如果文件的创建时间是今天，
# 那么就在文件里面写上文件的路径、 文件名和文件扩展名
# 3） 如果不是今天创建（ 获取文件的创建时间， 并转化为时间格式，
# 判断是否今天） ，请删除
# 4 ） 计算一下这个程序的执行耗时
file_path = 'D:\\cmp\\'
localTime = time.localtime()
sineTime = time.clock()
for i in os.listdir(file_path):
    print i
    fisrt = os.path.getctime(file_path+i)
    fisrtTime = time.localtime(fisrt)
    if localTime[:3]== fisrtTime[:3]:
        with open(file_path+i,'w') as fp:
            fp.write(''.join(os.path.split(file_path+i))+'\n')
            fp.write(os.path.splitext(file_path+i)[1])
    else:
        os.remove(file_path+i)
newTime = time.clock()
print u'程序的执行耗时为：',newTime-sineTime









# 7.删除某个目录下的全部文件
file_path ='D:\\tmp\\t23\\'
for i in  os.listdir(file_path):
    if os.path.isfile(file_path+i):
        os.remove(file_path+i)


# 8.统计某个目录下文件数和目录个数

file_path ='D:\\tmp\\t1\\'
filenum = 0
dirnum = 0
for i in  os.listdir(file_path):
    if os.path.isfile(file_path+i):
        filenum += 1
    else:
        dirnum += 1
print u'文件数:',filenum,u'目录个数:',dirnum


# 9.删除某个目录下的全部文件(仅限一级目录)

file_path = 'D:\\tmp'
os.chdir(file_path)
# print os.getcwd()
os.chdir(os.pardir)
file_path = os.getcwd()
# print file_path
for i in  os.listdir(file_path):
    if os.path.isfile(file_path+i):
        # print i
        os.remove(file_path+i)

# 10.使用程序建立一个多级的目录， 在每个目录下，
# 新建一个和目录名字一样的txt文件
str1 = os.makedirs('D:\\dmp\\emp\\smp\\simp\\wmp')
str3 = str1
for i in xrange(1,len(str1.split('\\'))+1):
    file1 = str1.split('\\')[-i] + '.txt'
    os.chdir(str3)
    with open(file1,'w') as fp:
        pass
    os.chdir(os.pardir)
    str3 = os.getcwd()
