# coding=UTF-8

from socket import *

tcp_server_socket = socket(AF_INET, SOCK_STREAM)

address = ('127.0.0.1', 7788)

tcp_server_socket.bind(address)

tcp_server_socket.listen(128)

client_socket, clientAddr = tcp_server_socket.accept()


recv_data = client_socket.recv(1024)  
print('receive:', recv_data)


client_socket.send("thank you !") #


client_socket.close()

