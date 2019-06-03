# encoding=utf-8
# [2017.03.26]
# windows的编码是gbk编码形式，要在cmd上进行运行要进行转码
#使用下面的程序在cmd上输出
# 请分别在cmd 命令下，以及pycharm下，
# 使用raw_input()方法，打印“请输入字符:”
#  sine = '请输入字符：'
# sine1 = sine.encode("GBK")
# raw_input(sine1)
raw_input(u'请输入字符:'.encode('gbk'))#在cmd上输出没有问题
# s1 = '光荣之路'
#
# print s1#utf-8编码形式--在cmd上出现乱码，因为当前的编码格式是utf-8
# print s1.decode('utf-8')#print会把Unicode编码格式主动转换成对应平台的编码方式--cmd上的格式没有出现乱码
# print s1.decode('utf-8').encode('gbk')#已经转换为gbk的编码格式，所以在utf-8的编码格式平台会出现乱码。---在cmd上没有出现乱码是因为Windows上的编码方式是gbk
# #在cmd上进行，然后报错的原因
# #u'中文'.decode('gbk')---ASCII不正常中文
# #u'中文'.decode('utf-8')---编码格式不支持

