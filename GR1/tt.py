# encoding=utf-8

list1 = []
with open('test.dat','w') as fp:
    for i in xrange(1000):
        list1.append("test"+str(i)+"\n")
    fp.writelines(list1)

