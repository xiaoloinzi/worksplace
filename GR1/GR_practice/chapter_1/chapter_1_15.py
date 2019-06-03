# encoding=utf-8
# 15 现有面包、热狗、番茄酱、芥末酱以及洋葱，数字显示有多少种订购组合，其中面包必订，0不订，1订，比如10000，
# 表示只订购面包
s = 0
for i in range(2):
    for j in range(2):
        for n in range(2):
            for u in range(2):
                s +=1
                print 1*10000+i*1000+j*100+n*10+u
print u'显示有%d种组合'%s
