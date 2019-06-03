# encoding=utf-8
#continue语句是跳出本次循环，和break不同的是，break是跳出整个循环，遇到continue的时候，循环中剩余的语句将不再循环，而是继续进行下一轮循环
for i in 'Python':
    if i == 'h':
        continue
    print u'遍历当前字母',i
var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print u'遍历当前值：',var
print u'结束'