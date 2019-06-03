# encoding=utf-8
## 15 现有面包、热狗、番茄酱、芥末酱以及洋葱，数字显示有多少种订购组合，其中面包必订，0不订，1订，比如10000，
# 表示只订购面包
#16 基于上题：给出每种食物的卡路里（自定义），再计算出每种组合总共的卡路里
#面包的卡路里是1
bread = 312
hotdog = 250
ketchup = 81
mustard = 84
onion = 39
lists = []
listw = {}
s = 0
sine = 0
for i in range(2):
    for j in range(2):
        for n in range(2):
            for u in range(2):
                s +=1
                sun = 1*10000+i*1000+j*100+n*10+u
                lists.append(str(sun))
for d in lists:
    d = int(d)
    d1 = d % 10
    d2 = (d/10)%10
    d3 = (d/100)%10
    d4 = (d/1000)%10
    d5 = d/10000
    sun1 = d5*bread + d4*hotdog + d3*ketchup + d2*mustard + d1*onion
    listw[d] = sun1
print u'不同种组合搭配的总卡路里如下：',listw