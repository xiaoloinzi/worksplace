# encoding=utf-8
import logging
import logging.handlers
import logging.config
from datetime import datetime
import time
import os
# 日志模块

# rootlog = logging.getLogger()
# rootlog.setLevel(logging.DEBUG)
# # backupCount=日志文件的个数
# fh = logging.handlers.RotatingFileHandler('D:\\tmp\\log\\'+str(time.strftime("%Y%m%d",time.localtime()))+".txt",maxBytes=512,backupCount=3)
# fmt = logging.Formatter('%(asctime)s|%(name)s|%(filename)s|%(lineno)d|%(levelname)s|%(message)s')
# fh.setFormatter(fmt)
# rootlog.addHandler(fh)
#
# for i in xrange(1000):
#     rootlog.info('this is test0827.txt log')
#
# print time.localtime()
# print time.strftime("%Y%m%d",time.localtime())



# 【python每日一练】编写一个程序，创建一个当前日期文件夹，例如20170823，
# 在该文件夹下按照日期生成一个文件，并向文件中写入数据，文件最大不超过1M，
# 如果超过1M，则将文件进行备份，要求备份的文件名称后面加一个.1或者.2,
# 例如现在有个文件20170823.txt,写入后文件如果大于1M，文件名称变为20170823.1.txt,
# 如果存在文件20170823.1.txt,则将名称修改为20170823.2.txt，以此类推，
# 最终文件的数量最大为20170823.10.txt

class FileWrite(object):
    def __init__(self,maxBytes,fileCount):
        self.one = str(time.strftime("%Y%m%d",time.localtime()))
        self.path = "D:\\tmp\\"+self.one
        if not os.path.exists(self.path):
            os.mkdir("D:\\tmp\\"+self.one)
        self.file = self.one+".txt"
        self.maxBytes = maxBytes
        self.fileCount = fileCount
    def writeFile(self,stra):
        paths = self.path+"\\"+self.file
        if not os.path.exists(paths):
            with open(paths,'a+'):
                pass
        while os.path.getsize(paths) < self.maxBytes:
            with open(paths,'a+') as fp:
                fp.write(stra)
        for i in range(self.fileCount - 1, 0, -1):
                sfn = self.path+"\\"+"%s.%d" % (self.one, i)+".txt"
                dfn = self.path+"\\"+"%s.%d" % (self.one, i + 1)+".txt"
                if os.path.exists(sfn):
                    if os.path.exists(dfn):
                        os.remove(dfn)
                    os.rename(sfn,dfn)
        dfn = self.path+"\\"+self.one + ".1"+".txt"
        if os.path.exists(dfn):
            os.remove(dfn)
        if os.path.exists(paths):
            os.rename(paths, dfn)
            with open(paths,'a+'):
                pass

if __name__=="__main__":
    osa = FileWrite(1,5)
    for i in xrange(1000):
        osa.writeFile("ssdfs江苏东方航空的说法还是快点发货dfsdfsdfhdjsfhksf")



















# class RotatingFileHandler(object):
#     def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=0):
#         if maxBytes > 0:
#             mode = 'a'
#         self.maxBytes = maxBytes
#         self.backupCount = backupCount
#
#     def doRollover(self):
#         if self.stream:
#             self.stream.close()
#             self.stream = None
#         if self.backupCount > 0:
#             for i in range(self.backupCount - 1, 0, -1):
#                 sfn = "%s.%d" % (self.baseFilename, i)
#                 dfn = "%s.%d" % (self.baseFilename, i + 1)
#                 if os.path.exists(sfn):
#                     if os.path.exists(dfn):
#                         os.remove(dfn)
#                     os.rename(sfn, dfn)
#             dfn = self.baseFilename + ".1"
#             if os.path.exists(dfn):
#                 os.remove(dfn)
#             if os.path.exists(self.baseFilename):
#                 os.rename(self.baseFilename, dfn)
#         if not self.delay:
#             self.stream = self._open()
#
#     def shouldRollover(self, record):
#         if self.stream is None:                 # delay was set...
#             self.stream = self._open()
#         if self.maxBytes > 0:                   # are we rolling over?
#             msg = "%s\n" % self.format(record)
#             self.stream.seek(0, 2)  #due to non-posix-compliant Windows feature
#             if self.stream.tell() + len(msg) >= self.maxBytes:
#                 return 1
#         return 0













