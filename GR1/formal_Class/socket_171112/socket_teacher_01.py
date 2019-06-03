# encoding=utf-8
import time,socket,threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 1235
s.bind(('0.0.0.0',port))
s.listen(5)


def replayHandler(conn):
    try:
        buf = conn.recv(1024)
        print u'[%s]接受客户端数据:%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),buf)
        if buf == 'SR':
            conn.send('%s, welcome to server!'%buf)
        else:
            conn.send('%s, pls go out!'%buf)
    except Exception as err:
        print 'err msg:',err.message
    finally:
        conn.close()

while True:
    connection,addr = s.accept()
    print connection,addr
    print 'got connection from ',addr
    t = threading.Thread(target=replayHandler,args=(connection,))
    t.start()

    # try:
    #     buf = connection.recv(1024)
    #     print u'[%s]接受客户端数据:%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),buf)
    #     if buf == 'SR':
    #         connection.send('%s, welcome to server!'%buf)
    #     else:
    #         connection.send('%s, pls go out!'%buf)
    # except Exception as err:
    #     print 'err msg:',err.message
    # finally:
    #     connection.close()
s.close()
