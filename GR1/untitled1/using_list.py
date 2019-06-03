#encoding=utf-8
shoplist = ['apple','mango','carrot','banana']
print("I have",len(shoplist),"items to purchase")
print("these items are:")
for item in shoplist:
    print(item)
print("\n I also have to buy rice")
shoplist.append('rice')
print("my shpopping list is now",shoplist)
print("I will sort my list now")
shoplist.sort()
print("Sorted shopping list is ",shoplist)
olditem = shoplist[0]
del shoplist[0]
print("i bought the ",olditem)
print("my shopping list is now",shoplist)