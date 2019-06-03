# # encoding=utf-8
import os,time,shutil
# 1.基础题：
# 检验给出的路径是否是一个文件：
# 检验给出的路径是否是一个目录：
# 判断是否是绝对路径：
# 检验给出的路径是否真地存:
# file_path ='D:\\tmp\\t23\\t2.txt'
# if os.path.isfile(file_path):
#     print u'给出的路径是一个文件！'
# if not os.path.isdir(file_path):
#     print u'给出的路径不是一个目录！'
# if os.path.isabs(file_path):
#     print u'给出的路径是绝对路径！'
# if os.path.exists(file_path):
#     print u'给出的路径是真地存'

# 2.返回一个路径的目录名和文件名
# file_path ='D:\\tmp\\t23\\t2.txt'
# print u'目录名：',os.path.split(file_path)[0],u'文件名：',os.path.split(file_path)[1]

# 3.分离文件名与扩展名
# print u'分离t2.txt的文件名与扩展名：'
# print os.path.splitext('t2.txt')


# 4.找出某个目录下所有的文件， 并在每个文件中写入“ gloryroad”
# file_path ='D:\\tmp\\'
# for i in os.listdir(file_path):
#     if os.path.isfile(file_path+i):
#         with open(file_path+i,'a') as fp:
#             fp.write('\ngloryroad')


# 5.如果某个目录下文件名包含txt后缀名， 则把文件后面追加写一行“被我找到了！ ”
# file_path ='D:\\tmp\\t1\\'
#
# for i in  os.listdir(file_path):
#     if os.path.isfile(file_path+i):
#         if os.path.splitext(i)[1] == '.txt':
#             with open(file_path+i,'a') as fp:
#                 fp.write('\n被我找到了！')

# 6. 命题练习:
# 1） 一个目录下只有文件（ 自己构造） ， 拷贝几个文件（ 手工完成）
# 2 ） 用listdir函数获取所有文件， 如果文件的创建时间是今天，
# 那么就在文件里面写上文件的路径、 文件名和文件扩展名
# 3） 如果不是今天创建（ 获取文件的创建时间， 并转化为时间格式，
# 判断是否今天） ，请删除
# 4 ） 计算一下这个程序的执行耗时
# file_path = 'D:\\cmp\\'
# localTime = time.localtime()
# sineTime = time.clock()
# for i in os.listdir(file_path):
#     print i
#     fisrt = os.path.getctime(file_path+i)
#     fisrtTime = time.localtime(fisrt)
#     if localTime[:3]== fisrtTime[:3]:
#         with open(file_path+i,'w') as fp:
#             fp.write(''.join(os.path.split(file_path+i))+'\n')
#             fp.write(os.path.splitext(file_path+i)[1])
#     else:
#         os.remove(file_path+i)
# newTime = time.clock()
# print u'程序的执行耗时为：',newTime-sineTime

# 7.删除某个目录下的全部文件
# file_path ='D:\\tmp\\t23\\'
# for i in  os.listdir(file_path):
#     if os.path.isfile(file_path+i):
#         os.remove(file_path+i)


# 8.统计某个目录下文件数和目录个数

# file_path ='D:\\tmp\\t1\\'
# filenum = 0
# dirnum = 0
# for i in  os.listdir(file_path):
#     if os.path.isfile(file_path+i):
#         filenum += 1
#     else:
#         dirnum += 1
# print u'文件数:',filenum,u'目录个数:',dirnum


# 9.删除某个目录下的全部文件(仅限一级目录)

# file_path = 'D:\\tmp'
# os.chdir(file_path)
# # print os.getcwd()
# os.chdir(os.pardir)
# file_path = os.getcwd()
# # print file_path
# for i in  os.listdir(file_path):
#     if os.path.isfile(file_path+i):
#         # print i
#         os.remove(file_path+i)

# 10.使用程序建立一个多级的目录， 在每个目录下，
# 新建一个和目录名字一样的txt文件
# str1 = 'D:\\dmp\\emp\\smp\\simp\\wmp'
# str3 = str1
# for i in xrange(1,len(str1.split('\\'))+1):
#     file1 = str1.split('\\')[-i] + '.txt'
#     os.chdir(str3)
#     with open(file1,'w') as fp:
#         pass
#     os.chdir(os.pardir)
#     str3 = os.getcwd()



# 11. 查找某个目录下是否存在某个文件名

# file_path = 'D:\\tmp'
# str1 = raw_input(u'输入你要查找的文件：')
# for i in os.listdir(file_path):
#     if i == str1+'.txt' or str1== i:
#         print u'存在文件：',i
#         exit()
# else:
#     print u'找不到你要查找的文件'


# 12. 用系统命令拷贝文件
# file_path = 'D:\\cmp'
# os.chdir(file_path)
# with open('score1.txt','w'):
#     pass
# os.system("copy %s %s"%('score1.txt','score2.txt'))
# print os.listdir(file_path)

# 13.输入源文件所在路径和目标目录路径， 然后实现文件拷贝功能

# file1 = raw_input(u'请输入源文件的路径（不同目录之间请用"\\"隔开：')
# file2 = raw_input(u'请输入目标的路径（不同目录之间请用"\\"隔开：')
# shutil.copy(file1,file2)

# 14.遍历某个目录下的所有图片， 并在图片名称后面增加_xx
# str1 = ('.bmp','.jpg','.jpeg','.png','.gif')
# file_path = 'D:\\cmp'
# os.chdir(file_path)
# for i in os.listdir(file_path):
#     if os.path.splitext(i)[1] in str1:
#         print os.path.splitext(i)[0]
#         os.rename(i,os.path.splitext(i)[0]+'_xx'+os.path.splitext(i)[1])


# 15、 遍历指定目录下的所有文件， 找出其中占用空间最大的前3个文件

# file_path = 'D:\\cmp\\'
# dict1 = {}
# for i in os.listdir(file_path):
#     dict1[i] = [os.path.getsize(file_path+i)]
# print sorted(dict1.items(),key=lambda e:e[1],reverse=True)[:3]



# 16、 过滤py源码中的#注释， 另存为文件result.py， 并执行result.py，
# 断言是否执行成功

# file_path = 'D:\\cmp\\py.py'
# os.chdir('D:\\cmp\\')
# with open(file_path,'r') as fp:
#     lista = fp.readlines()
#     for i in lista:
#         for j in i:
#             if j != '#':
#                 with open('result.py','a') as xf:
#                     xf.write(j)
#
#             else:
#                 with open('result.py','a') as xf:
#                     xf.write('\n')
#                 break
# assert not os.system('python %s'%('result.py')),u'断言'


# 17、 文件访问， 提示输入数字 N 和文件 F, 然后显示文件 F 的前 N 行.

# stra = raw_input(u'如果文件及前n行，以逗号隔开：')
# strb = stra.split(',')
# num1 = 0
# for i in xrange(int(strb[1])):
#     with open(strb[0],'r') as fp:
#         fp.seek(num1)
#         print fp.readline()
#         num1 = fp.tell()


# 18、 从命令行接受1个路径如： c:\a\b\c\1.py, 实现1个函数创建
# 目录a\b\c,创建文件1.py， 实现1个函数删除已创建的目录及文件

# file_path = 'c:\\a\\b\\c'
# file1 = '1.py'
# def ChJian(file_path,file1):
#     os.makedirs(file_path)
#     os.chdir(file_path)
#     list1 = ['import os \n',"file1 = r'\\1.py'\n","file_path = r'c:\\a\\b\\c'\n",
# 'def ShChu(file_path,file1):\n'
# '    os.remove(file_path+file1)\n',
# '    os.removedirs(file_path)\n',
# 'ShChu(file_path,file1)']
#     with open(file1,'w') as fp:
#         for i in list1:
#             fp.write(i)
# ChJian(file_path,file1)
#
# os.system('python c:\\a\\b\\c\\1.py')




# 19、 有一个ip.txt， 里面每行是一个ip， 实现一个函数，
# ping 每个ip的结果， 把结果记录存到ping.txt中，
# 格式为ip:0或ip:1 ， 0代表ping成功， 1代表ping失败

# with open('D:\\cmp\\ip.txt','a') as fp:
#     for i in xrange(50):
#         fp.write('192.168.1.'+str(i)+'\n')

# def PingIp(ipfile,pingfile):
#     with open(ipfile,'r') as fp:
#         # strIp = fp.readlines()
#         for i in fp.readlines():
#             with open(pingfile,'a') as xf:
#                 if os.system("ping %s"%i):
#                     xf.write(i.strip()+':1'+'\n')
#                 else:
#                     xf.write(i.strip()+':0'+'\n')
#
# file1 = 'D:\\cmp\\ip.txt'
# file2 = 'D:\\cmp\\ping.txt'
# PingIp(file1,file2)


# 20、 实现DOS命令执行功能， 接受输入命令并执行，
# 然后把执行结果和返回码打印到屏幕

# str1 = raw_input(u'输入命令：')
# str2 = os.popen(str1).readlines()
# for i in str2:
#     print i.decode('gbk')


# 21、 文件访问
# 访问一存在多行的文件， 实现每隔一秒逐行显示文本内容的程序，
# 每次显示文本文件的 5行, 暂停并向用户提示“ 输入任意字符继续” ，
# 按回车键后继续执行， 直到文件末尾。显示文件的格式为：
# [当前时间] 一行内容， 比如：
# [2016-07-08 22:21:51] 999370this is test0827.txt
# with open('D:\\cmp\\ip.txt') as fp:
#     info = fp.readlines()
#     num = 0
#     for i in info:
#         if num%5==0 and num != 0:
#             stra = raw_input(u'输入任意字符继续：')
#         formatTime = time.localtime()
#         str1 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#         time.sleep(1)
#         print '[',str1,']',i
#         num +=1