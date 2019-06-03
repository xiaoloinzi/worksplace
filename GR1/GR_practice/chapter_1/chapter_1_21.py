# encoding=utf-8
# 21输入3个数字， 以逗号隔开， 输出其中最大的数
#让用户一次性输入三个数，以逗号隔开，然后在遍历判断是否有逗号，把数字取出来放到列表中，然后列表排序，最后输出排在前面的数据
#Python split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
#str.split(str="", num=string.count(str)).
# 参数
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。
# 返回值
# 返回分割后的字符串列表。
sine = raw_input(u'请输入三个数，以英文逗号隔开：')
sine = sine.split(',')
list1 = []

for i in sine:
    if i !=',':
        i = int(i)
        list1.append(i)

list1.reverse()
print u'您输入的三个数中最大的数是：',list1[0]
