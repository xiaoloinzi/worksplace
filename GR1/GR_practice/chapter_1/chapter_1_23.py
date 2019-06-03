# encoding=utf-8
# 23求两个正整数m和n的最大公约数
#输入两个数字，判断哪个数字最大，然后遍历这个数字的数值，给两个数进行整除，
# 能被两个数都整除的数写入列表，对列表进行排序，取最大的值显示出来

sine1 = int(raw_input(u'请输入第一个要计算的数：'))
sine2 = int(raw_input(u'请输入第二个要计算的数：'))
list1 = []

if sine1 >= sine2:
    for i in range(1,sine1):
        if sine1 % i == 0 and sine2 % i == 0:
            list1.append(i)
else:
    for i in range(1,sine2):
        if sine1 % i == 0 and sine2 % i == 0:
            list1.append(i)
list1.reverse()
print u'最大的公约数是：',list1[0]