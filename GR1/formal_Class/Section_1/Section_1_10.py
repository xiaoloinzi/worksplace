# encoding=utf-8
list1 = [1,2,3]
tuple1 = (2,3,4)
s = 1
if s in list1:
    print s,u'在列表中',list1
else:
    print s,u'不在列表中',list1
if s in tuple1:
    print s,u'在元组中',tuple1
else:
    print s,u'不在元组中',tuple1

a =1
b =1
c =3
d =c
print id(a),id(b)

print u'a的id',id(a),u'b的id',id(b),u'a和b一样',a is b
# print u'c的id',id(c),u'd的id',id(d),u'c和d一样',c is d
import math

a = [-3.4,-6.78,-89.4,-98.6,-34.5]
# 1、转换成整数
# 2、求最大值
# 3、求最小值
list1 =[]
for i in a:
    i = int(i)
    i = abs(i)
    list1.append(i)
print list1
print max(list1)
print min(list1)

import random
#随机数random--choice随机取值，uniform随机取一个浮点数
#randrange在一定范围内取值，shuffle随机排列
#1、在[1,1000]的范围内,随机的选取一个整数，
#不少于三种方法

list2 = range(1,1001)
print random.choice(list2)
print random.randrange(1,1001)
print int(random.uniform(1,1000))
print random.randint(1,1000)#随机选整正整数

#repr--str,表达式字符串--字符串



