# encoding=utf-8
#文档注释
# def complex(real=0.0,img=0):
#     '''
#
#     :param real:
#     :param img:
#     :return:
#     '''
#
#
#     pass

def Sum(x,y):
    '''
    这个方法：输入两个数值，返回两个数值的和
    :param x: 输入的是一个加数的数值
    :param y: 输入的是一个加数的数值
    :return:调用这个方法后，返回的是x和y的和
    '''
    sum1 = x + y
    return sum1
print Sum(1,3)
#显示注释信息
help(Sum)

#生成注释文档
if __name__=="__main__":
    help(Section_1_08)
