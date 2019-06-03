# encoding=utf-8
# 22输入一个年份， 输出是否为闰年
# 是闰年的条件：
# 能被4整数但不能被100整除， 或者能被400整除的年份都是闰年。
#判断闰年条件①：非整百年数除以4，无余为闰，有余为平；②整百年数除以400，无余为闰有余
#让用户输入一个年份
#判断是否能被4整除并且不能被100整除，或者能被400整除就是闰年

# sine = int(raw_input(u'请输入一个年份：'))
#
# if (sine % 4 == 0 and sine % 100 != 0) or sine % 400 == 0:
#     print sine,u' 是闰年'
# else:
#     print sine,u' 不是闰年'


#输出某年到某年的所有闰年
#要求用户输入开始的年份和结束的年份

sine1 = int(raw_input(u'请输入开始计算的年份：'))
sine2 = int(raw_input(u'请输入结束计算的年份：'))
list1 = []
s = 0

for i in range(sine1,sine2+1):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        list1.append(i)
        s += 1

print u'你输入的年份中',s,u'个闰年，如下：',list1
