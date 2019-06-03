# encoding=utf-8
# 17输入5个名字，排序后输出
#先让用户分别输入五个名字，然后再进行倒序
import chardet
listq =[]
for i in range(5):
    s = raw_input('plese input you name:')
    listq.append(s)
listq.reverse()#倒序排列.sor()是从小到大排序
print ' '.join(listq)


nameList = []
for i in range(1,6):
    print u'请输入第%d 个名字：'%i,
    nameList.append(raw_input())

nameList.sort()
print ' '.join(nameList)
