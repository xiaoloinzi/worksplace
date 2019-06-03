# encoding=utf-8
from calculator import Count

class TestCount():

    def test_add(self):
        try:
            j = Count(2,2)
            add = j.add()
            assert(add==5),u"test不通过"
        except AssertionError as msg:
            print msg
        else:
            print u'测试通过'

mytest = TestCount()
mytest.test_add()

