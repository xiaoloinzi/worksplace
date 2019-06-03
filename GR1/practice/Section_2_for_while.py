# # # encoding=utf-8
# # # 练习题：嵌套循环输出10-50中个位带有1-5的所有数字
# #
# # for i in range(10,51):
# #     if i % 10 == 5:
# #         print i
# def create_counter(n):
#     print "create counter"
#     while True:
#         yield n
#         print 'increment n'
#         n += 1
#
# cnt = create_counter(2)
# print cnt
# print next(cnt)
# print next(cnt)

class getoutofloop(Exception):pass
try:
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if i == j == k == 3:
                    raise getoutofloop()
                else:
                    print i, '----', j, '----', k
except getoutofloop:
    pass