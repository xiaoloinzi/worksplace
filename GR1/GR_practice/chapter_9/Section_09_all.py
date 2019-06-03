# encoding=utf-8
import time
import os
import datetime
# 1、计算程序执行耗时
def hoashi():
    time.sleep(10)
time1 = time.time()
hoashi()
print u'程序耗时：',time.time()-time1
time2 = time.clock()
hoashi()
print u'程序的耗时：',time.clock()-time2

# 2、将时间字符串转换为时间戳
x = '2017-2-12 12:12:23'
time1 = time.localtime(x)
print time.mktime(time1)

# 老师的方法：
a = '2015-08-03 08:00:00'

tp = time.strptime(a,'%Y-%m-%d %H:%M:%S')
timeStamp = time.mktime(tp)
print timeStamp



# 3、将格式时间字符串转换成时间元组，然后再转换成自定义
# 的时间格式字符串
strx = '2017-2-12 12:12:23'
time1 = time.strptime(strx,"%Y-%m-%d %H:%M:%S")
time2 = time.strftime("%Y/%m/%d %H:%M:%S",time1)
print time1
print time2


# 4、将当前时间戳转换为指定格式日期

print  time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))



# 5、创建名称为当前时间(年月日)的目录，在这个目录下创建
# 名称为当前时间(年月日)的txt文件，并且输入内容为“你好”

strtime = time.strftime('%Y%m%d',time.localtime())
startpath = "D:\\tmp\\"+strtime+'\\'
os.makedirs(startpath)
str1 = strtime+'.txt'
with open(startpath+str1,'w') as fp:
    fp.write(u'你好')
# 老师的方法：
directoryName = time.strftime('%Y%m%d')
print directoryName
fileName = 'e:\\tmp\\'+directoryName+os.sep+directoryName+'.txt'

os.mkdir('e:\\tmp\\'+directoryName)
with open(fileName,'w') as fp:
    fp.write('你好')


# 6、获得三天（三小时和三分钟）前的时间方法

time1 = datetime.datetime.now()
print u'当前的时间：',time1
print u'三天前的时间：',time1-datetime.timedelta(days=3)
print u'三小时的时间：',time1-datetime.timedelta(hours=3)
print u'三分钟的时间：',time1-datetime.timedelta(minutes=3)

# 老师的方法：
threeDaysAgo = datetime.datetime.now() - datetime.timedelta(days=3)
threeHoursAgo = datetime.datetime.now() - datetime.timedelta(hours=3)
threeMinutesAgo = datetime.datetime.now() - datetime.timedelta(minutes=3)

print threeDaysAgo
print threeHoursAgo
print threeMinutesAgo


# 7、计算昨天和明天的日期
today = datetime.date.today()
strday = datetime.timedelta(days=1)
# strtime = datetime.datetime.now()
# print u'明天的日期：',strtime+strday
# print u'昨天的日期：',strtime-strday
print u'明天的日期：',today+strday
print u'昨天的日期：',today-strday

# 老师的方法：
tomorow = datetime.date.today() + datetime.timedelta(days=1)
print tomorow
print threeDaysAgo
print threeHoursAgo
print threeMinutesAgo

# 8、使用datetime模块来获取当前的日期和时间
print u'当前的日期：',datetime.datetime.now().date()
print u'当前的时间：',datetime.datetime.now().time()

# 老师的方法：
i = datetime.datetime.now()

print i.year
print i.month
print i.day
print i.hour


# 9、创建名称为log的目录，目录下创建三个文件夹，名分别
# 为去年今天的日期、当前日期(年月日)、明年今天的日期，
# 然后分别在这三个目录中创建三个.log文件，名分别为当年
# 的今天在当年中第多少天，文件中分别写入当年的今天是这
# 一年的第几个星期以及当前是星期几。


nows = datetime.datetime.now()

thisYear = nows.strftime('%Y%m%d')
thispath = 'D:\\'+thisYear
os.makedirs(thispath)
with open(os.path.join(thispath,nows.strftime('%j')+'.log'),'w') as fp:
    str1 = u'一年中的第%s'%nows.strftime('%U')+u'当前是%s'%nows.strftime('%A')
    fp.write(str1)


lastYear = nows.replace(year=nows.year+1).strftime('%Y%m%d')
lastpath = 'D:\\'+lastYear
os.makedirs(lastpath)
with open(os.path.join(lastpath,nows.replace(year=nows.year+1).strftime('%j')+'.log'),'w') as fp:
    str1 = u'一年中的第%s'%nows.replace(year=nows.year+1).strftime('%U')+u'当前是%s'%nows.replace(year=nows.year+1).strftime('%A')
    fp.write(str1)

previousYear = nows.replace(year=nows.year-1).strftime('%Y%m%d')
previouspath = 'D:\\'+previousYear
os.makedirs(previouspath)
with open(os.path.join(previouspath,nows.replace(year=nows.year-1).strftime('%j')+'.log'),'w') as fp:
    str1 = u'一年中的第%s'%nows.replace(year=nows.year-1).strftime('%U')+u'当前是%s'%nows.replace(year=nows.year-1).strftime('%A')
    fp.write(str1)

# 老师的方法：
def calcDays(date):
    formatDate =time.strptime(date,'%Y-%m-%d')
    dayInYear = time.strftime('%j', formatDate)
    weekInYear = time.strftime('%U',formatDate)
    dayOfWeek = time.strftime('%w', formatDate)
    return dayInYear,weekInYear,dayOfWeek

def writeFile(filePath):
    date = os.path.basename(filePath)
    dayInYear,weekInYear,dayOfWeek = calcDays(date)
    fileName = os.path.join(filePath,dayInYear+'.log')
    with open(fileName,'w') as fp:
        fp.write('%s,属于这一年中第%s个星期，今天是星期%s'%(date,weekInYear,dayOfWeek))

def createDir(rootDir):
    structTime = time.localtime()
    monthDay = time.strftime('%m-%d',structTime)
    thisYear = time.strftime('%Y-%m-%d',structTime)
    lastYear = str(int(structTime.tm_year)-1)+'-'+monthDay
    nextYear = str(int(structTime.tm_year)+1)+'-'+monthDay

    thisYearDir = os.path.join(rootDir,thisYear)
    lastYearDir = os.path.join(rootDir,lastYear)
    nextYearDir = os.path.join(rootDir,nextYear)

    if not os.path.exists(thisYearDir):
        os.makedirs(thisYearDir)

    if not os.path.exists(lastYearDir):
        os.makedirs(lastYearDir)

    if not os.path.exists(nextYearDir):
        os.makedirs(nextYearDir)

    writeFile(thisYearDir)
    writeFile(lastYearDir)
    writeFile(nextYearDir)

if __name__ == '__main__':
    rootDir = 'c:\\log'
    createDir(rootDir)








