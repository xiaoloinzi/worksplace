# encoding=utf-8
# 获取标签对之间的数据
from xml.dom import minidom
# 打开xml文档
dom = minidom.parse('xml/info.xml')
# 得到文档元素对象
root = dom.documentElement

provinces = dom.getElementsByTagName('province')
citys = dom.getElementsByTagName('city')
'''
firstChild属性返回被选节点的第一个节点，data表示获取该节点的数据，
它和WebDriver中提供的text方法类似
'''

# 获得第二个province标签对的值
p2 = provinces[1].firstChild.data
print p2

# 获得第一个city标签对的值
c1 = citys[0].firstChild.data
print p2

c2 = citys[0].firstChild.data
print c2


