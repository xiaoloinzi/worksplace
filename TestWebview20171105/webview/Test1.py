# encoding=utf-8
import sys,unittest,time
from appium import webdriver
from TestWebview20171105.webview import Common

default_encoding = "gb2312"
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding("gb2312")
class Test(unittest.TestCase):
    # define setup method
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '192.168.19.101:5555'
        desired_caps['appPackage'] = 'com.example.testWebview'
        desired_caps['appActivity'] = 'com.my.activity.MainActivity'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print "setup"
    def _testa(self):
        #点击注册按钮
        #1.查找注册按钮的控件id值
        registerId="com.example.testWebview:id/registerBtn"
        # 2.根据id值去找控件对象
        #registerIdObj = self.driver.find_element_by_id(registerId)
        registerIdObj = Common.find_element_by_id(self,registerId)
        # 3.操作注册控件，这里的点击
        registerIdObj.click()
        # 4、查找姓名文本框的id值
        nameText = '//*[@id=\"name\"]'
        # 获取当前驱动
        print self.driver.context
        # 获取所有驱动
        print self.driver.contexts
        # 切换驱动
        Common.find_context(self,'webview')#把需要的驱动封装为一个方法进行调用
         # 切换到WEBVIEW驱动
        # self.driver.switch_to.context(u"WEBVIEW_com.example.testWebview")
        # 5、获取文本框对象
        nameTextObje = Common.find_elements_by_xpath(self,nameText,0)
        print nameTextObje
        # 6、点击
        nameTextObje.click()
        # 在姓名框输入text（建议在输入之间点击并clear，清空输入框的默认提示），set_text('test')输入中文比较好用，
        # 但是注意新版本是否支持
        nameTextObje.send_keys("text3")
        #8.点击注册按钮
        # 使用浏览器的调试功能查找到xpath路径
        registerqueID='//*[@id="register"]'
        registerqueIDObje = Common.find_elements_by_xpath(self,registerqueID,0)
        # 点击
        registerqueIDObje.click()
        #9.点击弹出框中的确定按钮(切换到原生app驱动)
        # 打印当前的界面驱动
        print self.driver.context
        # 切换到原生app驱动
        Common.find_context(self,'native')
        # self.driver.switch_to.context(u"NATIVE_APP")
        # 在UI Automator Viewer中找到关闭弹出框确定ID
        registerBtn='android:id/button1'
        registerBtnObj = Common.find_element_by_id(self,registerBtn)
        registerBtnObj.click()
        # 切换驱动
        Common.find_context(self,'webview')
        # self.driver.switch_to.context(u"WEBVIEW_com.example.testWebview")
        # 10、输入密码
        # 获取输入密码框的xpath
        time.sleep(1)
        regismima='//*[@id="pwd"]'
        regismimaobject = Common.find_elements_by_xpath(self,regismima,0)
        regismimaobject.send_keys('test')
        time.sleep(1)
        # 11、输入确认密码
        quermima = '//*[@id="pwd1"]'
        quermimaobject = Common.find_elements_by_xpath(self,quermima,0)
        quermimaobject.send_keys('test')
        # 注册
        registerqueIDObje = Common.find_elements_by_xpath(self,registerqueID,0)
        # 点击注册按钮
        registerqueIDObje.click()
        # 确定保存
        Common.find_context(self,'native')
        # self.driver.switch_to.context(u"NATIVE_APP")
        # 在UI Automator Viewer中找到关闭弹出框确定ID
        registerBtn='android:id/button1'
        registerBtnObj = Common.find_element_by_id(self,registerBtn)
        registerBtnObj.click()
        #13.点击确定按钮回到登录界面
        shouye='com.example.testWebview:id/registerBtn'
        shouyeObj = Common.find_element_by_id(self,shouye)
        print shouyeObj.text
        #14.验证结果正确性
        self.assertEqual(shouyeObj.text,u'注册')
        # # 获取个列表进行验证所有的数据
        # list1 = [u'登录',u'重置',u'注册']
        # syou =u'//android.widget.Button'
        # syouobje = self.driver.find_elements_by_xpath(syou)
        # for i in xrange(len(syouobje)):
        #     print syouobje[i].text
        #     self.assertEqual(syouobje[i].text,list1[i])
        time.sleep(1)
        # 登陆操作
        deluid = 'com.example.testWebview:id/editText1'
        dlumimaid = 'com.example.testWebview:id/editText2'
        deluBtnid = 'com.example.testWebview:id/btn1'
        # s输入用户名
        deluobject = Common.find_element_by_id(self,deluid)
        deluobject.set_value('text')
        # 输入密码
        time.sleep(1)
        delummobject = Common.find_element_by_id(self,dlumimaid)
        delummobject.set_value('test')
        time.sleep(1)
        Common.find_element_by_id(self,deluBtnid).click()
        # 按返回按钮/键
        self.driver.keyevent(4)
        # 暂停下看下效果
        time.sleep(5)
        print "testa"
    def _testswithcontext(self):
        for i  in xrange(10):
            Common.find_context(self,'native')
            registerId="com.example.testWebview:id/registerBtn"
            registerIdObj = Common.find_element_by_id(self,registerId)
            registerIdObj.click()
            nameText = '//*[@id=\"name\"]'
            # 切换驱动
            Common.find_context(self,'webview')#把需要的驱动封装为一个方法进行调用
            time.sleep(2)
            nameTextObje = Common.find_elements_by_xpath(self,nameText,0)
            nameTextObje.click()
            nameTextObje.send_keys("text3")
            self.driver.keyevent(4)
    def testteacher(self):
        for i in range(10):
            # Common.switchContext(self,"native")
            time.sleep(2)
            self.driver.switch_to.context(u"NATIVE_APP")
            print self.driver.context
            time.sleep(2)
            Common.find_element_by_id(self,"com.example.testWebview:id/registerBtn").click()
            # Common.switchContext(self,"webview")
            time.sleep(2)
            self.driver.switch_to.context(u"WEBVIEW_com.example.testWebview")
            print self.driver.context
            time.sleep(2)
            Common.find_elements_by_xpath(self,"//*[@id=\"name\"]").send_keys("context")
            # Common.switchContext(self,"native")
            time.sleep(2)
            self.driver.keyevent(4)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print "teardown"