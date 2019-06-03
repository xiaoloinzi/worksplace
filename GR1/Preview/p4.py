# encoding=utf-8
listA = [1,2,3,4,5,6]
listB = ['one','two','three','fow','five','six']
dictA = dict.fromkeys(listA,12)
print dictA

tupleA = (1,2,3,4,5,6)
print tupleA
dictS = {}
zoo = ('wolf','elephant')
newZoo = ('monkey', 'pig', zoo)
for i in newZoo:
    if isinstance(i,tuple):
        for j in i:
            dictS = dict.fromkeys(listA,j)

    else:
        dictS.append(dict.fromkeys(listA,i))
print dictS


tupleA = (1,2,3,4,5,6,7,8,9)
#遍历元组，判断下标是奇数的则放入奇数列表，偶数放入偶数列表
#
list1 = []
list2 = []
for i in range(len(tupleA)):
    if i % 2 == 0:
        list1.append(tupleA[i])
    else:
        list2.append(tupleA[i])
print list1
print list2

tuple1 = tuple(list1)
tuple2 = tuple(list2)
print tuple1
print tuple2

#采用切片的方式
listA = list(tupleA)
print '全部数值',listA
print '奇数坐标',listA[::2]
print '偶数坐标',listA[1::2]
tuple1 = tuple(listA[::2])
tuple2 = tuple(listA[1::2])
print tuple1
print tuple2