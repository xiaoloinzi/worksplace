# encoding=utf-8
import module2,module3,module4,module5
import logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s |'
#            '%(name)s'
#            '%(filename)s|'
#            '%(module)s |%(message)s'
#            '|%(levelname)s'
#            '|%(funcName)s'
#            '|%(lineno)d'
    # filename= 'D:\\tmp\\log\\mainlog1.log',
    # filemode='a+'
# )#设置显示日志的级别
# 不设置的情况下，只显示error和waring
# 日志的级别
# CRITICAL>ERROR >WARNING>INFO>DEBUG>NOTEST

logging.debug('debug log')
logging.info('info log')
logging.warning('warning')
logging.error('error log')


# 习题2：有两个py文件，其中main.py
# 会使用module1.py中的方法，两个py文件中，
# 在进入方法时，都会写日志，要求包括如下的
# 日志内容：时间、日志名称、调用日志输出函数的
# 模块的文件名、行号、当前执行程序的程序名、
# 日志级别、日志内容，日志级别是debug级别
# def func1():
#     logging.debug('func1 debug')
#     module1.func2()
#
#
#
# if __name__=='__main__':
#     func1()




