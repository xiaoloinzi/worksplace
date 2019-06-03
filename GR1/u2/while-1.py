# encoding=utf-8
#使用while和if的判断猜数字游戏
while True:
    number1 = int(raw_input('please input you like number:'))
    if number1 == 25:
        print 'you win!'
        break
    elif number1 < 25:
        print 'you input number is small'
    else:
        print 'you inout number is Big'
