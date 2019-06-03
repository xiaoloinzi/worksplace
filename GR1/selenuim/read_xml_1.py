# encoding=utf-8
# 获得任何标签名
from xml.dom import minidom

# 打开xml文档
dom = minidom.parse('xml/info.xml')

# 得到文档元素对象
root = dom.documentElement
'''
getElementsByTagName()可以通过标签名获取标签，它所获取的对象是以数组形式存放，
例如‘login’和‘province'标签在info.xml文件中有多个，
则可以通过指定数组的下标方式获取某个具体标签
getElementsByTagName('province')获得的标签名为province的一组标签
getElementsByTagName('province').tagname[0]表示一组标签中的第一个
getElementsByTagName('province').tagname[2]表示一组标签中的第三个
'''
tagname = root.getElementsByTagName('browser')
print tagname[0].tagName

tagname = root.getElementsByTagName('login')
print tagname[1].tagName

tagname = root.getElementsByTagName('province')
print tagname[2].tagName

tagname = root.getElementsByTagName('province')
print tagname