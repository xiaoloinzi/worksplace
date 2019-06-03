# encoding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver

class Youdao(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(10)
        self.base_url='http://www.youdao.com/'


    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("translateContent").send_keys("http test0827.txt runner")
        driver.find_element_by_id("translateContent").submit()

    def tearDown(self):
        pass

if __name__=='__main__':

    testsuite = unittest.TestSuite()
    testsuite.addTest(Youdao('test_youdao'))
    # 定义存放文件的路径
    fp = open('result.html','wb')
    runner = HTMLTestRunner(stream=fp,
                            title='有道翻译测试报告',
                            description='用例执行情况')
    runner.run(testsuite)
    fp.close()