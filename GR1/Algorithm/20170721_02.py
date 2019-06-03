# encoding=utf-8
# 1、二叉树的广度优先遍历

from Queue import Queue

class TreeNode(object):
    def __init__(self,var,left=None,right=None):
        self.var = var
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root=None):
        self.root = root

    def breathSearch(self):
        if self.root == None:
            return None
        retList = []
        queue = Queue()
        queue.put(self.root)

        while queue.empty() is not True:
            node = queue.get()
            retList.append(node.var)

            if node.right != None:#先左还是先右换判断就好
                queue.put(node.right)
            if node.left != None:
                queue.put(node.left)
        return retList

if __name__ == '__main__':
    rootNode = TreeNode(50)
    rootNode.left = TreeNode(20,left=TreeNode(15),right=TreeNode(30))
    rootNode.right = TreeNode(60,right=TreeNode(70))
    tree = BinaryTree(rootNode)
    retList = tree.breathSearch()
    print retList



























