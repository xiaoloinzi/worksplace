# encoding=utf-8
# 【python每日一练】定义一个Person类，基本属性包括pName,pSex,
# pAge和pAddress,pAddress又包括家庭地址(homeAddress)，
# 公司地址(companyAdrress)，常用地址(frequentAdress)，
# 地址请使用类来定义。即地址对象为Person类的一个属性。
# 最后实例化3个Persion对象，
# 并将结果转化成功json格式输出
import json


class Person(object):
    def __init__(self,pName,pSex,pAge,pAddress):
        self.pName = pName
        self.pSex = pSex
        self.pAge = pAge
        self.pAddress = pAddress
    def printJson(self):
        return {
            "name":self.pName,
            "sex":self.pSex,
            "age":self.pAge,
            "address":{"homeAddress":self.pAddress.homeAddress,
                       "companyAdrress":self.pAddress.companyAdrress,
                       "frequentAdres":self.pAddress.frequentAdres}
        }
    def printJson1(self,obj_instant):
        return {
            "name":obj_instant.pName,
            "sex":obj_instant.pSex,
            "age":obj_instant.pAge,
            "address":{"homeAddress":obj_instant.pAddress.homeAddress,
                       "companyAdrress":obj_instant.pAddress.companyAdrress,
                       "frequentAdres":obj_instant.pAddress.frequentAdres}
        }
class Paddress(object):
    def __init__(self,homeAddress,companyAdrress,frequentAdres):
        self.homeAddress = homeAddress
        self.companyAdrress = companyAdrress
        self.frequentAdres = frequentAdres
if __name__=="__main__":
    person1 = Person(u"张三","wa",25,Paddress(u"天河1",u'高德1',u'中山大道1'))
    person2 = Person(u"李四","wb",26,Paddress(u"天河2",u'高德2',u'中山大道2'))
    person3 = Person(u"王五","wc",27,Paddress(u"天河3",u'高德3',u'中山大道3'))
    list1 = [person1.printJson(),person2.printJson(),person3.printJson()]
    print json.dumps(list1,indent=4,ensure_ascii=False,sort_keys=True)
    # print json.dumps(person1,default=person1.printJson,indent=4,ensure_ascii=False,sort_keys=True)





















