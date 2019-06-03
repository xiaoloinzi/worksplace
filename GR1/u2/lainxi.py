# encoding=utf-8
import linecache
import os
# print linecache.getlines('tuan.txt')[:2]
# print linecache.getline('tuan1.txt',3)
# print linecache.checkcache('tuan1.txt')
# print linecache.updatecache('tuan1.txt')[2:4]
# print linecache.clearcache()

# def delblankline(infile,outfile):
#     infp = open(infile,'r')
#     outfp = open(outfile,'w')
#     lines = infp.readlines()
#     print 'infp.readlines():',lines
#     for li in lines:
#         # print li.split()
#         if li == '\n':
#             print u'空格'
#         if li.split():
#             outfp.write(li)
#     infp.close()
#     outfp.close()
#
# if __name__=='__main__':
#     delblankline('tuan1.txt','tuan2.txt')
#     print '-'*40
#     fp = open('tuan2.txt','r')
#     print fp.read()
#     fp.close()
#
# print '-'*40
# fp = open('tuan1.txt','r')
# alist = []
# for item in fp:
#     if item.strip():
#         alist.append(item)
# fp.close()
# fp = open('tuan3.txt','w')
# fp.writelines(alist)
# fp.close()
#
#
# fp = open('tuan1.txt','r')
# print fp.read()
# fp.close()
#
# print '-'*40
#
# fp = open('tuan3.txt','r')
# print fp.read()
# fp.close()
# fp = open('kong.txt','r')
# s = 0

# for i in fp:
#     s += len(i.replace(',','').split())
#     print i.replace(',','').split()
# print s
#
# fp.close()
#
# print '-'*40
# fp = open('test0827.txt.txt','r')
# wf = open('xin.txt','a')
#
# for i in fp:
#     print i[::-1].split()
#     wf.writelines(i[::-1].split())
#     wf.writelines('\n')
#
# fp.close()
# wf.close()
# fp = open('kong.txt','r')
# wf = open('xin.txt','a')
#
# for i in fp:
#     print i[::-1].split()
#     wf.writelines(i[::-1])
#     wf.writelines('\n')
# fp.close()
# wf.close()
import cPickle as p
# shoplife = 'kong.txt'
# shoplist = ['apple','mango','carrot']
# f = file(shoplife,'w')
# p.dump(shoplist,f)
# f.close()
# del shoplist
# f = file(shoplife)
# storedlist = p.load(f)
# print u'从文件读取的列表对象：',storedlist
#
# writelist = ['apple','mango','carrot']
# fp = open('tuan1.txt','w')
# fp.writelines(writelist)
# fp.close()
# shoplistfile = 'shoplist.data'
# shoplist = ['apple','mango','carrot']
# aniumalist = ['hippo','rabbit']
# f = file(shoplistfile,'w')
# p.dump(shoplist,f)
# p.dump(aniumalist,f)
# f.close()
# del shoplist
# del aniumalist
# f = file(shoplistfile)
# # 那个先第一个读取数据，则永远排第一
# animalist = p.load(f)
# shorelist = p.load(f)
# print animalist
# print shorelist
import os
# print u'当前的工作目录：',os.getcwd()
# os.chdir(r'D:\worksplace\GR1\u2')
# print u'修改后的目录：',os.getcwd()

# print os.curdir
# print os.pardir
# print os.getcwd()
# os.chdir(os.pardir)
# print os.getcwd()
# print os.name
# os.mkdir(r'D:\gloryroad')

from selenium import webdriver

driver = webdriver.Ie()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')






