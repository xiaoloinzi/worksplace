# encoding=utf-8
import logging
import log_0826_01

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s'
           '%(filename)s'
           '[line:%(lineno)d'
           '%(levelname)s'
           '%(message)s',
    datefmt= '%Y-%m-%d %H:%M:%S',
    filename= 'D:\\tmp\\log.log',
    filemode='a'
)


console = logging.StreamHandler()
confile = logging.FileHandler('D://tmp//filelog.log')
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)2s | %(filename)s| %(funcName)s | %(levelname)-5s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
console.setFormatter(formatter)
confile.setFormatter(formatter)
logging.getLogger().addHandler(console)
logging.getLogger().addHandler(confile)



def prints():
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.error('error message')
    logging.critical('critical message')
    log_0826_01.add()
    print 'message'

if __name__=="__main__":
    prints()

















