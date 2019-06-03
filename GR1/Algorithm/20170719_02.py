# encoding=utf-8
'''
母亲为儿子sum的四年学费准备了一笔存款，方式死整存零取，规定sum
每个月底取下一个月的生活费，现在假设银行的年利息是1.71%，请编写
程序计算母亲最少要存多少钱
'''
lista = [1000]
s = 1000/(1+0.0171/12)
for i in xrange(1,48):
    s = (s+1000)/(1+0.0171/12)
    lista.append(s)
lista = lista[::-1]
for i in range(1,len(lista)+1)[::-1]:
    print i,'个月末存款%0.2f'%lista[i-1]



















