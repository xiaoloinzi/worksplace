# encoding=utf-8
import json

data = [{'a':'A','b':(2,4),'c':3.0}]
res = repr(data)
print 'data:',res
data_json = json.dumps(data)
print data_json[2:10]

a = [{1:12,'a':12.3},[1,2,3],(1,2),'abs',u'ad',12,13L,3.3,
     True,False,None]
print u'Python的类型：\n',a
print u'编码后的json类型：\n',json.dumps(a)

date = [{'a':'A','b':(2,4),'c':3.0}]
print json.dumps(date)
print json.dumps(date,sort_keys = True)
print json.dumps(date)
print json.dumps(data,sort_keys = True,indent = 3)
print json.dumps(date),':',len(json.dumps(date))
print json.dumps(data,separators=(',',':')),':',len(json.dumps(data,separators=(',',':')))
print u'不设置参数shipkeys'
try:
    res1 = json.dumps(date)
except Exception,e:
    print e

print u'设置skipkeys参数'
print json.dumps(date,skipkeys=True)









































