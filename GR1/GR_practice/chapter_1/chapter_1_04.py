# encoding=utf-8
#4. 3个人在餐厅吃饭，想分摊饭费。总共花费35.27美元，他们还想给15%的小费。每个人该怎么付钱，
#编程实现,使用浮点数
totalCost = 35.27
tip = 15.00/100.00
averageEach = (totalCost * tip + totalCost) /3.00
print u'每个人该给%2.2f美元'%averageEach