# encoding=utf-8
fp1 = open('d:\\testfile.txt','r')
try:
    info1 = fp1.read()
    raise NameError
except Exception,e:
    print e.message
finally:#
    fp1.close()

#with
with open('d:\\testfile.txt','r') as fp2:
    info2 = fp2.read()
    raise NameError,'Name error'
    print info2