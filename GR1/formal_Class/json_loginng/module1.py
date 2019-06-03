# encoding=utf-8

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s '
           '|%(name)s'
           '|%(filename)s|'
           '%(module)s |%(message)s'
           '|%(levelname)s'
           '|%(funcName)s'
           '|%(lineno)d'
    # filename= 'D:\\tmp\\log\\modulelog1.log',
    # filemode='a+'
    )
logging.debug('debug log')
logging.info('info log')
logging.warning('warning')
logging.error('error log')

def func2():
    logging.debug('fun2 debug')


