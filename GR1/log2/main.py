# encoding=utf-8
import logging
import logging.handlers
import t1,t2,t3,t4
from common import log,initLog

logger = initLog()

@log(logger)
def funcMain():
    t1.func1()
    t2.func2()
    t3.func3()
    t4.func4()
if __name__ == '__main__':
    funcMain()







