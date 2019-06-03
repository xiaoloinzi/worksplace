# encoding=utf-8
with open('user_info.txt','r') as user_file:
    lines = user_file.readlines()

for line in lines:
    username = line.split(',')[0]
    password = line.split(',')[1]
    print username,password