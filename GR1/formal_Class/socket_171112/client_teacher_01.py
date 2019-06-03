# encoding=utf-8
import time,socket,threading

ip = '127.0.0.1'
port = 1235
# for i in xrange(10):
#     time.sleep(0.5)
#     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     s.connect((ip,port))
#     s.send('SR')
#     print u'[%s]服务端返回数据:%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),s.recv(1024))
#     s.close()

def socketReq():
    time.sleep(0.5)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    s.send('SR')
    print u'[%s]服务端返回数据:%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),s.recv(1024))

    s.close()

for i in xrange(10):
    t = threading.Thread(target=socketReq)
    t.start()
