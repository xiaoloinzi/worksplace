# encoding=utf-8

fp = open('data.log','r')

for str in fp:
    xf = open(str[:8]+'.txt','a')
    xf.writelines(str[14:])
    xf.close()
fp.close()