# encoding=utf-8
# 搜索str.find(substr,[start,[end]]),substr子串必填
s = 'I an a girl.'
print s.find('a')
print s.find('a',3)
print s.find('a',6,7)

# s.index(substr,[start,[end]])
print s.index('girl',1)
print s.index('girl',1,13)

# 实现find的方法：


def Find(str,subStr,start = 0, end = None):
    a = len(subStr)
    for i in xrange(start,len(str)):
        if subStr == str[i:i+a]:
           return i
    else:
        return -1
s = 'I an a girl.'
print Find(s,'girl')
print Find(s,'an',1,8)
print Find(s,'an')

# 1、只能查找一个子字符串；2、可以没有start参数，只有end参数是不能执行的
# 3、当start大于end时，返回错误信息；4、对于参数个数没有校验
# 防御性编程：1、所有的入参是否做校验；2、所有的异常是否有捕获
# 3、过载如何处理；4、队列满等如何处理

def find(sourceStr,subStr,**kwargs):
    start = 0
    end = len(sourceStr)-1
    if len(kwargs)>2:
        print 'paremeters error'
        return -1
    if kwargs.has_key('start'):
        start = kwargs['start']
        if kwargs.has_key('end'):
            end = kwargs['end']
        else:
            if len(kwargs) != 1:
                print 'paremeter error'
    else:
        if len(kwargs)!=0:
            print 'paremeter error'
            return -1
    if not isinstance(start,int) or not isinstance(end,int):
        print 'type error'
        return -1
    if start>end:
        print 'parameter error'
        return -1

    if subStr not in sourceStr[start:end +1] or len(subStr)==0:
        return -1
    for i in xrange(start,end+1):
        if sourceStr[i:i+len(subStr)] == subStr:
            return i
    return -1
print find('ancdefg','cd',end=1)








