# encoding=utf-8
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class MyQueue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def put(self, n):
        packNode = Node(n)
        if self.first == None:
            self.first = packNode
            self.last = packNode
        else:
            self.last.next = packNode
            self.last = packNode

    def get(self):
        if self.first == None:
            return None
        else:
            tmp = self.first.val
            if self.first == self.last:
                self.last = None
            self.first = self.first.next
            return tmp

if __name__ == '__main__':
    q = MyQueue()
    q.put(1)
    q.put(2)
    q.put(3)
    print q.get()
    print q.get()
    print q.get()
    print q.last.val
# 习题：写get方法，返回节点的值
