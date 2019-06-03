# encoding=utf-8

def yunSuan():
    str1 = raw_input(u'请输入5个数，之间用空格隔开：')
    str2 = raw_input(u'请输入结果：')
    list1 = str1.split(' ')
    list2 = []
    for i in ['*','/','+','-']:
        for j in ['*','/','+','-']:
            for s in ['*','/','+','-']:
                for n in ['*','/','+','-']:
                    sun1 = eval(list1[0]+i+list1[1]+j+list1[2]+s+list1[3]+n+list1[4])
                    sun2  = eval(list1[1]+j+list1[2]+s+list1[3]+n+list1[4])
                    sun3 = eval(list1[2]+s+list1[3]+n+list1[4])
                    sun4 = eval(list1[3]+n+list1[4])
                    if (i=='/'and sun2 == 0) or (j=='/'and sun3 == 0) or (s=='/'and sun3 == 0) or (n=='/'and sun4 == 0):
                        continue
                    if sun1 == int(str2):
                        son = list1[0]+i+list1[1]+j+list1[2]+s+list1[3]+n+list1[4]+'='+str2
                        list2.append(son)
    for i ,j in enumerate(list2):
        print i+1,j

if __name__=='__main__':
    yunSuan()


















