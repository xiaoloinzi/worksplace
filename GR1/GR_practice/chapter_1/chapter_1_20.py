# encoding=utf-8
# 20 计算存款利息
# 4种方法可选：
# 活期， 年利率为r1；
# 一年期定息， 年利率为r2；
# 存两次半年期定期， 年利率为r3
# 两年期定息， 年利率为r4
# 现有本金1000元， 请分别计算出一年后按4种方法所得到的本息和。
# 提示： 本息= 本金+ 本金* 年利率* 存款期
#把r当做一个百分比，则r1=1%，r2=%2,r3=%3,r4=%4
#活期本息= 1000 + 1000 * 0.01
# 一年期定息本息= 1000 + 1000* 0.02
# 存两次半年期定期本息= 1000 +1000 * 0.03//2 * 0.03/2
# 两年期定息本息=  1000+ 1000 * 0.04/2
hqi = 1000//4 + 1000 * 0.01
ydqi = 1000//4 + 1000* 0.02
lbdq = 1000//4 +1000 * 0.03/2 * 0.03/2
ldq = 1000//4 + 1000 * 0.04/2
sun = hqi + ydqi + lbdq + ldq
print u'一年后按4种方法所得到的本息和：%0.2f'%sun