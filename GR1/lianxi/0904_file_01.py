# encoding=utf-8
import linecache


# with open('D:\\tmp\\c\\t4.txt','a+') as fp:
#     line = fp.read(48)
#     print line
#     print fp.tell()
#     fp.truncate()
#     print fp.tell()


# with open('D:\\tmp\\c\\t3.txt','a+') as fp:
#     for i in xrange(6):
#         line = fp.readline()
#     fp.truncate()
#     fp.seek(0)
#     lines = fp.read()
#     print lines

# with open('D:\\tmp\\c\\t5.txt','a+') as fp:
#     fp.seek(50)
#     print fp.tell()
#     fp.truncate()
# truncate没有指定大小则从当前位置开始截取，指定位置后则在指定位置截取
# with open('D:\\tmp\\c\\t56.txt','a+') as fp:
#     fp.truncate(50)

# filename = 'D:\\tmp\\c\\t5.txt'
# fileContent = linecache.getlines(filename)
# print fileContent
# line2 = linecache.getline(filename,2)
# print line2
# print linecache.updatecache(filename)
# linecache.clearcache()
# list1 = []
# for i in xrange(20):
#     list1.append(str(i+1)+"abcd\n")
# with open('D:\\tmp\\c\\t5.txt','w') as fp:
#     fp.writelines(list1)
#
# for i in xrange(1,20,2):
#     print linecache.getline(filename,i)
# print linecache.getlines(filename)[::2]

# def newFile(filename):
#     with open(filename,'r') as fp:
#         line = fp.readlines()
#     list1 = []
#     for i in line:
#         if i != "\n":
#             list1.append(i)
#     print list1
#     with open('D:\\tmp\\c\\t6.txt','w') as fp:
#         fp.writelines(list1)
#
# newFile(filename)
outfile = 'D:\\tmp\\c\\t8.txt'

# def func1(infile,outfile):
#     infp = open(infile,'r')
#     outfp = open(outfile,'w')
#     lines = infp.readlines()
#     for i in lines:
#         if i.split():
#             outfp.write(i)
#     infp.close()
#     outfp.close()
#
# func1(filename,outfile)

# fp = open(outfile,'w+')
# fp.write('你好吗')
# fp.seek(0)
# print fp.read()
# fp.close()
# lines = ''
# fp = open('D:\\tmp\\c\\t7.txt','r')
# lines = fp.read()
# filrs = "0"+lines[:2]+"2"+lines[2:4]+"4"+lines[4:]
# fp.seek(0)
# lines = lines + str(fp.tell())+fp.read(1)
# fp.seek(2)
# lines = lines + str(fp.tell())+fp.read(2)
# fp.seek(4)
# lines = lines + str(fp.tell())+fp.read()
# fp.close()
# print filrs
# fp = open('D:\\tmp\\c\\t10.txt','w')
# fp.writelines(filrs)
# fp.close()

import cPickle as p

shopListFile = 'D:\\tmp\\c\\t11.txt'
shopList = ["lin","chun","lian"]
fp = open(shopListFile,'w')
pick = p.dump(shopList,fp)
fp.close()
del shopList
fp = open(shopListFile)
storeList = p.load(fp)
print 'after load,the list is:',storeList



























