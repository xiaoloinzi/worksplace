# encoding=utf-8
# 获取标签的属性值
from xml.dom import minidom
'''
getAttribute()方法用于获取元素的属性值
'''
# 打开xml文档
dom = minidom.parse('xml/info.xml')

# 得到文档元素对象
root = dom.documentElement

logins = root.getElementsByTagName('login')

# 获得login标签的username属性值
username = logins[0].getAttribute('username')
print username
password = logins[0].getAttribute('password')
print password
username = logins[1].getAttribute('username')
print username
password = logins[1].getAttribute('password')
print password
























