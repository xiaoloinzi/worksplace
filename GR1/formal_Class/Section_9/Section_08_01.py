# encoding=utf-8
import time
import datetime
# 讨论一
# 遇到问题的解决方式
# 1、目标（不需要找到原因/需要找到原因）
# 1）、插拔法、比较法
# 2）、问题定界--os/平台/应用软件
#
# 3）问题定位
# 日志/截图/百度
#
# 讨论二
# 学有余力的，该如何更好的学习Python
# 1、看现在
# 1）写自动化测试框架--（1）日志、日志产生的时间点
# （2）2017-05-31 09:23:34|error|xxx
# （3）性能相关--统计API的响应时间
#
#
# 2）写自动化测试工具
# 3）Python核心编程精读
# 4）工作中勇于表达
# 5）优化框架
# time.sleep(5)
# xxx
# assert ()
# 固定等待-->循环校验、超时时间设置
#
#
# 2、看未来
# Python语言入门容易、精通的人非常少
# Python应用领域太广
# 应用领域：
# 大数据、AI
# 企业经营模式->总投入、总盈利
# 精细化经营
# 采集->
# BI->

# 时间元组
t1 = time.localtime()
print t1
print t1.tm_year
print t1.tm_min
print t1[0]
print t1[1]
#
# # 时间戳
t2 = time.time()
print t2
# # 时间戳转换为时间元组
#
print time.localtime()
time.sleep(10)
print time.localtime(t2)
print time.localtime()
# 1、分别调用time.time()函数 以及 time.localtime()函数，
# 说出他们的区别
# 2、遍历打印时间元组，并且说明其中每一个元素的意思
# 3、打印出如下的字符串，不允许使用time模块除了time()
# 和localtime()之外的函数：
# 2017-05-31 09:23:34
# 2017/05/31 09:23:34

print time.time()#显示的时间戳，以秒为单位
print time.localtime()#显示的是时间元组
time1 = time.localtime()
for i in time1:
    print i,
print
print str(time1[0])+'-'+str(time1[1])+'-'+str(time1[2])+' '+str(time1[3])+\
      ':'+str(time1[4])+':'+str(time1[5])
print str(time1[0])+'/'+str(time1[1])+'/'+str(time1[2])+' '+str(time1[3])+\
      ':'+str(time1[4])+':'+str(time1[5])
# # tm_year=2017,--表示的是年份 tm_mon=5--表示的是月份, tm_mday=28,--表示的是这个月的天数
# # tm_hour=10--表示的是小时, tm_min=0--表示的是分钟,
# # tm_sec=51--表示的是秒钟, tm_wday=6--表示的是周数，0为周一, tm_yday=148--表示的是今年的天数,
# # tm_isdst=0--表示的是夏令时
#
print "%d-%d-%d %d:%d:%d"%(time1[0],time1[1],time1[2],time1[3],time1[4],time1[5])
# gmtime--世界协调时间，比time.localtime()少8个小时
t1 = time.gmtime()

# 把元组转换为时间戳mktime()
print time.mktime(t1)

time1 = time.time()
time.sleep(5)
endtime = time.time()
print time1-endtime

#获取当前时间的格式化时间
#星期的简写
#星期的全写
t4 = time.localtime()
print time.strftime('%Y-%m-%d %H:%M:%S',t4)
print time.strftime('%c',t4)#t4加不加区别为，指定时间和当前时间
print time.strftime('%A',t4)
print time.strftime('%a',t4)

#日期时间的格式化
#月份的简写
#月份的全写
print time.strftime('%c',t4)
print time.strftime('%b',t4)
print time.strftime('%B',t4)

#日期字符串
#时间字符串
#今天是这周的星期几
print time.strftime('%X',t4)
print time.strftime('%x',t4)
print time.strftime('%w',t4)

#今天是今年的第几天
#这周是今年的第几周
print time.strftime('%U',t4)
print time.strftime('%j',t4)

# strftime()
# strptime()把时间字符串逆向转化为时间元组
strTime = '2017-05-28 09:45:42'
formatTime = time.strptime(strTime,'%Y-%m-%d %H:%M:%S')
print formatTime



# 3、实现如下的函数，写日志函数，要求写文件，
# def writeLog(msg, timeType):
# 其中timeType是0，则写本地时间，1写UTC时间
# 日志类型：
# 2017-04-24 12:00:00|xxxxxxxxxxxxxxxxx

def writeLog(msg,timeType):
    if timeType!=0 and timeType!= 1:
        print 'param timeType error,the value is',timeType
        return False
    with open('D:\\tmp\\log.txt','a') as fp:
        if timeType==0:
            aStr = time.strftime('%Y-%m-%d %H:%M:%S') +'|'+msg+'\n'
            fp.write(aStr)
        elif timeType==1:
            aStr = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()) +'|'+msg+'\n'
            fp.write(aStr)

writeLog('utc time log',1)
writeLog('local time log',0)

# 4、使用上面的题目的函数，写10行日志，并记录或计算程序的时间

#datetime
# localtine ->strftime()
print datetime.date
print datetime.time
print datetime.datetime.now()#秒表示的是微秒
tw = datetime.datetime.now()
print tw
print tw.year
print tw.month

# fromtimestamp--时间戳转化时间元组，或者转datetime
te = time.time()
dt = datetime.datetime.fromtimestamp(te)
print dt
print type(dt)

# strftime()格式化时间字符串
print tw.strftime('%Y-%m-%d %H:%M:%S %a %A')

# replace
t5 = tw.replace(month=4,hour=23)
print t5

t6 = tw-t5
print type(t6)
print t6


















