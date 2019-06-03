# encoding=utf-8
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read('D:\\tmp\\config.cfg\\properties.conf')
# print cf.sections()

print cf.options('baseconf')#---key值
print cf.items('baseconf')#(key,value)

print cf.get('baseconf','db_name')#取精确的值--重点
print type(cf.get('baseconf','db_name'))

cf.add_section('test3')
cf.set('test3','key12','value12')
cf.write(open('D:\\tmp\\config.cfg\\properties.conf','w'))


# 习题：
# 读取baseconf下的host
# 读取test下的float

# print cf.get('baseconf','host')
# print cf.get('test0827.txt','float')

# 习题：在配置文件中，写如下的数据：
# [test12]
# ip = 127.0.0.1
# int = 1
# float = 1.5
# bool = True

cf.add_section('test12')
cf.set('test12','ip','127.0.0.1')
cf.set('test12','int','1')
cf.set('test12','float','1.5')
cf.set('test12','bool','True')
cf.write(open('D:\\tmp\\config.cfg\\properties.conf','w'))






