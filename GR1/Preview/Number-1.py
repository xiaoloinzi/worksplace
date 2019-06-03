# encoding=utf-8
# Number数据类型是用于存储数值并不允许改变的，如果改变Number这种数据类型的值，就意味着要重新分配内存空间
# 在变量赋值时，Number对象将就被创建，如下
import math
import random

var1 = 1
var2 = 2
#可以使用del来删除Number对象的引用，
#del的删除语法是：del var1[,var2[,var3[....varN]]]
var3 = 65
print var1,var2,var3

#使用del语句删除单个会多个对象

del var1
del var2,var3
#print var1,var2,var3#提示出错，因为var1,var2,var3已被删除。
# *Python中类型的转换：
# int(x[,base])--将x转换为一个整数
var4 = 12.98
print int(var4)
# long(x[,base])--将x转换为一个长整型数
var5 = 3632476L
print long(var5)#python后期不再使用这种数据类型
# float(x)--将x转换为一个浮点型数
var6 = 12
print float(var6)
# complex(x,[,img])--创建一个复数
print complex(1,2)
# str(x)--将对象x转换为字符串
var7 =str(45)
print var7
print type(var7)
#repr(x)--将对象x转换为表达式字符串
#函数str()用于将值转化为适于人阅读的形式，而repr（）转化为供解释器读取的形式
#repr()函数得到的字符串通常可以用来重新获得该对象，repr()的对Python比较友好，通常情况下obj == eval(repr(obj))这个等式是成立的
obj = 'I love python'
print obj == eval(repr(obj))
#print obj == eval(str(obj))#报错
print u'repr输出的格式',repr([0,1,2,3])
print u'str输出的格式',str([0,1,2,3])
print u'repr输出的格式',repr('hello')
print u'str输出的格式',str('hello')
print u'repr输出的格式',repr(1.0/7.0)
print u'str输出的格式',str(1.0/7.0)
#eval(x)--用来计算字符串中有效的Python表达式，并返回一个对象
var9 = '2+3'
print u'eval转换前',var9
print u'eval转换前',eval(var9)
#tuple(s)--将序列s转换为一个元组
var10 = 'yuanzu'
print u'将var10 = \'yuanzu\'转换为元组',tuple(var10)
#list(s)--将序列s转换为一个列表
print u'将var10 = \'yuanzu\'转换为列表',list(var10)
#chr(x)--将一个整数转换为一个字符,返回整数i对应的ASCII字符。与ord()作用相反
var10 = 67
print chr(var10),chr(97)
#unichr(X)--将一个整数转换为Unicode字符
print unichr(2345)
#ord(x)--将一个字符转换为它的整数值
print ord('Z')
#hex(x)--将一个整数转换为一个十六进制的字符串
print hex(45)
#oct(x)--将一个整数转换为一个八进制的字符串
print oct(45)

#*python中的函数值
#abs(x)--返回数字的绝对值
print u'返回-10的绝对值：',abs(-10)
print u'abs(\'11L\'):',abs(11L)
#fbas(x）--返回数字的绝对值，引用math模块
print u'返回-10的绝对值:%d，通过math.fabs()'%math.fabs(-10)
#ceil(x)--返回数字的上入整数
print u'返回4.1的上入整数：%d,通过math.ceil()引用'%math.ceil(4.1)
print u'math.ceil(-45.17)',math.ceil(-45.17)
print u'math.ceil(99L)',math.ceil(99L)
print u'math.ceil(math.pi)',math.ceil(math.pi)
#cmp(x,y)--如果x>y,返回1，如果x<y,返回-1，如果x==y,返回0.
print u'返回cmp(2,3)的值',cmp(2,3)
print u'返回cmp(3,3)的值',cmp(3,3)
print u'返回cmp(4,3)的值',cmp(4,3)
print u'cmp(-100,100)',cmp(-100,100)
#exp(x)--返回e的x次幂
print math.exp(2)
print u'math.exp(math.pi)',math.exp(math.pi)
print u'math.exp(99L)',math.exp(99L)
print u'math.exp(-45.17)',math.exp(-45.17)
print u'math.exp(100.57)',math.exp(100.57)
#floor(x)--返回整数的下舍整数
print math.floor(3.3)
#max(x1,x2)--返回给定参数的最大值
print max(2,3,4)
#min(x1,x2)--返回给定参数的最小值
print min(2,3,4)
#modf(x)--返回x的整数部分与小数部分，两部分的数值符号与x的相同，整数部分以浮点型表示
print math.modf(3.45)
#pow(x,y)--计算x**y的值
print pow(2,3)
#round(x[,n])--返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
print round(3.456,2)
#sqrt(x)--返回数字x的平方根，数字可以为负数，返回类型为实数
print math.sqrt(4)

#*Python随机数函数
#choice(sep)--从序列的元素中随机挑选一个元素，
print random.choice(range(10))
#randrange([start,]stop[,step])--从指定的范围内，按指定基数递增的集合获取一个随机数基数缺省值为1
print random.randrange(0,10,2)
#random()--随机生成下一个实数，在[0,1]的范围内
var14 = random.random()
print var14
#shuffle(lst)--将序列中的所有元素随机排序
list11 = [2,3,4,1,7,5,9,8]
random.shuffle(list11)
print list11
#uniform(x,y)--随机生成一个实数，它在[x,y]的范围内
print random.uniform(1,4)

print math.e
print math.pi