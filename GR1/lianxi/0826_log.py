# encoding=utf-8
import logging
import log_0826_01


logging.basicConfig(
    level=logging.DEBUG,
    format = '%(asctime)s %(filename)s [line:%(lineno)d] %(message)s',
    filename='D:/tmp/test0827.log',
)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

def mainprint():
    log_0826_01.add()
    print 'mainprint'
    logging.debug('0826_log debug message')

if __name__=="__main__":
    mainprint()


















