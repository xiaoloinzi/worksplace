# encoding=utf-8
import logging

def initLog():
    logRoot = logging.getLogger()
    logRoot.setLevel(logging.DEBUG)
    # fh = logging.FileHandler('e:\\tmp\\log\\log98.log')
    fh = logging.handlers.RotatingFileHandler('e:\\tmp\\log\\log91.log',maxBytes=1024,backupCount=3)
    sh = logging.StreamHandler()
    fmt = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s')
    fh.setFormatter(fmt)
    sh.setFormatter(fmt)
    logRoot.addHandler(fh)
    logRoot.addHandler(sh)
    return logRoot

def log(logger):
    def log(func):
        def wrapper(*args,**kwargs):
            logger.info('execute '+func.__name__ +' begin')
            ret = func(*args,**kwargs)
            logger.info('execute '+func.__name__+' end')
            return ret
        return wrapper
    return log


