# encoding=utf-
# 1. 输入1-127的ascii码并输出对应字符
from pkg_resources._vendor.pyparsing import range

list1 = []
for i in range(128):
    char1 = chr(i)
    print '%d\t%s'%(i,char1)


