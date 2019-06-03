# encoding=utf-8
import csv

# 读取本地CSV文件信息
date = csv.reader(open('info.csv','r'))

# 循环输出每一行信息
for user in date:
    print u'用户的邮箱：',user[1]


