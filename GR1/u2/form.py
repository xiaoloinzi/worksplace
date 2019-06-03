#!F:\Python27\python.exe
# encoding=utf-8

import cgi
print "Content-Type: text/html; charset=utf-8"
print ''
# header = 'Content-Type:text/html\n\n'
html = u'<h3>接受处理表单数据\n<\h3>'
# 打印返回的内容
# print header
print html
# 接受表单提交的数据
form = cgi.FieldStorage()
print u'接受表单get的数据：',form
print'<p/>'
# 解析处理提交的数据
content = form['text'].value
formhtml = '''''
<label for=''>you say:<\label><input type ="text" value="%s">
'''
print formhtml % (content)