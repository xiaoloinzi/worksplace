# encoding=utf-8
import json


# json
# 1、把Python的数据，转换成为json格式--json.dump()
# 2、把json格式转换成为Python格式--json.load()
data = [{'a':'A','b':(2,4),'c':3.0,'d':None,'e':True}]

print data
dataJson = json.dumps(data)
print dataJson

data2 = {u'a':'abc',u'b':(1,2)}
print data2
print json.dumps(data2)
# dumps(sort_keys=是否按照字典显示--Ture--按照字典序输出,False，
# indent =添加空格显示，separators=指定字符后面的空格去掉，
# skipkeys=True忽略出错的数值，其他数值照常输出

# 1、对于如下的python数据
# data= [ { 'a':'A', 'b':(2, 4), 'c':3.0, (1,2):'D tuple' } ]
# ，转换成json字符串，空4格显示，字典序

data1= [{'a':'A','d':(2, 4),'c':3.0,'D':(1,2)}]
print json.dumps(data1,sort_keys=True,separators=(',',':'),indent=4)


# 1、对于如下的python数据
# data= [ { 'a':'A', 'b':(2, 4), 'c':3.0, (1,2):'D tuple' },u'中国':'china' ]
# ，转换成json字符串，空4格显示，字典序，把逗号和冒号后面的空格去掉
# 分别skipkeys设置成True 和 False,分别设置ensure_ascii 为True 和False
data3= [ { 'a':'A', 'b':(2, 4), 'c':3.0, (1,2):'D tuple' ,u'中国':'china' }]
data4= [ { 'a':'A', 'b':(2, 4), 'c':3.0, (1,2):'D tuple' ,'中国'.decode('utf-8'):'china' }]

print json.dumps(data3,
                sort_keys=True,
                separators=(',',':'),
                indent=4,
                skipkeys=True,
                )
print '-'*40
# print json.dumps(data3,
#                 sort_keys=True,
#                 separators=(',',':'),
#                 indent=4,
#                 skipkeys=False,
#                 )
print '-'*40
print json.dumps(data3,
                sort_keys=True,
                separators=(',',':'),
                indent=4,
                skipkeys=True,
                ensure_ascii=True)
print '-'*40
print json.dumps(data3,
                sort_keys=True,
                separators=(',',':'),
                indent=4,
                skipkeys=True,
                ensure_ascii=False)
print json.dumps(data4,
                sort_keys=True,
                separators=(',',':'),
                indent=4,
                skipkeys=True,
                ensure_ascii=False,
                encoding='gbk')











