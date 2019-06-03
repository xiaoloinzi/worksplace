# encoding=utf-8
# 不能用列表做key值
dict1 = {'Name':'Zara','Age':7,'Class':'First'}
print dict1
#
# 1、访问字典中的值
# 2、修改字典中的值
# 3、向字典中增加key-value对
# 4、删除字典中的条目
# 5、清空字典
# 6、新增一个条目，key是列表，看是否报错，如果报错的话，是什么原因报错

print dict1['Name']
dict1['Name']='xiugai'
print dict1['Name']
dict1['Add']='zjia'
print dict1
del dict1['Name']
print dict1
# dict1.clear()
print dict1
# dict1[[123]]='123'
for i in dict1.keys():
    print i
for key,value in dict1.items():
    print key,value
dic2 =  {'1':1,'2':2}
print cmp(dict1,dic2)
print str(dict1)
print len(dict1)
print type(dict1)

# sorted(iterable,[cmp[,key[,reverse]]])
user = {'user3':'a','user2':'c','user1':'b'}
print user.items()
sort1 = sorted(user.items(),key=lambda e:e[0],reverse=False)#以key值来排序
print sort1
sort1 = sorted(user.items(),key=lambda e:e[1],reverse=False)#以value值来排序
print sort1

# 5、将一个多重嵌套的列表的元素进行互换，存到另一个同等维度的嵌套列表中，
# 例如：[[1,2,3],[4,5,6]]互换后变成[[1,4],[2,5],[3,6]]
# 1、元素个数由谁决定：由子列表的长度决定
# 2、元素值由谁决定：由[1,4,7,10]
lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,23]]
def change(listVal):
    valLen = len(listVal[0])
    newList = []
    for i in xrange(len(listVal)):
        for j in xrange(valLen):
            if i == 0:
                newList.append([listVal[i][j]])
            else:
                newList[j].append(listVal[i][j])
    return newList
print change(lista)

















