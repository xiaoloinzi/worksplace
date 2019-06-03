# encoding=utf-8
# 实现 字符串的upper（str)\lower(str)

def upper(st):
    newStr = ''
    for i in st:
        if ord(i)>=97 and ord(i)<=122:
            i = chr(ord(i)-32)
            newStr += i
        else:
            newStr +=i
    return newStr

def lower(st):
    newStr = ''
    for i in st:
        if ord(i)>=65 and ord(i)<=90:
            i = chr(ord(i)+32)
            newStr += i
        else:
            newStr +=i
    return newStr


















