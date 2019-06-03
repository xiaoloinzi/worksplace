# encoding=utf-8
from HTMLTestRunner import HTMLTestRunner
from calculator import Count
import unittest

class add_html(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_html(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)

    def tearDown(self):
        pass


if __name__=='__main__':

    testloader = unittest.TestLoader()
    suite = testloader.loadTestsFromTestCase(add_html('test_add_html'))
    fp = open('./r.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file('d:/test0827.txt.html','wb'),
                            title='加法测试结果报告',
                            description='用例执行情况',)
    runner.run(suite)
    fp.close()



