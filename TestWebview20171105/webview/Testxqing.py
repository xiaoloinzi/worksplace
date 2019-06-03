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
    def testxq(self):
        '''
        webview自动化课后练习20171105
        在testwebview的app中使用用户名和密码登录系统，在系统中完成以下操作
        1.发布新闻
        新增新闻--
        1）点击新增按钮id com.example.testWebview:id/btnAdd
        2）输入标题：标题输入框id：com.example.testWebview:id/title
        3）输入内容：内容输入框id：com.example.testWebview:id/content
        4）点击确定：确定按钮id：com.example.testWebview:id/addOkBtn
        5）验证是否新增成功：获取列表标题id：com.example.testWebview:id/newsTitleText
        校验标题是否为输入的标题

        2.点击新闻显示详情
        1）点击标题查看详情：标题id：com.example.testWebview:id/newsTitleText
        2）获取发表发表评论按钮验证是否跳转到详情界面：
        按钮id：com.example.testWebview:id/suggestionBtn
        3）验证标题是否正确：标题id：com.example.testWebview:id/newsDetailTitleText
        4）验证内容是否正确，内容id：com.example.testWebview:id/newsDetailContentText

        3.对新闻进行评论，点击评论按钮，在页面中输入自己的评论并提交
        1）点击发表评论：评论按钮id：com.example.testWebview:id/suggestionBtn
        2）切换到webview驱动，并验证是否以切换
        3）输入内容，获取输入框的xpath路径：//*[@id="suggestInfo"]
        4）点击提交按钮，获取提交按钮的xpath路径：//*[@id="submitBtn"]
        5）切换驱动到app：
        6)点击确定，确定按钮ID：android:id/button1

        4.对提交的评论进行验证
        1）验证评论内容，评论内容Id：com.example.testWebview:id/newsSuggestText
        2）验证内容是否正确
        :return:
        '''
        print self.driver.context
        # 登陆操作
        deluid = 'com.example.testWebview:id/editText1'
        dlumimaid = 'com.example.testWebview:id/editText2'
        deluBtnid = 'com.example.testWebview:id/btn1'
        # 输入用户名
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
        biaoti = u'testtop'
        neirong = u'nei rong testtop'
        plnrong = u'shu ru neirong'
        Common.find_element_by_id(self,'com.example.testWebview:id/btnAdd').click()
        Common.find_element_by_id(self,'com.example.testWebview:id/title').set_value(biaoti)
        Common.find_element_by_id(self,'com.example.testWebview:id/content').set_value(neirong)
        Common.find_element_by_id(self,'com.example.testWebview:id/addOkBtn').click()
        biao = self.driver.find_elements_by_xpath('//android.widget.RelativeLayout/android.widget.TextView[@index=1]')
        print biao[-1].text
        self.assertTrue(biao[-1].text.startswith(u'标题：test'))
        biao[-1].click()
        biaoBtn = Common.find_element_by_id(self,'com.example.testWebview:id/suggestionBtn')
        self.assertEqual(biaoBtn.text,u'发表评论')
        biaot = Common.find_element_by_id(self,'com.example.testWebview:id/newsDetailTitleText')
        biaon = Common.find_element_by_id(self,'com.example.testWebview:id/newsDetailContentText')
        print biaot.text,' : ',biaon.text
        self.assertEqual(biaot.text,biaoti)
        self.assertEqual(biaon.text,neirong)
        biaoBtn.click()
        time.sleep(2)
        Common.find_context(self,'webview')
        print self.driver.context
        time.sleep(2)
        textarea = Common.find_elements_by_xpath(self,'//*[@id="suggestInfo"]',0)
        textarea.send_keys(plnrong)
        Common.find_elements_by_xpath(self,'//*[@id="submitBtn"]',0).click()
        Common.find_context(self,'native')
        print self.driver.context
        time.sleep(2)
        Common.find_element_by_id(self,'android:id/button1').click()
        plnr = Common.find_element_by_id(self,'com.example.testWebview:id/newsSuggestText')
        print plnr.text
        self.assertEqual(plnr.text,plnrong)
        time.sleep(5)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print "teardown"