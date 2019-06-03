# encoding=utf-8
list = [12,'ldfd',2.3]
print list

shoplist = ['apple','mongo','carrot','banana']
print 'I have',len(shoplist),'item to buy'

print type(shoplist)

for item in shoplist:
    print item

shoplist.append('rice')
print u'新购物清单',shoplist

shoplist.sort()#sort方法只能先排序，再输出。
print u'排序后的购物清单',shoplist
#打印字符串，整数，浮点数，及uncod字符串的值及类型
list1 = ["zi fu cuang",3,2.3,u'你好']
print list1
for i in list1:
    print i,type(i)
#使用列表的extend（）方法进行列表的追加
listA = [1,2,3]
listB = [9,6,4]
listA.extend(listB)
print u'新的列表',listA
#多维列表，对于列表再用一个中括号表示，
listC = [[1,2,3,4],[21,22,23,24]]
print u'第一个元素',listC[0]
print u'访问第一个元素的第二个数值',listC[0][1]
#使用del进行列表的删除
print u'删除之前的列表',listC
del listC[0]
print u'删除之后的列表',listC

# isinstance(listC，list)判断listC是否是列表
if isinstance(listC,list):
    print 'OK'

lists = [[1,2,456,4],23,[4567]]

for i in lists:
    if isinstance(i,list):
        for s in i:
            print s
    else:
        print i
#不使用isinstance 方法遍历列表
#思路：遍历一遍列表，获得元素，判断列表元素，则再遍历一遍，否则直接打印
for i in lists:
    if type(i) == list:#使用类型进行判断
        for j in i:
            print j
    else:
        print i

#切片操作
listE = [1,2,3,4,5,6]
#listA[startpoint:endpoind:step]==[开始的元素（包含）：结束的元素（不包含）：步长（默认为1），步长为2，就会间隔2个取数值]
print listE[0:4:1]
print u'什么都不指定的时候',listE[::]
print u'步长指定为-1指定的时候',listE[::-1]
listr = 'abcdfdrg'

print listr[::-1]

for i in listr[::-1]:
    print i
#倒序排列/从后面往前面排序
j = 1
listq = []
for i in listr:
    print listr[len(listr)-j]
    listq.append(listr[len(listr)-j])
    j = j+1
print listq







print ''.join(listq)
#列表生成器rang(1,10,2)从1开始，长度为10，步长为2
list1 = range(1,10,2)
print list1

list2 = [x*x for x in range(10)]
print list2

list3 = [24,456,7565,45]
#对于列表list3要得到一个新的列表并且每个值都小于之前列表相应值得10
list4 = [x-10 for x in list3]
print list4
#找到列表中相同的和不同的元素
list5 = [1,3,4,'a','b',[8,9,6]]
list6 = [1,'a',8]
# list7 = []
# for i in list5:
#      for j in list6:
#          if i == j:
#              list7.append(i)
# print list7
#解两个列表中不同的元素
list7 = []
list8 = []
for i in list5:
    if i in list6:
        list7.append(i)
    else:
        list8.append(i)
print u'打印出两个列表中不同的元素',list8
print u'打印出列表中相同的元素',list7