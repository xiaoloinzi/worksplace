# encoding=utf-8


# 冒泡排序和插入排序
#
def bubbleSort(listx):
    xLen = len(listx)
    for i in xrange(xLen-1):
        for j in xrange(xLen-1-i):
            if listx[j] > listx[j+1]:
                # tmp = listx[j]
                listx[j],listx[j+1]= listx[j+1],listx[j]
                # listx[j+1] = tmp
            print listx
    return listx
list1 = [2,3,1,0,66,87,34,2,54,23,12,0]
print bubbleSort(list1)

#
# 1、1行代码搞定数据交换；
# 2、从大到小做冒泡排序
def bubbleSort(listx):
    xLen = len(listx)
    for i in xrange(xLen-1):
        for j in xrange(xLen-1-i):
            if listx[j] > listx[j+1]:
                # tmp = listx[j]
                listx[j],listx[j+1]= listx[j+1],listx[j]
                # listx[j+1] = tmp
            # print listx
    return listx
list1 = [2,3,1,0,66,87,34,2,54,23,12,0]
print bubbleSort(list1)
# 从大到小
def bubbleSort(listx):
    xLen = len(listx)
    for i in xrange(xLen-1):
        for j in xrange(xLen-1-i):
            if listx[j] < listx[j+1]:
                # tmp = listx[j]
                listx[j],listx[j+1]= listx[j+1],listx[j]
                # listx[j+1] = tmp
            # print listx
    return listx

list1 = [2,3,1,0,66,87,34,2,54,23,12,0]
print bubbleSort(list1)

# 计算时间复杂度
# 1：n-1
# 2:n-2
# 3:n-3
# .....
# 比较总次数：n-1:1---1+2+3+....+(n-1)=(n*(n-1))/2
#
# ===O(n^2)
# O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<....<O(2^n)<O(n!)--重点背

# 插入排序

def insertSort(listx):
    xLen = len(listx)
    for i in xrange(1,xLen):
        key = listx[i]
        j = i-1
        while j >= 0:
            if listx[j] > key:
                # listx[j+1] = listx[j]
                # listx[j] = key
                listx[j+1],listx[j] = listx[j],key
                j -= 1
            else:
                break
    return listx

if __name__=='__main__':
    list1 = [2,3,1,0,66,87,34,2,54,23,12,0]
    print insertSort(list1)

# 不要使用key进行插入排序
def insertSort(listx):
    xLen = len(listx)
    for i in xrange(1,xLen):
        # key = listx[i]
        j = i-1
        while j >= 0:
            if listx[j] > listx[j+1]:
                # listx[j+1] = listx[j]
                # listx[j] = key
                listx[j+1],listx[j] = listx[j],listx[j+1]
                j -= 1
            else:
                break
    return listx

if __name__=='__main__':
    list1 = [2,3,1,0,66,87,34,2,54,23,12,0]
    print insertSort(list1)



# 插入排序的时间复杂度
# 最好情况：n-1--O(n)
#
# 平均情况：n^2/4---O(n^2)
#
# 最差情况：n^2/2-n/2----O(n^2)
# 1:1
# 2:2
# 3:3
# ....
# n-1:n-1


