# encoding=utf-8
# 公鸡每只5元，母鸡每只3元，小鸡3只1元，
# 问用100元买100只鸡，公鸡、母鸡、小鸡各自多少只


for i in range(21):
    for j in range(34):
        for n in range(301):
            if (n % 3 == 0) and (i*5 + j*3 + n/3 == 100) and (i + j + n == 100):
                print u'公鸡：',i,u'母鸡：',j,u'小鸡：',n