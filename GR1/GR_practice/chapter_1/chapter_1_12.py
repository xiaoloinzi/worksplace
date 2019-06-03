# encoding=utf-8
# 12交换两个变量的值
#使用Python中特殊的形式，x,y=y,x
x = raw_input(u'请输入变x的值，按回车键结束：')
y = raw_input(u'请输入变y的值，按回车键结束：')
x,y = y,x
print u'x和y的值',x,y