# encoding=utf-8
import networkx as nx
import random

Graph = nx.DiGraph()
allShortPath = {}

def addEdge(sourceNode,dstNode):
    Graph.add_edge(sourceNode,dstNode)

def printGraph():
    print 'nodes:('+str(Graph.number_of_nodes())+')'+str(Graph.nodes())
    print 'edges:('+str(Graph.number_of_edges())+')'+str(Graph.edges())

def genAllShortestPath():
    global allShortPath
    allShortPath = nx.all_pairs_shortest_path(Graph)
    print 'the shortest path is :',str(allShortPath)
    print 'the shortest path list is :',str(list(allShortPath))

#[node1,node2,node3]
def randomPath(sourceNode=None,minLen=2):
    while True:
        if sourceNode == None:
            sourceNode = random.choice(list(allShortPath))
        targetNode = random.choice(list(allShortPath[sourceNode]))
        path = allShortPath[sourceNode][targetNode]
        if len(path) >= minLen:
            break
    print
    return path

def getPath(sourceNode,dstNode):
    path = allShortPath[sourceNode][dstNode]
    return path























