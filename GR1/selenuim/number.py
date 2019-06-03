# encoding=utf-8
from random import randint

# 生成一个人1000到9999之间的随机数
verify = randint(1000,9999)
print u'生成的随机数是：%s'%verify

number = raw_input(u'请输入一个随机数：')
print number
number = int(number)

if number == verify:
    print u'登录成功'
elif number == 132741:
    print u'登录成功'
else:
    print u'验证码输入失败'

