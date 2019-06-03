# encoding=utf-8
import logging
import logging.handlers
import module4,module5,module2,module3




# 打造日志系统：
# 1、一个main.py,4个模块文件
# 2、在main.py 中定义初始化日志函数initLog()，
# 目的是让root log既能写文件，也能在终端显示，且定义显示格式。
# 3、其他模块的日志name是文件名称
# 4、5个文件中都有函数，每个函数进入之后都会写日志，
# 在main.py的函数中调用其它4个模块的函数。
# 5、代码尽量优雅

def initLog():
    logRoot = logging.getLogger()
    logRoot.setLevel(logging.DEBUG)
    fh = logging.FileHandler('D:\\tmp\\log98.log')
    sh = logging.StreamHandler()
    fmt = logging.Formatter('%(asctime)s|%(name)s|%(filename)s|%(lineno)d|%(levelname)s|%(message)s')
    rootlog = logging.getLogger()
    rootlog.setLevel(logging.DEBUG)

    fh = logging.handlers.RotatingFileHandler('D:\\tmp\\log0.log',maxBytes=5120,backupCount=3)
    sh = logging.StreamHandler()
    fmt = logging.Formatter('%(asctime)s|%(name)s|%(filename)s|%(lineno)d|%(levelname)s|%(message)s')
    fh.setFormatter(fmt)
    rootlog.addHandler(fh)
    rootlog.addHandler(sh)
    return rootlog

logRoot = initLog()
def funcMain():
    logRoot.info('execute funcMain begin')
    module2.fuc2()
    module3.fuc3()
    module4.fuc4()
    module5.fuc5()
    logRoot.info('execute funcMain end')
if __name__ == '__main__':
    funcMain()








# 1、在上述的日志系统中，使用RotatingFileHandle进行写日志
# 2、在t2.py中同时写两个日志文件



