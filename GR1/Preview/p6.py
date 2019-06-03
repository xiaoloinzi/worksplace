# # encoding=utf-8
filePath = 'D:\\worksplace\\GR1\\test1.txt'
f = open(filePath,'w')
stra = 'hello world!!'
f.write(stra)
lista = ['a','b','c']
f.writelines(lista)
dica = {'key1':'a','key2':'b'}
f.writelines(dica)
tuplea = ('a','b','c')
f.writelines(tuplea)
f.close()
#请将lista列表中的值['this','is','your','first','file']写入一个文件中，
# # 要求每个值占用一行,并在最后一行签上自己的名字(要求中文)
listb = ['this','is','your','first','file']
filePath = 'D:\\worksplace\\GR1\\test1.txt'
f = open(filePath,'w')
for i in listb:
    f.write(i+'\n')
    #f.writelines('\n')
f.writelines(u'林春莲')
f.close()
#思路：1、定义一个列表
#2、定义一个文件，指定文件路径
#3、打开这个文件
#4、将内容写入文件
#4.1值从列表中获取出来
#4.2一行一行去写入，循环取列表中的值，
#5、写上自己名字
#----------write和writelines的区别：write是每次都是写字符串，writelines多个元素进行写入
filePath = 'D:\\worksplace\\GR1\\test1.txt'
f = open(filePath,'r')
#文件都有文件句柄，读写文件都需要关闭文件使用。close（）
strb = f.read()
strc = f.readlines()
print strc
for line in open(filePath,'r'):
    line = f.read()
    print line
f.close()
#请将生成的文件读写并使用列表的形式打印出来
#并将结果还原成原始状态,需要去掉用户名并打印出来
#思路：1.读文件（文件路径）
#2、定义一个列表
#3、read/readlines
#4、内容添加到列表中（转换内容）再添加到列表中去
#4.1必须留下单行字符串
#4.2去掉名字并打印出来
#5、打印列表内容
listS = []
for line in f.readlines():
    line = line.strip('\n')
    if line.decode("utf-8")!= "林春莲":#.decode("utf-8")--转换后比较Unicode字符
        listS.append(line)
    else:
        print line
f.close()
print listS
