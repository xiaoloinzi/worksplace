# encoding=utf-8
# 9. 一家商场在降价促销。如果购买金额50-100元（包含50元和100元）之间，会给10%的折扣，如果
# 购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（10%或20%）和
# 最终价格
#先输入一个数值，然后在判断这个数值在哪个范围内，然后打印出来
#20%的折扣是8折，10%的折扣是9折
#思路：
#1、输入价格
#2、判断价格，并且显示出折扣
price = float(raw_input('please input you purchase price :'))
if price > 100:
    discount1 = float(1)-float(20)/float(100)
    sum = price * discount1
    print u'你可以打%d折,你需要付款的金额是%0.2f元'%(discount1*10,sum)
elif 50<= price and price<=100:
    discount2 =float(1)- float(10)/float(100)
    sum = price * discount2
    print u'你可以打%d折,你需要付款的金额是%0.2f元'%(discount2*10,sum)
else:
    print u'你消费的金额是%0.2f元'%price

