# encoding=utf-8







list1 = [2,5,1,78,87,34,234,64,4,3]
print len(list1)
for i in xrange(len(list1)//2,-1,-1):
    print i,":",2*i+1,":",2*i+2
    print i
#
# n=5 lager = 5 letf = 11 right =12
# n=4 lager = 4 letf = 9 right =10
# letf = 9---heap[4]=87--heap[9]=3--不满足
# n=3 lager = 3 letf = 7 right =8
# letf = 7--heap[3]=78--heap[7]=64--不满足
# right = 8--heap[3]=78--heap[8]=4---不满足
#
# n=2 lager = 2 letf=5 right = 6
# letf = 5--heap[2]= 1--heap[5]=34--满足
# lager = left = 5
# right=6--heap[5]=34--heap[6]=234--满足
# lager = right=6
# lager=6!=n=2
# heap[6],heap[2]=heap[2],heap[6]---234,1,1,234













