# # encoding=utf-8
# list = [4,3,6]
# list1 = [x+x for x in list]
# print list1
# sun = 0
# list2 = []
# for x in list:
#     sun += x
#     list2.append(sun)
# print list2
#
# print len(list)-1
# for i in range(len(list)-1):
#     print i
str1 = "If you do not learn to think when you are young, you may never learn"
list1 = str1.replace(',','').replace('.','').split(' ')
dict1 = {}

for i in list1:
    if dict1.has_key(i):
        dict1[i] += 1
    else:
        dict1[i] = 1

print dict1

for key,value in dict1.items():
    if value == max(dict1.values()):
        print u'出现最多次数的IP是',key
