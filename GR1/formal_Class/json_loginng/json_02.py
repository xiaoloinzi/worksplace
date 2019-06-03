# encoding=utf-8
import json

json.loads()

data = [{'a':'A','b':(2,4),'c':3.0,'d':None,'e':True}]
print data
dataJson = json.dumps(data,
                      sort_keys=True,
                      separators=(',',':'),
                      indent=4,
                      skipkeys=True)
print dataJson
print json.loads(dataJson)

class Employee(object):
    def __init__(self,name,age,sex,tel):
        self.name = name
        self.age = age
        self.sex = sex
        self.tel = tel

    def objJson(self,obj_instance):
        return {
            'name':obj_instance.name,
            'age':obj_instance.age,
            'sex':obj_instance.sex,
            'tel':obj_instance.tel
        }

e1 = Employee('andly','24','male','13XXXXXXXX')
# default=调用什么方法，再返回值
print json.dumps(e1,default=e1.objJson)
e1.objJson(e1)


# 习题：
# 1、通过__dict__改写如下的代码，
# print json.dumps(e1,default=e1.objJson)
# 完成实例转换成为json格式对象。

# print json.dumps(e1.__dict__)


# 类json转换Python

class Employee(object):
    def __init__(self,name,age,sex,tel):
        self.name = name
        self.age = age
        self.sex = sex
        self.tel = tel
    def objJson(self,obj_instance):
        return {
            'name':obj_instance.name,
            'age':obj_instance.age,
            'sex':obj_instance.sex,
            'tel':obj_instance.tel
        }

e1 = Employee('andy','24','male','131xxxxxxxx')
print json.dumps(e1.__dict__)
#fucn(e1)
print e1.__dict__

def jsonToClass(dictVar):
    return Employee(dictVar['name'],dictVar['age'],dictVar['sex'],dictVar['tel'])
jsonDate = '{"name": "andy", "age": "24", "sex": "male", "tel": "131xxxxxxxx"}'
e = json.loads(jsonDate,object_hook=jsonToClass)
print e
print e.name
print type(e.name)


# 习题：在上述代码的基础上，循环做5次序列化对象反序列化对象
class Employee(object):
    def __init__(self,name,age,sex,tel):
        self.name = name
        self.age = age
        self.sex = sex
        self.tel = tel
    def objJson(self,obj_instance):
        return {
            'name':obj_instance.name,
            'age':obj_instance.age,
            'sex':obj_instance.sex,
            'tel':obj_instance.tel
        }

e1 = Employee('andy','24','male','131xxxxxxxx')
print json.dumps(e1.__dict__)
#fucn(e1)
print e1.__dict__

def jsonToClass(dictVar):
    return Employee(dictVar['name'],dictVar['age'],dictVar['sex'],dictVar['tel'])
jsonDate = '{"name": "andy", "age": "24", "sex": "male", "tel": "131xxxxxxxx"}'
e = json.loads(jsonDate,object_hook=jsonToClass)
print e
print e.name
print type(e.name)







