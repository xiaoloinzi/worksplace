# encoding=utf-8
#确认当前的编码是utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


#代码示例：
#-*- coding: UTF-8 -*-
fp1 = open('d:\\testfile.txt', 'r')
#文件是ansi保存（gbk）
info1 = fp1.read()
print type(info1)
print info1 #默认使用gbk编码进行转换，转换
#unicode进行打印
# 已知是 GBK 编码，解码成 Unicode
tmp = info1.decode('GBK')
print isinstance(tmp, unicode)
print isinstance(info1, unicode)
#