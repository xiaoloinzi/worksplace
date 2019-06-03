# encoding=utf-8
import  json

data = {'a':'A','b':(2,4),'c':3.0}
res = repr(data)
print res
data_json = json.dumps(data,indent=2)
print data_json

class Person(object):
    def __init__(self,name,age,sex,adress):
        self.name = name
        self.age = age
        self.sex = sex
        self.adress = adress

    def printJson(self,obj_instance):
        return {
            "name":obj_instance.name,
            "age":obj_instance.age,
            "sex":obj_instance.sex,
            "adress":obj_instance.adress.__dict__
        }
class Adress(object):
    def __init__(self,hadress,cadress,fadress):
        self.hadress = hadress
        self.cadress = cadress
        self.fadress = fadress


if __name__ == '__main__':
    a = Adress("a","2","3")
    b = Adress("b","2","3")
    c = Adress("c","2","3")
    p1 = Person("name1",11,"m1",a)
    p2 = Person("name2",12,"m2",b)
    p3 = Person("name3",13,"m3",c)
    print json.dumps(p1,default=p1.printJson,indent=4)
    print json.dumps(a,default=lambda a:a.__dict__)







