# encoding=utf-8
# 3. 计算一周有多少分钟、多少秒钟
#一周有7天，一天有24小时，一小时有60分钟，一分钟有60秒
weed1 = int(raw_input('pleae input you need Calculation the number of weeks: '))
minute = weed1 * 7 * 24 * 60
second = weed1 * 7 * 24 * 60 * 60
print u'%d周有%d分钟%d秒'%(weed1,minute,second)