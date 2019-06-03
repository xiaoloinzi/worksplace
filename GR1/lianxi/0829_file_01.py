# encoding=utf-8
import os
import chardet


# fp = open('D:\\tmp\\c\\t1.txt','w')
# print type(fp)
# print fp
# fp.write('嘎嘎嘎\n')
# fp.write('hello world')
# fp.close()

# fp = open('D:\\tmp\\c\\t1.txt','r')
# content = fp.read()
# print content
# fp.close()


# fp = open("D:\\tmp\\c\\t2.txt",'r')
# content = fp.read()
# fp.close()
# # for i in content:
# print chardet.detect(content)["encoding"]
# print content.decode('gbk')
# print chardet.detect(content)
#
# with open("D:\\tmp\\c\\t1.txt",'r') as fp:
#     print fp.closed
#     comtemt = fp.read()
# print comtemt
# print fp.closed
# print fp.mode
# print fp.name
# print fp.softspace#是否打印空格符

# with open("D:\\tmp\\c\\t2.txt",'w+') as fp:
#     fp.write("hello ")
# if not fp.closed:
#     fp.close()
# with open("D:\\tmp\\c\\t2.txt",'w+') as fp:
#     fp.write("world ")
#     print fp.closed
#     if not fp.closed:
#         fp.close()
#     print fp.closed
# with open("D:\\tmp\\c\\t2.txt",'r') as fp:
#     content = fp.read()
# print fp.closed
# if not fp.closed:
#     fp.close()
# print fp.closed
# print content

# fp = open("D:\\tmp\\c\\t1.txt",'r')
# c1 = fp.readline()
# c2 = fp.readline()
# print c1
# print c2
# list1 = []
# for i in xrange(10000):
#     list1.append(str(i)+"你好hello123456\n")
#
# fp = open("D:\\tmp\\c\\t3.txt",'w+')
# fp.writelines(list1)
# fp.close()

# fp = open("D:\\tmp\\c\\t4.txt",'a')
# fp.write("你好吗\n")
# fp.write("hello\n")
# fp.write("Bu好吗\n")
# fp.close()
# fp = open("D:\\tmp\\c\\t4.txt",'r')
# print fp.readline()
# print fp.tell()


fp = open("D:\\tmp\\c\\t3.txt",'r')
list1 = fp.readlines()
fp.close()
for i in xrange(100):
    print str(i)+":",list1[1]
print '*'*50
fp = open("D:\\tmp\\c\\t3.txt",'r')
sinr = fp.readline()
sine = fp.readline()
fp.close()
for i in xrange(100):
    print str(i)+":", sine
print "*"*50
fp = open("D:\\tmp\\c\\t3.txt",'r')
sinea = fp.readline()
linno = fp.tell()
for i in xrange(100):
    fp.seek(linno)
    print str(i)+":",fp.readline()
fp.close()



























