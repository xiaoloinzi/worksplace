# encoding=utf-8
# 2. 输入a，b，c，d4个整数，计算a+b-c*d的结果
def funCsum():
    a = int(raw_input('plese input the number-a:'))
    b = int(raw_input('plese input the number-b:'))
    c = int(raw_input('plese input the number-c:'))
    d = int(raw_input('plese input the number-d:'))
    sum = a + b - c * d
    return 'a + b - c * d = %d'%sum

print funCsum()
