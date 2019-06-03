# encoding=utf-8
import logging

log1 = logging.getLogger('module2')
def printmodule2():
    fh = logging.FileHandler('D:\\tmp\\log\\m2.log')
    log1.addHandler(fh)
    log1.info('begain module2 info')
    print 'print module2'
    log1.info('end module2 info')










