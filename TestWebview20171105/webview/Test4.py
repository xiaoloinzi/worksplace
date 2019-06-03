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
    def testBaidu(self):
        # #点击注册按钮
        # #1.查找注册按钮的控件id值
        # registerId="com.example.testWebview:id/registerBtn"
        # # 2.根据id值去找控件对象
        # registerIdObj = Common.find_element_by_id(self,registerId)
        # # 3.操作注册控件，这里的点击
        # registerIdObj.click()
        # # 4、查找姓名文本框的id值
        # nameText = '//*[@id=\"name\"]'
        # # 获取当前驱动
        # print self.driver.context
        # # 切换驱动
        # Common.find_context(self,'webview')
        # # 5、获取文本框对象
        # nameTextObje = Common.find_elements_by_xpath(self,nameText,0)
        # print nameTextObje
        # # 6、点击
        # nameTextObje.click()
        # # 7、输入注册名称
        # nameTextObje.send_keys("text")
        # # 输入密码
        # # 获取输入密码框的xpath
        # time.sleep(1)
        # regismima='//*[@id="pwd"]'
        # regismimaobject = Common.find_elements_by_xpath(self,regismima,0)
        # regismimaobject.send_keys('test')
        # time.sleep(1)
        # # 输入确认密码
        # quermima = '//*[@id="pwd1"]'
        # quermimaobject = Common.find_elements_by_xpath(self,quermima,0)
        # quermimaobject.send_keys('test')
        # # 选择性别
        # time.sleep(1)
        # Common.find_elements_by_xpath(self,'//*[@id="sexMan"]',0).click()
        # # 输入年龄
        # time.sleep(1)
        # Common.find_elements_by_xpath(self,'//*[@id="age"]',0).send_keys('12')
        # time.sleep(1)
        # Common.find_elements_by_xpath(self,'//*[@id="checkLike3"]',0).click()
        # time.sleep(1)
        # xuanz = Common.find_elements_by_xpath(self,'//*[@id="otherSelect"]',0)
        # xuanz.find_element_by_xpath("//*[@id=\"optionSelect4\"]").click()
        # registerBtn =  Common.find_elements_by_xpath(self,"//*[@id=\"register\"]")
        # print registerBtn.get_attribute("value")
        # print registerBtn.get_attribute("id")
        # registerBtn.click()
        # Common.find_context(self,'native')
        # registerBtn='android:id/button1'
        # registerBtnObj = Common.find_element_by_id(self,registerBtn)
        # registerBtnObj.click()
        # time.sleep(2)
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
        stranum = Common.find_element_by_id(self,'com.example.testWebview:id/textView')
        self.assertEqual(stranum.text,u'新闻列表信息')
        print stranum.text

        time.sleep(10)
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print "teardown"