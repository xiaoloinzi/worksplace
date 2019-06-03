# encoding=utf-8
# 快速排序


def quickSort(listx):
    def pathSort(lista,sIndex,eIndex):
        flag = lista[eIndex]
        i = sIndex-1
        for j in xrange(sIndex, eIndex):
            if lista[j] <= flag:
                i += 1
                lista[i],lista[j] = lista[j],lista[i]
        lista[eIndex],lista[i+1] = lista[i+1],lista[eIndex]
        return i+1

    def qSort(listb,sIndex,eIndex):
        if sIndex >= eIndex:
            return
        middle = pathSort(listb,sIndex,eIndex)
        qSort(listb,sIndex,middle-1)
        qSort(listb,middle+1,eIndex)
        print listb

    qSort(listx,0,len(listx)-1)
    return listx

if __name__ == '__main__':
    print quickSort([233,4,2334,44,5666,2,3,456,234,1])

i = start
def quickSort(listx):
    def pathSort(lista,sIndex,eIndex):
        flag = lista[eIndex]
        i = sIndex
        for j in xrange(sIndex, eIndex):
            if lista[j] <= flag:
                lista[i],lista[j] = lista[j],lista[i]
                i += 1
        lista[eIndex],lista[i] = lista[i],lista[eIndex]
        return i

    def qSort(listb,sIndex,eIndex):
        if sIndex >= eIndex:
            return
        middle = pathSort(listb,sIndex,eIndex)
        qSort(listb,sIndex,middle-1)
        qSort(listb,middle+1,eIndex)
        print listb

    qSort(listx,0,len(listx)-1)
    return listx

if __name__ == '__main__':
    print quickSort([233,4,233,4,44,5666,2,3,456,234,1])



































