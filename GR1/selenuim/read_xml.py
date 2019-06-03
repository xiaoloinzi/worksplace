# encoding=utf-8
# 获得标签的信息
from xml.dom import minidom
# 打开xml文档
dom = minidom.parse('xml/info.xml')
'''
首先导入xml文件的minidom模块，用来处理XML文件，parse（）用于打开一个xml文件，
documentElement得到xml文件的唯一根元素
每个节点都有它的nodeName、nodeType、nodeValue等属性，nodeName为节点的名称；
nodeValue为节点的值，只对本节点有效；nodeType为节点的类型
'''
# 得到文档元素对象
root = dom.documentElement

print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE












