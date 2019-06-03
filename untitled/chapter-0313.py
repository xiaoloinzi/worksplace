# encoding=utf-8
print abs(-4)
myString = 'Hello World'
print myString
mystr1 = '3'
print str(mystr1)
print repr(mystr1)
print '%s in number %d!'% ('python',1)
logfile = open('myfile.txt','a')
print >>logfile,'Fatal error:invalid input!'
logfile.close()
user = raw_input('enter login name:')
print 'you login is:',user
num = raw_input('now enter a number:')
print 'Doubling your number:%d'%(int(num)*2)
print 'your number :%s'%num
print -2 * 4 + 3 ** 2
print 2 < 4 and 2 == 4
print 2 > 4 or 2 < 4
print not 6.2 <= 6
print 3 < 4 < 5#不合理的写法
print 3 < 4 and 4 < 5#合理的写法
counter = 0
miles = 1000.0
name = 'Bob'
counter = counter + 1
kilometers = 1.609 * miles
print '%f miles is the same as %f km'%(miles,kilometers)
print '0 counter is the same as %d,the name is %s'%(counter,name)
number1 = 1.1
print number1
pystr = 'python'
iscool = 'iscool'
print pystr[0],iscool[5],iscool[-1]
print pystr[1:3],iscool[2:3],iscool[3:]
print pystr + iscool
print pystr*2
print iscool*2*2
pystr1 = '''python
is cool'''
print pystr1
pystr2 = 'python\nis\ncool'
print pystr2
alist = [1,2,3,4]
print alist
print alist[3],alist[1:4]
alist[1] = 5
print alist
aTuple = ('robot',77,93,'try')#元组不能被修改
print aTuple,'\n',aTuple[3],'\n',aTuple[:3]
aDict = {'host':'earth'}
aDict['port'] = 80
print aDict,'\n',aDict.keys(),'\n'
for key in aDict:
    print key,aDict[key]
