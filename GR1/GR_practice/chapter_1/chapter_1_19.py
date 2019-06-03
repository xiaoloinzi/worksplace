# encoding=utf-8
# 19输入一个正整数， 输出其阶乘结果
sun = 1
while True:
    try:
        sine = int(raw_input(u'请输入一个正整数：'))
        if sine > 0:
            for i in range(1,sine+1):
                sun *= i
            print sine,u'的阶乘结果是',sun
            break
        else:
            print u'输入错误'
    except ValueError:
        print u'输入错误'
