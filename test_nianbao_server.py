# _*_coding:utf-8_*_
# https://www.cnblogs.com/zhouxuchong/p/11576275.html
# 服务器接受数据粘包栗子：

__author__ = 'nickchen121'
from socket import *
ip_port = ('127.0.0.1', 8080)

TCP_socket_server = socket(AF_INET, SOCK_STREAM)
TCP_socket_server.bind(ip_port)
TCP_socket_server.listen(5)

conn, addr = TCP_socket_server.accept()

data1 = conn.recv(2) # receive 2 Bytes at one time 
data2 = conn.recv(10)

print('----->', data1.decode('utf-8'))
print('----->', data2.decode('utf-8'))

conn.close()