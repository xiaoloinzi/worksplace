# encoding=utf-8
print 10 ** 4
print 2 ** 32

a = 8
#二进制以0b开头，bin()输出的是字符串
print u'a的二进制表示：',bin(a)
print u'a的二进制表示：',bin(a)[2:].zfill(len(bin(a)))

#&
b = 7
print a & b
#|
print a | b

#^
print a ^ b
#~
print ~a

#转八进制
print oct(a)
#转十六进制
print hex(a)

#对于16进制的数：0x456,0x323，求上述的所有操作

c = 0x456
d = 0x323

print bin(c)
print bin(d)
# &
print c & d
# |
print c | d
# ^
print c ^ d
#~
print ~c

e = int('0x456',16)
f = int('0x323',16)
print u'已转换为十进制后'
print bin(c)
print bin(d)
# &
print e & f

# |
print e | f
# ^
print e ^ f
#~
print ~e

