# encoding=utf-8
import Queue

class TreeNode(object):
    def __init__(self,var):
        self.value = var
        self.left = None
        self.right = None
        self.father = None


class BST(object):
    def __init__(self,nodeList):
        self.root = None
        for node in nodeList:
            self.insert(node)

    def insert(self,node):
        father = None
        cur = self.root

        while cur != None:
            if cur.value == node.value:
                return -1
            father = cur
            if node.value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        node.father = father
        if father == None:
            self.root = node
        elif node.value < father.value:
            father.left = node
        else:
            father.right = node

    def delete(self,node):
        father = node.father
        if node.left == None:
            if father == None:
                self.root = node.right
                if node.right != None:
                    node.right.father = None
            elif father.left == node:
                father.left = node.right
                if node.right != None:
                    node.right.father = father
            else:
                father.right = node.right
                if node.right != None:
                    node.right.father = father
            return 1
        tmpNode = node.left
        while tmpNode.right != None:
            tmpNode = tmpNode.right

        tmpNode.right = node.right
        if node.right != None:
            node.right.father = tmpNode

        if father == None:
            self.root = node.left
            node.left.father = None
        elif father.left == node:
            father.left = node.left
            node.left.father = father
        else:
            father.right = node.left
            node.left.father = father
        node = None
        return 2

    def searchNode(self,var):
        cur = self.root
        while cur != None:
            if cur.value == var:
                return cur
            elif cur.value < var:
                cur = cur.right
            else:
                cur = cur.left
        return

    def brethSearch(self):
        if self.root == None:
            return None
        retList = []
        queue = Queue.Queue()
        queue.put(self.root)
        while queue.empty() is not True:
            node = queue.get()
            retList.append(node.value)
            if node.left != None:
                queue.put(node.left)
            if node.right != None:
                queue.put(node.right)
        return retList

if __name__ == '__main__':
    varList = [24,34,5,4,8,23,45,35,28,6,29,30]
    nodeList = [TreeNode(var) for var in varList]
    bst = BST(nodeList)
    print bst.brethSearch()
    node = bst.searchNode(34)
    bst.delete(node)
    bst.insert(TreeNode(20))
    print bst.brethSearch()

