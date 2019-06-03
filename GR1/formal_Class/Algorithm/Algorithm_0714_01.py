# encoding=utf-8
class TreeNode(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root):
        self.root = root
#
# # 先序遍历
def preOrder(retList,node):
    if node != None:
        retList.append(node)
        preOrder(retList,node.left)
        preOrder(retList.node.right)
    return retList
if __name__=='__main__':
    rootNode = TreeNode(50)
    rootNode.left=TreeNode(20,left=TreeNode(15),right=TreeNode(30))
    rootNode.right=TreeNode(60,right=TreeNode(70))
    binaryTree = BinaryTree(rootNode)
    retList = preOrder([],binaryTree.root)
    for i in retList:
        print i.val
# 先序遍历
class TreeNode(object):
    def __init__(self,var,left=None,right=None):
        self.var = var
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root=None):
        self.root = root

def preOrder(retList,node):
    if node != None:
        retList.append(node)
        preOrder(retList,node.left)
        preOrder(retList,node.right)

    return retList

if __name__ == '__main__':
    rootNode = TreeNode(11)
    rootNode.left = TreeNode(9,left=TreeNode(6,left=TreeNode(3),right=TreeNode(8)),right=TreeNode(10))
    rootNode.right = TreeNode(17,left=TreeNode(12),right=TreeNode(19))
    binaryTree = BinaryTree(rootNode)

    retList = preOrder([],binaryTree.root)
    for i in retList:
        print i.var,

# 中序遍历
class TreeNode(object):
    def __init__(self,var,left=None,right=None):
        self.var = var
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root=None):
        self.root = root

def inOrder(retList,node):
    if node != None:

        inOrder(retList,node.left)
        retList.append(node)
        inOrder(retList,node.right)
    return retList

if __name__ == '__main__':
    rootNode = TreeNode(11)
    rootNode.left = TreeNode(9,left=TreeNode(6,left=TreeNode(3),right=TreeNode(8)),right=TreeNode(10))
    rootNode.right = TreeNode(17,left=TreeNode(12),right=TreeNode(19))
    binaryTree = BinaryTree(rootNode)
    retList = inOrder([],binaryTree.root)
    for i in retList:
        print i.var,

# 后序遍历
class TreeNode(object):
    def __init__(self,var,left=None,right=None):
        self.var = var
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root=None):
        self.root = root

def postOrder(retList,node):
    if node != None:
        postOrder(retList,node.left)
        postOrder(retList,node.right)
        retList.append(node)
    return retList

if __name__ == '__main__':
    rootNode = TreeNode(11)
    rootNode.left = TreeNode(9,left=TreeNode(6,left=TreeNode(3),right=TreeNode(8)),right=TreeNode(10))
    rootNode.right = TreeNode(17,left=TreeNode(12),right=TreeNode(19))
    binaryTree = BinaryTree(rootNode)

    retList = postOrder([],binaryTree.root)
    for i in retList:
        print i.var,

# 习题：把先序遍历函数移到类里面去
class TreeNode(object):
    def __init__(self,var,left=None,right=None):
        self.var = var
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root=None):
        self.root = root

    def preOrder(self,retList,node):
        if node != None:
            retList.append(node)
            self.preOrder(retList,node.left)
            self.preOrder(retList,node.right)

        return retList



if __name__ == '__main__':
    rootNode = TreeNode(11)
    rootNode.left = TreeNode(9,left=TreeNode(6,left=TreeNode(3),right=TreeNode(8)),right=TreeNode(10))
    rootNode.right = TreeNode(17,left=TreeNode(12),right=TreeNode(19))
    binaryTree = BinaryTree(rootNode)

    retList = binaryTree.preOrder([],binaryTree.root)
    for i in retList:
        print i.var,









