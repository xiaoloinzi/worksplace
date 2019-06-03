# encoding=utf-8

import time

def find_element(driver,idOrXpath,n=10):
    for i in xrange(n):
        try:
            if idOrXpath.startswith('/'):
                ret = driver.find_element_by_xpath(idOrXpath)
            else:
                ret = driver.find_element_by_id(idOrXpath)
            return ret
        except Exception as err:
            print err.message
            time.sleep(2)
    raise Exception('element %s could not be found'%idOrXpath)



