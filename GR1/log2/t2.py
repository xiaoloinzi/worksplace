# encoding=utf-8
import logging
import logging.handlers
from common import log
logger = logging.getLogger('t2')
fh2 = logging.handlers.RotatingFileHandler('e:\\tmp\\log\\log92.log',maxBytes=1024,backupCount=3)
fmt = logging.Formatter('%(asctime)s|%(name)s|%(filename)s|%(lineno)d|%(levelname)s|%(message)s')
fh2.setFormatter(fmt)
logger.addHandler(fh2)
@log(logger)
def func2():
    a = 1+2
