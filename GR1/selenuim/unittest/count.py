# encoding=utf-8
# 判断质数
def is_prime(n):
    if n <= 1:
        return False
    for i in xrange(2,n):
        if n%i == 0:
            return False
        return True


