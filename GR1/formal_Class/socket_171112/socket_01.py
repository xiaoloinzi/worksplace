# encoding=utf-8
'''
创建socket


UCP和TCP区别：UCP不会有accept（）这个过程，客户端不会和和服务端建立连接，而是直接建立连接
ucp:s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
问题1：该TCP通信方式时单线程还是多线程，服务端是否常驻？
答：单线程，不是常驻
问题2：修改部分代码，服务端修改为常驻模式，客户端发送10次请求，用单线程的方式实现
客户端进行for循环，服务端进行while True
问题3：此种处理方式，多个请求情况下，服务端是否并行处理
处理完一个再处理另外一个
问题4：修改部分代码，服务端修改为常驻模式，使服务端具备并行处理的能力，客户端发送10次请求（并行发送）
习题5：修改UDP该部分代码，服务端修改成常驻模式，使服务端具备并行处理的能力，客户端发送10次请求（并行发送）。


'''
import time,socket

while True:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port = 1235
    s.bind(('0.0.0.0',port))
    s.listen(5)
    connection,addir = s.accept()
    print connection,addir
    print 'got connection from ',addir
    try:
        # recv接收多少字节，指定长度
        buf = connection.recv(1024)
        print u'[%s]接收客户端数据：%s'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),buf)
        if buf == 'SR':
            connection.send('%s, welcome to server!'%buf)
        else:
            connection.send('%s,pls go out!'%buf)
    except Exception as err:
        print 'err msg:',err.message
    finally:
        connection.close()
s.close()










