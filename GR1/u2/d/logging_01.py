# encoding=utf-8
import logging
import module,module1,module2,module3,module4
import logging.handlers
# 习题：自定义一个格式的输出日志，包括时间、调用日志输出模块的文件名
# 当前执行程序的程序名、日志级别、日志内容，级别是debug级别，写入日志文件
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s|%(filename)s|%(module)s|'
#            '%(levelname)s|%(message)s',
#     filename='D:\\tmp\\log\\newlog.log'
# )
#
# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')


# 习题：有两个py文件，其中main.py会使用module.py中的方法
# 两个py文件中，在进入方法时，都会写日志，要求包含如下的日志内容
# ：时间、日志名称、调用日志输出函数的模块文件名
# 行号、当前执行程序的程序名，日志级别、日志内容、rhino级别是debug级别
# logging.basicConfig(
#         level=logging.DEBUG,
#         format='%(asctime)s|'
#                '%(name)s|'
#                '%(filename)s|'
#                '%(lineno)d|'
#                '%(module)s|'
#                '%(levelname)s|'
#                '%(funcName)s|'
#                '%(message)s|',
#         filename='D:\\tmp\\log\\ninelog.log'
#     )
#
# def printmain():
#     module.printlogging()
#
#     print u'main func'
#     logging.info('info')
#     logging.debug('debug')
#
# if __name__=='__main__':
#     printmain()
#
# 习题：创建如下name的日志log1，log1.log2,log1.log2.log3,给他们
# 分别添加fh\sh,添加formatter，需要显示时间、文件名、日志name，级别，msg
# 解释打印多行的情况


# logging.basicConfig(
#         level=logging.DEBUG,
#         format='%(asctime)s|'
#                '%(name)s|'
#                '%(filename)s|'
#                '%(lineno)d|'
#                '%(module)s|'
#                '%(levelname)s|'
#                '%(funcName)s|'
#                '%(message)s|',
#         # filename='D:\\tmp\\log\\ninelog.log'
#     )
# log1 = logging.getLogger('log1')
# log1.setLevel(logging.DEBUG)
# fh = logging.FileHandler('D:\\tmp\\log\\deng1.log')
# sh = logging.StreamHandler()
# fmt = logging.Formatter('%(asctime)s|'
#                '%(name)s|'
#                '%(filename)s|'
#                '%(lineno)d|'
#                '%(module)s|'
#                '%(levelname)s|'
#                '%(funcName)s|'
#                '%(message)s|')
# log1.addHandler(fh)
# log1.addHandler(sh)
# fh.setFormatter(fmt)
# sh.setFormatter(fmt)
#
# log1.info('log1 info')
#
#
# log2 = logging.getLogger('log1.log2')
# log2.info('log2 info')
#
#
# log3 = logging.getLogger('log1.log2.log3')
# log3.addHandler(fh)
# log3.addHandler(sh)
# log3.info('log3 info')


#打造日志系统：
# 1、一个main.py,4个模块文件
# 2、在main.py 中定义初始化日志函数initLog()，
# 目的是让root log既能写文件，也能在终端显示，且定义显示格式。
# 3、其他模块的日志name是文件名称
# 4、5个文件中都有函数，每个函数进入之后都会写日志，
# 在main.py的函数中调用其它4个模块的函数。
# 5、代码尽量优雅


# def initLog():
#     # logging.basicConfig(
#     #     level=logging.DEBUG,
#     #
#     # )
#     logroot = logging.getLogger()
#     fh = logging.FileHandler('D:\\tmp\\log\\rizhilog.log')
#     sh = logging.StreamHandler()
#     fmt = logging.Formatter('%(asctime)s|'
#                '%(name)s|'
#                '%(filename)s|'
#                '%(lineno)d|'
#                '%(module)s|'
#                '%(levelname)s|'
#                '%(funcName)s|'
#                '%(message)s|')
#     sh.setFormatter(fmt)
#     fh.setFormatter(fmt)
#     logroot.addHandler(fh)
#     logroot.addHandler(sh)
#     return logroot
#
#
# logroot = initLog()
# def funMain():
#     logroot.info('begain funcMain info')
#     module1.printmodule1()
#     module2.printmodule2()
#     module3.printmodule3()
#     module4.printmodule4()
#     logroot.info('end funcMain info')
#
#
#
# if __name__=='__main__':
#     funMain()

# 1、在上述的日志系统中，使用RotatingFileHandle进行写日志
# 2、在t2.py中同时写两个日志文件

def initLog():
    logroot = logging.getLogger()
    fh = logging.handlers.RotatingFileHandler('D:\\tmp\\log\\rizhi.log',maxBytes=1024,backupCount=5)
    fmt = logging.Formatter('%(asctime)s|'
               '%(name)s|'
               '%(filename)s|'
               '%(lineno)d|'
               '%(module)s|'
               '%(levelname)s|'
               '%(funcName)s|'
               '%(message)s|')

    fh.setFormatter(fmt)
    logroot.addHandler(fh)
    return logroot


logroot = initLog()
def funMain():
    logroot.info('begain funcMain info')
    module1.printmodule1()
    module2.printmodule2()
    module3.printmodule3()
    module4.printmodule4()
    logroot.info('end funcMain info')



if __name__=='__main__':
    funMain()