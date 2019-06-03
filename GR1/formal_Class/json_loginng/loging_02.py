# encoding=utf-8
import logging
import logging.handlers
import logging.config
from datetime import datetime
# 日志模块

rootlog = logging.getLogger()
rootlog.setLevel(logging.DEBUG)
# backupCount=日志文件的个数
fh = logging.handlers.RotatingFileHandler('D:\\tmp\\log\\log79.txt',maxBytes=512,backupCount=3)
fmt = logging.Formatter('%(asctime)s|%(name)s|%(filename)s|%(lineno)d|%(levelname)s|%(message)s')
fh.setFormatter(fmt)
rootlog.addHandler(fh)

for i in xrange(1000):
    rootlog.info('this is test0827.txt log')

#
# logging.config.cfg.fileConfig('D:\\tmp\\log\\log.config.cfg')
# logger1 = logging.getLogger('t2')
# logger1.debug('this is a debug t2 log')
#
#
#
#
# # 基于log.config.cfg，添加一个日志t3，只用在streamHandler中显示
# # 修改配置文件log.config.cfg
# logger2 = logging.getLogger('t3')
# logger2.debug('this is a debug t3 log')










