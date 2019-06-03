# encoding=utf-8
# 10.判断一个数n能否同时被3和5整除
#输入一个数n对于3和5取模，如果取模是0则可以整除

while True:
    number1 = int(raw_input('please input the number:'))
    if number1 % 3 == 0 and number1 % 5 == 0:
        print u'你输入的数值可以同时整除3和5'
        break
    else:
        print u'你输入的数值不能同时整除3和5，请重新输出'
