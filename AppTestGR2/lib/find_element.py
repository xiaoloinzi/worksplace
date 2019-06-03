# encoding=utf-8
import time

# 定义一个方法，可以统一管理是否找到控件
def find_element(driver,idorXpath,n=10):
    for i in xrange(n):
        try:
            if idorXpath.startswith('/'):
                ret = driver.find_element_by_xpath(idorXpath)
            else:
                ret = driver.find_element_by_id(idorXpath)
            return ret
        except Exception as err:
            print err.message
            time.sleep(2)
    raise Exception('element %s could not be found '%idorXpath)