# encoding=utf-8
import time,socket,threading
def sock():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = '127.0.0.1'
    port = 1235
    s.connect((ip,port))
    s.send('SR')
    print u'[%s]服务端返回数据：%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),s.recv(1024))
    s.close()

for i in xrange(10):
    t = threading.Thread(target=sock)
    t.start()
    time.sleep(1)

