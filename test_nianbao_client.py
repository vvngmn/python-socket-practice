# _*_coding:utf-8_*_
__author__ = 'nickchen121'
import socket
BUFSIZE = 1024
ip_port = ('127.0.0.1', 8080)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = s.connect_ex(ip_port)

s.send('hello'.encode('utf-8')) # b'hello'
s.send('feng'.encode('utf-8'))
