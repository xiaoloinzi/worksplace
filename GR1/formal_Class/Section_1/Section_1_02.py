# encoding=utf-8
# #s1从字节字符串转换成Unicode编码
# s1 = '光荣之路'
# print type(s1)
# print type(s1.decode())
# print s1
# 题目：手工创建一个文件，d:\\testfile.txt，
# 写上中文，此文件的编码格式是？写程序读取文件，
# 并且打印出来。把文件的编码修改成utf-8，
# 之后再次读取文件，并且打印出来
# 分别在pycharm 和 cmd 上面显示
#先调用open方法打开文件
#调用read方法，读取文件
#打印文件内容，并且UTF-8和gbk终端上
fp1 = open('D:\\testfile3.txt','r')

info1 = fp1.read()
tmp = info1.decode('gbk')
print tmp
fp1.close()
#decode('gbk')
#encode('utf-8')
#调用write()
fp2 = open('D:\\testfile3.txt','w')
info2 = tmp.encode('utf-8')
fp2.write(info2)
fp2.close()
f3 = open('D:\\testfile3.txt','r')
info3 = f3.read()
print info3
f3.close()
print type(info3)
#把修改格式后的文件，
# 分别使用gbk和utf-8解码，之后打印。





f1 = open('testfile.txt','r',)
info1 = f1.read()
print info1
f1.close()
print type(info1)
info2 = info1.decode('gbk').encode('utf-8')
print info2
print type(info2)
f2 = open('testfile.txt','w')
f2.write(info2)
f2.close()
f3 = open('testfile.txt','r')
info3 = f3.read()
print info3
f3.close()
print type(info3)



