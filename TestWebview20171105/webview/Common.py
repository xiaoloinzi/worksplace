#coding=gb2312
import sys
from time import sleep

default_encoding = "gb2312"
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding("gb2312")
    
#通过控件id每隔1秒查询一次控件，最大查询1分钟，超过一分钟后查询失败
def find_element_by_id(self,resourceId):
    idObj=''
    count = 1
    while (count <= 60):
        sleep(1)
        try:
            idObj = self.driver.find_element_by_id(resourceId)
        except Exception as errorMsg:
            print str(errorMsg)
            count=count +1
            continue
        break
    return idObj
#通过控件路径每隔2秒查询一次控件，最大查询1分钟，超过一分钟后查询失败
def find_elements_by_xpath(self,xpath,index=0):
    xpathObj=''
    count = 1
    while (count <= 30):
        sleep(2)
        try:
            xpathObj = self.driver.find_elements_by_xpath(xpath)
        except Exception as errorMsg:
            print str(errorMsg)
            print 'waiting for finding element'+xpath
            count=count +1
            continue
        break
    try:
        if(len(xpath) > 1):
            return xpathObj[index]
    except Exception as errorMsg:
        return xpathObj

# 通过控件路径每隔2秒查询一次控件，最大查询1分钟，超过一分钟后查询失败,查询控件的数量
def find_elementsCount_by_xpath(self, xpath):
    xpathObj = ''
    count = 1
    while (count <= 30):
        sleep(2)
        try:
            xpathObj = self.driver.find_elements_by_xpath(xpath)
        except Exception as errorMsg:
            print str(errorMsg)
            print 'waiting for finding element' + xpath
            count = count + 1
            continue
        break
    xpathObj = len(xpathObj)
    return xpathObj
#通过控件路径每隔2秒查询一次控件，最大查询1分钟，超过一分钟后查询失败，根据文本来获取
def find_elements_by_xpath_text(self,xpath,text):
    xpathObj=''
    count = 1
    while (count <= 30):
        sleep(2)
        try:
            xpathObj = self.driver.find_elements_by_xpath(xpath)
        except Exception as errorMsg:
            print str(errorMsg)
            print 'waiting for finding element'+xpath
            count=count +1
            continue
        break
    try:
        if(len(xpath) > 1):
            for element in xpathObj:
                if element.text == text.decode('GBK'):
                    print str(text)
                    print str(element.text)
                    return element
        else:
            return  xpathObj
    except Exception as errorMsg:
        print errorMsg
        return xpathObj

def find_elements_by_xpath_texts(text):
    print text

# 练习：自己编写一个公共函数，实现context切换，
# 输入参数：切换到哪里（native/webview）
# 如果输入native，就需要将驱动切换到native
# 如果输入webview，就需要将驱动切换到webivew

def find_context(self,drivername):
    sleep(1)
    try:
        if drivername=='native':
            print self.driver.context
            self.driver.switch_to.context(u"NATIVE_APP")
        if drivername=='webview':
            print self.driver.context
            self.driver.switch_to.context(u"WEBVIEW_com.example.testWebview")
    except Exception,e:
        print e

if __name__=="__main__":
    
    find_elements_by_xpath_texts("中国人")