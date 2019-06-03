# encoding=utf-8
# 6. 怎么得到9 / 2的小数结果
#先使用math.modf()，把整数和小数部分分开，在遍历取值
import math
sine = float(9)/float(2)
for i in math.modf(sine):
    if i < 1:
        print u'9/2的小数结果是:',i
    else:
        break
