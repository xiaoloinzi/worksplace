# # encoding=utf-8
s = int(raw_input(u'请输入一个数值：'))
a = 0
if a == 0:
    print a

if s == 0:
    print s
else:
    print u'输入的数值不等于0'

if s == 0:
    print s
elif s > 1:
    print s
else:
    print u'输入的数值不等于0'

if s == 0:
    print s
elif s == 1:
    print s
elif s == 2:
    print s
elif s == 3:
    print s
else:
    print u'输入的数值不等于0'
#1、使用字典去承载
# 2、通过name[0][0]的形式去取首字母
# 3、通过has_key判断是否存在，并且做相关计算
name=['foster','foe','lily',
      'mickel','live','moon',
      'ruby','cindy','miya']
dict1 = {}

for i in name:
    if dict1.has_key(i[0]):
        dict1[i[0]] +=1
    else:
        dict1[i[0]] =1
print dict1

for key,value in dict1.items():
    print u'以姓名为字母',key,u'开头的有：',value

# 1、封装一个函数，判断是否是三角形，
# 获取数据，调用函数

def checkTriangle(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    flag = a+b>c and a+c>b and b+c >a#做一个标记
    if not flag:
        return False
    return True
if checkTriangle(2,2,3):
    print u'是三角形'

while True:
    i = raw_input(u'fff')
    if i == 'quit':
        break

for i in range(10):
    for j in range(i):
        print j


# 1、封装一个函数，求公式；1个参数
# 2、调用函数
def multinomial(n):
    mathStr = ''

    while n>=0:
        if n == 0:
            mathStr +='a'+'0'
        else:
            mathStr += 'a'+str(n)+'x'+'^'+str(n)+'+'
        n -=1
    return mathStr

print multinomial(9)
# 写一个死循环
l = [1,2,3]
a = 3
for i in l:
    print i
    if raw_input('please input:') != 'quit':
        l.append(a)
    else:
        break
# 从2一直除到该数都没有被整除的就为素数
i = int(raw_input('please:'))
flag = True
for j in range(2,i):
    if i%j == 0:
        flag =False
        break
if not flag:
    print u'不是素数'
else:
    print u'是素数'

# 求100个随机数之和，随机数要求为0—9的整数
# 练习题：嵌套循环输出10-50中个位带有1-5的所有数字
for i in range(10,50):
    if str(i)[1] in ['1','2','3','4','5']:
        print i

for i in range(1,5):
    number = i*10
    for j in range(1,6):
        sum = number + j
        print sum
# 判断字符串、列表、元组、数字、字典 是否可迭代，
# 如果可以的话，遍历打印里面的所有值

list1 = [1,2,3]
tuple1 = (1,2,3)
str1 = '1234'
s = 123
dict1 = {'1':1,'2':2}
from collections import Iterable
print isinstance('abc', Iterable) # str是否可迭代
print isinstance([1,2,3], Iterable) # list是否可迭代
print isinstance(123, Iterable) # 整数是否可迭代

def checkIter(date):
    if isinstance(date, Iterable):
        for i in date:
            print i
    else:
        print u'不可以迭代'
    return ' '
print checkIter(list1)
print checkIter(tuple1)
print checkIter(str1)
print checkIter(s)
print checkIter(dict1)













































