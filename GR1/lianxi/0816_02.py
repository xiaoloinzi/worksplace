# encoding=utf-8
import json

class Employee(object):
    def __init__(self,name,age,sex,tel):
        self.name = name
        self.age = age
        self.sex = sex
        self.tel = tel

if __name__=="__main__":
    emp = Employee("lily",24,"famale",'18525444444')
    def jsonToClass(emp):
        return Employee(emp["name"],emp["age"],emp["sex"],emp["tel"])
    json_str = '{"name":"Lucy","age":21,"sex":"famale","tel":"18542544122"}'
    e = json.loads(json_str,object_hook=jsonToClass)
    print emp.__dict__
    print e
    print e.name








