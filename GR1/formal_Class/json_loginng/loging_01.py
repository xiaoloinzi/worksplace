# encoding=utf-8
import logging
import sys

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s %(levelname)s |%(message)s',
#     filename= 'D:\\tmp\\log\\log1.log'
# )#设置显示日志的级别
# # 不设置的情况下，只显示error和waring
# # 日志的级别
# # CRITICAL>ERROR >WARNING>INFO>DEBUG>NOTEST
#
# format：指定handler使用的日志显示格式，即日志打印的格式字符串。可
# 用到的格式化串：
# %(name)s：Logger的名字；
# %(levelno)s：日志级别的数值；
# %(levelname)s：日志级别名称；
# %(pathname)s：当前执行程序的路径，其实就是sys.argv[0]，可能没有；
# %(filename)s：调用日志输出函数的模块的文件名；
# %(module)s：当前执行程序的程序名；
# %(funcName)s：日志输出函数的函数名；
# %(lineno)d：日志输出函数的语句所在的代码行；
# %(created)f：当前时间，用UNIX标准的表示时间的浮点数表示；
# %(relativeCreated)d：输出日志信息时的，自Logger创建以来的毫秒数；
# %(asctime)s：字符串形式的当前时间。默认格式是 “2016-06-06
# 16:49:45,896”。逗号后面的是毫秒；
# %(thread)d：线程ID。可能没有；
# %(threadName)s：线程名。可能没有；
# %(process)d：进程ID。可能没有；
# %(message)s：用户输出的消息；
# logging.debug('debug log')
# logging.info('info log')
# logging.warning('warning')
# logging.error('error log')

# 习题：自定义一个格式的输出日志，包括时间、
# 调用日志输出函数的模块的文件名、当前执行程序的程序名、
# 日志级别、日志内容，日志级别是debug级别，写入日志文件



logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s |%(filename)s|%(module)s |%(message)s|%(levelname)s',
    filename= 'D:\\tmp\\log\\log1.log',
    filemode='a+'
)#设置显示日志的级别
# # 不设置的情况下，只显示error和waring
# # 日志的级别
# CRITICAL>ERROR >WARNING>INFO>DEBUG>NOTEST

logging.debug('debug log')
logging.info('info log')
logging.warning('warning')
logging.error('error log')


# 只用root log 的弊端：
# 1、FileHandle 和 StreamHandle不能共存，使用不方便
# 2、不能配置多个FileHandle
#
# 1、root log 是所有日志实例的祖先
# 2、其他的日志实例通过logging.getLogger('logname')
# 3、子节点会继承root log 的所有属性
# 4、日志具有传递性，在子节点上写的日志，
# 则会传递给父亲节点写一次。
# 4、日志具有传递性，在子节点上写的日志，
# 若父节点有子节点额外添加之外的handler，则会传递给父亲节点写一次。
# 5、对于一个logger，可以设置filehandler和streamhandler
# 6、对于一个logger，可以设置Formatter

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s |%(filename)s|%(module)s |%(message)s|%(levelname)s',
    # filename= 'D:\\tmp\\log\\log98.log',
    # filemode='a+'
)

# logging.debug('debug log')
# logging.info('info log')
# logging.warning('warning')
# logging.error('error log')

log1 = logging.getLogger('log1')
log1.setLevel(logging.INFO)

fh = logging.FileHandler('D:\\tmp\\log\\log99.log')
sh = logging.StreamHandler()

fmt = logging.Formatter('%(asctime)s|%(name)s|%(filename)s|%(lineno)d|%(levelname)s|%(message)')
fh.setFormatter(fmt)
sh.setFormatter(fmt)
log1.addHandler(fh)
log1.addHandler(sh)

log2 = logging.getLogger('log1.log2')
log2.info('log2 info msg')
# log1.info('handle log test0827.txt')


# 习题：创建如下name的日志log1，log1.log2, log1.log2.log3，
# 给他们分别添加fh、sh，添加formatter，
# 需要显示时间、文件名、行号、日志name、级别、msg。
# 解释打印多行的情况
# log1:2个stream1个file
# log2:2个stream1个file
# log3 ：3个stream 2个file


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s|%(filename)s|%(lineno)d|%(levelname)s|%(message)s',
    # filename= 'D:\\tmp\\log\\log98.log',
    # filemode='a+'
)

# logging.debug('debug log')
# logging.info('info log')
# logging.warning('warning')
# logging.error('error log')

log1 = logging.getLogger('log1')
log1.setLevel(logging.INFO)

fh = logging.FileHandler('D:\\tmp\\log\\log99.log')
sh = logging.StreamHandler()

fmt = logging.Formatter('%(asctime)s|%(filename)s|%(lineno)d|%(levelname)s|%(message)s')
fh.setFormatter(fmt)
sh.setFormatter(fmt)

log1.addHandler(fh)
log1.addHandler(sh)
log1.info('log1 info msg')

log2 = logging.getLogger('log1.log2')
# log2.addHandler(fh)
# log2.addHandler(sh)
log2.info('log2 info msg')

log3 = logging.getLogger('log1.log2.log3')
log3.addHandler(fh)
log3.addHandler(sh)
log3.info('log3 info msg')


# 老师的方法：

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s|%(name)s|%(filename)s|%(lineno)d|%(levelname)s|%(message)s',
    # filename='e:\\tmp\\log\\log98.log',
)

log1 = logging.getLogger('log1')
log1.setLevel(logging.INFO)

fh = logging.FileHandler('e:\\tmp\\log\\log99.log')
sh = logging.StreamHandler()

fmt = logging.Formatter('%(asctime)s|%(name)s|%(filename)s|%(lineno)d|%(levelname)s|%(message)s')
fh.setFormatter(fmt)
sh.setFormatter(fmt)
log1.addHandler(fh)
log1.addHandler(sh)

log2 = logging.getLogger('log1.log2')
log2.info('log2 info msg')

log3 = logging.getLogger('log1.log2.log3')
log3.addHandler(fh)
log3.addHandler(sh)
log3.info('log3 info log')

# Filter


logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s|%(name)s|%(filename)s|%(lineno)d|%(levelname)s|%(message)s',
    # filename='e:\\tmp\\log\\log98.log',
)
fi = logging.Filter('log1.log2')#显示那个日志


log1 = logging.getLogger('log1')
log1.addFilter(fi)
log1.setLevel(logging.INFO)

fh = logging.FileHandler('D:\\tmp\\log\\log99.log')
sh = logging.StreamHandler()

fmt = logging.Formatter('%(asctime)s|%(name)s|%(filename)s|%(lineno)d|%(levelname)s|%(message)s')
fh.setFormatter(fmt)
sh.setFormatter(fmt)
log1.addHandler(fh)
log1.addHandler(sh)

log2 = logging.getLogger('log1.log2')
log2.addFilter(fi)
log2.info('log2 info msg')

log3 = logging.getLogger('log1.log2.log3')
log3.addHandler(fh)
log3.addFilter(fi)
log3.addHandler(sh)
log3.info('log3 info log')


log4 = logging.getLogger('log4')
log4.addFilter(fi)
log4.error('log4 error log')


# 打造日志系统：
# 1、一个main.py,4个模块文件
# 2、在main.py 中定义初始化日志函数initLog()，
# 目的是让root log既能写文件，也能在终端显示，且定义显示格式。
# 3、其他模块的日志name是文件名称
# 4、5个文件中都有函数，每个函数进入之后都会写日志，
# 在main.py的函数中调用其它4个模块的函数。
# 5、代码尽量优雅











