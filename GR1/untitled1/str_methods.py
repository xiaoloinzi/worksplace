#encoding=utf-8
name = 'Swaroop'#This is a string object
if name.startswith('Swa'):
    print("Yes ,the string starts with \"Swa\"")
if 'e' in name:
    print("Yes ,it containts the string \"a\"")
if name.find('war') != -1:
    print("Yes,it constains the string \"war\"")
delimiter = '_*_'
mylist = ['Brazil','Russia','India','China']
print(delimiter.join(mylist))