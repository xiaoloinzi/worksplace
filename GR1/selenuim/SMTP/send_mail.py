# encoding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtpserver = 'smtp.qq.com'
# 发送邮箱用户名/密码
user = '1247636039@qq.com'
password = 'lchl1992'
# 发送邮箱
sender = '1247636039@qq.com'
# 接收邮箱
receiver = 'xiaoloinzi@163.com'
# 发送主题
subject = 'Python email test0827.txt'

# 编写HTML类型的邮件正文
msg=MIMEText('<html><h1>你好!</h1></html>','html','utf-8')
msg['subject'] = Header(subject,'utf-8')

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver,465)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()




















