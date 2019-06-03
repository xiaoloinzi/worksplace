#encoding=utf-8
i = 28
l = 987654325252
f = 32.12
p = 6+1j


print type(i)
print type(l)
print type(f)
print type(p)
#不同的数值类型
s = 810
s1 = 12345679
f1 = 9.0
cheng = s*s1
chu = cheng/f1
print(cheng)
print(chu)
print type(cheng)
print type(chu)
#不同的显示形式
str1 = 'CR1'
str2 = "GR2"
str3 = '''GR3
GR3
GR3//
'''
str4 = "GR2\nGR3"

strU = u'光荣之路'
strR = r'&#\\'
print str1,str2,str3,str4,strU,strR
字符的转换
strz1 = r'\''
strz2 = u'单引号：\''
strz3 = u'\n双引号：\"'
strz4 =u"三引号：\'''"
print strz2,strz3,strz4
print("单引号：\'\n双引号：\"三引号：\'''")
length = 10
breadth = 5
area = length * breadth
print u'面积是：',area
#函数的写法
def getArea(length,breadth):
    return length * breadth

print getArea(10,5)
def getSum(self1,self2):
    return self1+self2
print(getSum(2046,9876))
# 指定数值
def getArea(length,breadth=7):
     return length * breadth
print getArea(10)
i = 5
if i < 5:
    pass
elif i==5:
    pass
else:
    pass
# #界面输入值
# j =raw_input(u'请输入：')
# print j

#输入值的时候要转换类型
j = int(raw_input('请输入学生分数：'))
if 0 <= j < 60:
    print '不及格'
elif 100 >= j >= 60:
    print '及格'
else:
    print '输入有误'




