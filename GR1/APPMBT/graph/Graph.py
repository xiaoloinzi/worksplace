# encoding=utf-8
import networkx as nx
import random

# 得到一个图的实例
Graphs = nx.DiGraph()
allShortPath = {}

def addEdge(sourceNode,dstNode):
    # 添加边
    Graphs.add_edge(sourceNode,dstNode)

def printGraph():
    # 打印节点
    print 'nodes:('+str(Graphs.number_of_nodes())+')'+str(Graphs.nodes())
    # 打印边
    print 'edges:('+str(Graphs.number_of_edges())+')'+str(Graphs.edges())

# 获取最短路径
def genAllShortPath():
    global allShortPath
    allShortPath = nx.all_pairs_shortest_path(Graphs)
    print 'the shortest path is :',str(allShortPath)
    print 'the shotest path list is:',str(list(allShortPath))

# 生成随机路径
# [node1,node2,node3]
def randomPath(sourceNode = None,minlen = 2):
    while True:
        if sourceNode == None:
            # 获取一个随机节点作为开始节点
            sourceNode = random.choice(list(allShortPath))
        targetNode = random.choice(list(allShortPath[sourceNode]))
        path = allShortPath[sourceNode][targetNode]
        if len(path) >= minlen:
            break
    print
    return path

# 指定路径
def getPath(sourceNode,dstNode):
    path = allShortPath[sourceNode][dstNode]
    return path

















