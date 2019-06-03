# encoding=utf-8
import Queue
# 深度优先的桟实现：
def depthFirstSearch2(self, root=None):
    # 存放遍历列表
    order = []
    s = Queue.LifoQueue()
    # s = Queue.Queue()
    # 访问完该节点之后，继续深度访问其邻接节点，直到没有节点可以访问
    # def dfs():
    #     node = s.get()
    #     self.visited[node] = True
    #     order.append(node)
    #     for n, v in self.nodeNeighbors[node]:
    #         if n not in self.visited:
    #             s.put(n)
    #             dfs()
    def dfs():
        while s.empty() is not True:
            node = s.get()
            self.visited[node] = True
            order.append(node)
            for n, v in self.nodeNeighbors[node]:
                if n not in self.visited:
                    s.put(n)

    if root:
        s.put(root)
        dfs()

    # 一次dfs访问不到的节点，以它为起点继续遍历
    for node in self.nodes():
        if not node in self.visited:
            dfs()
    return order







