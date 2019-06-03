# encoding=utf-8
#1.使用尽可能多的方法实现list去重
import itertools

list1 = [1,7,3,8,3,2,5,6,1,2,3,4]
list2 = ['a','b','c','d','d','a','b','f']
list3 = []
list4 = [1,7,3,8,3,2,5,6,1,2,3,4]
dict1 = {}

for i in list1:
    if i not in list3:
        list3.append(i)
print list3

list5 = list(set(list1))
print list5


for i in list1:
    while list1.count(i)>1:
        del list1[list1.index(i)]
print list1

list2.sort()
s = itertools.groupby(list2)

for a,b in s:
    print a,

c = lambda x,y:x if y in x else x + [y]
print '\n',reduce(c,[[],]+list4)

# 16.求所有的水仙花数
# for a in range(1,101):
#     for b in range(101):
#         for c in range(101):
#             if a*100 + b*10 + c == a**3 + b**3 + c**3:
#                 print a*100 + b*10 + c