# encoding=utf-8
import os

# 【Python每日一练】文件中存在三行数据分别为
# key1,value1,value2
# key2,value2,value2
# key3,value3,value3
# 输入一个字符和行号，将输入的字符加入到对应行的后面，需要以逗号隔开，
# 如果该行第四个位置已经存在数据则进行修改操作，比如key3,value3,value3,value3,
# 再次输入value4和3后，更新对应的值为key3,value3,value3,value4,
# 始终保证每一行只有四个数据，这里不考虑输入包括逗号的情况

def makefile(filepath):
    stra = raw_input(u"输入一个字符和行号(以逗号隔开）:")
    lista = stra.split(',')
    if int(lista[1]) < 1 or int(lista[1]) > 3:
      print u"输入的行号不在1-3内"
    listb = []
    with open(filepath,'r') as fp:
        lines = fp.readlines()
        for i in xrange(len(lines)):#0,1,2
            listb.append(lines[i].split(','))
            if lista[1] == listb[i][0]:
                if len(listb[i]) < 4:
                    listb[i].append(lista[0])
                else:
                    listb[i][3] = lista[0]
    with open(filepath,'w') as ft:
        for i in xrange(len(listb)):#0,1,2
            for j in xrange(len(listb[i])):
                s = listb[i][j].strip('\n')
                if j == len(listb[i])-1:
                    ft.write(s+"\n")
                else:
                    ft.write(s+",")
if __name__=='__main__':
    makefile("0731_01.txt")





















