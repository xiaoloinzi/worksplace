# encoding=utf-8
import logging
# 写文件的时候，最后一次配置会覆盖之前的配置，所以，会写在最后一个文件中
logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s|'
               '%(name)s|'
               '%(filename)s|'
               '%(lineno)d|'
               '%(module)s|'
               '%(levelname)s|'
               '%(funcName)s|'
               '%(message)s|',
        # filename='D:\\tmp\\log\\ninelog1.log'
    )
def printlogging():

    print u'module func'
    logging.warning('warning')
    logging.error('error')
    logging.info('info')
    logging.debug('debug')
