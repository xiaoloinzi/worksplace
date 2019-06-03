#encoding=utf-8
print("simple assignent")
shoplist = ['apple','mango','carrot',
            'banana']
mylist = shoplist#mylist is just anther name pointing to the same object
#mylist读取shoplist的内存，两个修改那个，另一个也会改变
print("shoplist is ",shoplist)
print("mylist is ",mylist)
del shoplist[0]
print("shoplist is ",shoplist)
print("mylist is ",mylist)
#notice that both shoplist and mylist both print the same list without
#the 'apple' confirming that they poit to the same object
del mylist[0]
print("shoplist is ",shoplist)
print("mylist is ",mylist)
print("copy by making a full slice")
mylist = shoplist[:]#make a copy by doing a full slice
#直接赋值，两者后面不相关，修改某一个，另一个不做改变
print("shoplist is ",shoplist)
print("mylist is ",mylist)
del shoplist[0]
print("shoplist is ",shoplist)
print("mylist is ",mylist)
del mylist[0]#remove first item
print("shoplist is ",shoplist)
print("mylist is ",mylist)
#notice that now the two lists are different