# # encoding=utf-8
# str = "hello boy<[www.baidu.com]>byebye"
# print str.split("[")[1].split("]")[0]#先执行前边的，后边的又在前边的结果上进行


str = [(1,2,3),11,21,(4,5,6),(7,8,9),10]
for i in str:
    if isinstance(i ,tuple):
        for s in i:
            print s
    # else:
    #     print i