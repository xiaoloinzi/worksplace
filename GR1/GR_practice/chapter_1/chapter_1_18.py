# encoding=utf-8
# 18实现一个简单的单词本
# 功能：
# 可以添加单词和词义，当所添加的单词已存在，让用户知道；
# 可以查找单词，当查找的单词不存在时，让用户知道；
# 可以删除单词，当删除的单词不存在时，让用户知道；
# 以上功能可以无限制操作，直到用户输入bye退出程序。
#先要求用户是添加单词还是查找单词，还是删除单词，让用户输入两个值，一个是单词，一个是词义，如果用户输入的单词是bye则退出，
# 否则判断这个单词是否存在，存在就打印已存在，
dict1 = {}
siner = 0
while siner != 'bye':
    siner = raw_input(u'请选择：1为添加单词，2为查找单词，3为删除单词，退出程序请输入bye,按回车键结束：')
    if siner == '1':
        item1 = raw_input(u'请输入你要添加的单词，按回车键结束：')
        if item1 in dict1.keys():
            print u'你添加的单词已经存在，请重新添加'
        else:
            item2 = raw_input(u'请输入你已添加单词的词义，按回车键结束：')
            dict1[item1] = item2
            print u'你输入的单词 %s 已添加，请继续操作'%item1
    elif siner == '2':
        item3 = raw_input(u'请输入你要查找的单词，按回车键结束：')
        if item3 in dict1.keys():
            print u'单词：',item3,u'词义：',dict1[item3]
        else:
            print u'你查找的单词不存在，请继续操作'
    elif siner == '3':
        item4 = raw_input(u'请输入你要删除的单词，按回车键结束：')
        del dict1[item4]
        print item4,u'已删除，请进行操作'
    elif siner != 'bye':
        print u'操作失误，请重新输入'
        continue
print u'程序已退出,谢谢使用！'







