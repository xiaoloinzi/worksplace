# encoding=utf-8

# 【python每日一练】实现一个购物车功能，商品属性只需要包括名称，数量，价格，
# 要求实现添加一个商品，删除一个商品，最终打印订单详情和总价格
'''
1、写一个购物车的类，属性有商品名称，数量，价格，然后实现添加商品，删除商品、打印订单详情的方法
2、定义一个字典的数据结构进行存储数据，要判断输入的商品是否存在，存在则提示并不保存
'''
dict1 = {}
class Shopping(object):
    def __init__(self,product_name= None,price= None,quantity= None):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def addProduct(self):
        if self.product_name == None or self.price == None or self.quantity == None:
            return "product_name or price or quantity can not be empty not be empty!"
        if dict1.has_key(self.product_name):
            num = raw_input("The goods you have entered have been added to the shopping cart, whether to modify!(Y/N)")
            if num == "Y" or num == "y":
                dict1[self.product_name] = [self.price,self.quantity]
        else:
            dict1[self.product_name] = [self.price,self.quantity]

    def deleteProduct(self):
        if self.product_name == None or self.price == None or self.quantity == None:
            return "product_name or price or quantity can not be empty not be empty!"
        if not self.price.isdigit() and not self.quantity.isdigit():
            return "Price or quantity entered incorrectly"
        if dict1.has_key(self.product_name):
            del dict1[self.product_name]
        else:
            num = raw_input("The item you entered does not exist")

if __name__=="__main__":
    stration = ""
    while True:
        stration = raw_input("Please enter the goods you want to buy and the price and quantity, separated by commas")
        if stration == "quit":
            break
        num = int(raw_input("Do you need to add a product or delete a product?(1-add;2--delete)"))
        stration = stration.split(',')
        if len(stration) == 3:
            product = Shopping(stration[0],stration[1],stration[2])
            if num == 1:
                product.addProduct()
            elif num == 2:
                product.deleteProduct()
            elif num != 1 and num != 2:
                print "Sorry, the operation you entered does not exist, please start from scratch"
        else:
            print "The information you entered is incomplete"
    print u'商品名称'+'\t'+u'价格'+'\t'+u'数量'
    for i,j in dict1.items():
        print i+'\t\t'+j[0]+'\t\t'+j[1]















