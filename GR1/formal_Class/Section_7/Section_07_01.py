# encoding=utf-8
import random,os
# print 1/0
# 1.随机去生成一个数字，输入一个数字去猜随机生成的数，猜对了，提示猜对了，
# 如果输入错误，提示用户再次输入，在用户输入正确数据后需要提示
# 用户该输入的数字是大了还是小，正确了退出并且提示输入正确（数字区间1-10）
num2 = random.randrange(0,11)

while True:
    try:
        num1 = int(raw_input(u'输入一个数字进行猜：'))
        if num1 == num2:
            print u'你猜对了'
            break
        elif num1>num2:
            print u'你猜的数字大了'
        elif num1 < num2:
            print u'你猜的数字小了'
    except Exception,e:
        print u'输入错误！'
        break
# 常用异常
# NameError
# try:
#     print a
# except NameError,e:
#     print u'定义变量异常'
#
# IOError
try:
    with open('cmm\\file.txt','r') as fp:
        s = fp.readlines()
        print s
except IOError,e:
    print u'文件不存在',e
SyntaxError
print 'list[11],11'

# 练习题2:  向文件中写入一行文本失败，捕获失败的异常，并打印
# try:
#     try:
#         fp = open('D:\\cmp\\c3.txt','r')
#     except IOError,e:
#         print u'打开文件异常',e
#     else:
#         try:
#             fp.write('hello world!')
#         except IOError,msg:
#             print u'写入异常',msg
#         else:
#             try:
#                 fp.close()
#             except IOError,ms:
#                 print u'关闭文件异常',ms
#     finally:
#         fp.close()
# except NameError:
#     pass

try:
    xf = open('D:\\cmp\\c3.txt','r')
    try:
        xf.write('abc')
    except IOError,i:
        print i
    else:
        print 'has no excetion'
    finally:
        print 'aaa'
        xf.close()
except Exception,e:
    print e
try:
    try:
        filepath = raw_input(u'请输入一个文件路径：')
        fp = open(filepath,'r')
        list1 = fp.readlines()
        num1 = len(list1)
        int1 = int(raw_input(u'请需要读取的行数：'))
        for i in xrange(int1):
            print list1[i]
    except IOError,e:
        print u'文件读写异常',e
    except ValueError,v:
        print u'输入值异常',v
    except IndexError,i:
        print u'输入的行数大于，文件中的总行数',i
    finally:
        fp.close()
except Exception,ec:
    print u'存在异常'

#输入一个字符，长度超过2个就抛出异常，没有异常打印成功

class MyExcetion(Exception):
    def __init__(self,stra):
        self.stra = stra

    def myMethod(self):
        print '自定义异常'
        return self.stra+u'长度超过2个'

try:
    num1 = raw_input(u'请输入一个字符串：')
    if len(num1) > 2:
        raise MyExcetion(num1)
except EOFError,e:
    print u'没有输入异常参数'
except MyExcetion,s:
    print s.myMethod()
else:
    print num1
class myException(Exception):
	def __init__(self,stra):
		self.stra=stra
		#设置长度
	def myMethod(self):
		stra = self.stra
		if len(stra) >2:
			raise Exception('the length is more than 2')
		else:
			print 'the length is less than or equal 2'
try:
	raise myException('awwa')
except myException,myex:
	myex.myMethod()



























