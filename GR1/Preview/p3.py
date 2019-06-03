# encoding=utf-8


dictB = {'agr':18,'name':'andy'}

for key in dictB.kry():
    print key

for value in dictB.value():
    print value

for key,value in dictB.items():
    print str(key)+'='+str(value)

'''习题1：
找出如下句子中，最长的单词，以及最短的单词，以字典的形式返回，多个值之间以空格隔开。
If you do not learn to think when you are young, you may never learn.
结果：
{‘max’:’xxx xxx’, ‘min’:’x x’}'''

str = "If you do not learn to think when you are young, you may never learn"

list1 = str.replace(',','').replace('.','').split(' ')
dicr = {}
#数据结构就是用来存储数据的结构
maxlist = [list1[0]]

for i in list1:
    if len(i) > len(maxlist[0]):
        maxlist = []
        maxlist.append(i)
    elif len(i) == len(maxlist[0]):
        maxlist.append(i)


print list1
print maxlist







