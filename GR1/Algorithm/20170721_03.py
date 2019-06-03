# encoding=utf-8
# 从大到小
def maxHeap(heap, heapSize, i):
    left = 2*i +1
    right = 2*i +2
    larger = i
    if left < heapSize and heap[larger] > heap[left]:
        larger = left
    if right < heapSize and heap[larger] > heap[right]:
        larger = right
    if larger != i:
        heap[i],heap[larger] = heap[larger],heap[i]
        maxHeap(heap,heapSize,larger)

def buildMaxHeap(heap):
    heapSize = len(heap)
    for i in xrange((heapSize-1)//2,-1,-1):
        maxHeap(heap,heapSize,i)

def heapSort(heap):
    buildMaxHeap(heap)
    for i in xrange(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        maxHeap(heap,i,0)
    return heap

if __name__ == '__main__':
    heap1 = [233,34,3,3,454,5,2,78,989]
    print heap1
    heapSort(heap1)
    print heap1


#从小到大
def maxHeap(heap, heapSize, i):
    left = 2*i +1
    right = 2*i +2
    larger = i
    if left < heapSize and heap[larger] < heap[left]:
        larger = left
    if right < heapSize and heap[larger] < heap[right]:
        larger = right
    if larger != i:
        heap[i],heap[larger] = heap[larger],heap[i]
        maxHeap(heap,heapSize,larger)

def buildMaxHeap(heap):
    heapSize = len(heap)
    for i in xrange((heapSize-1)//2,-1,-1):
        maxHeap(heap,heapSize,i)

def heapSort(heap):
    buildMaxHeap(heap)
    for i in xrange(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        maxHeap(heap,i,0)
    return heap

if __name__ == '__main__':
    heap1 = [233,34,3,3,454,5,2,78,989]
    print heap1
    heapSort(heap1)
    print heap1



















