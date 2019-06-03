# encoding=utf-8
import os


filepath = os.getcwd()+'/tests/testData/'+"Download.csv"
list1 = []
list2 = []
dicts={}
with open(filepath) as fp:
    line = fp.readlines()
for i in xrange(1,len(line)):
    list1.append(line[i].rstrip('\n').split(','))
for i in xrange(len(list1)):
    list2.append(list1[i][2].split('|'))
for i in xrange(len(list2[0])):
    dicts[list2[0][i].split('=')[0]]=list2[0][i].split('=')[1]
print dicts





















