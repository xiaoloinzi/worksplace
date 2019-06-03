# encoding=utf-8
import socket

print u'创建一个TCP/IP的套接字'
tcpsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'TCP Socket created!'
print tcpsock

print u'创建一个UDP/IP的套接字：'
udpSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print "UDP Socket created!"
print udpSock
