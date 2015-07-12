#!/usr/bin/python

import time
import socket
import _thread as thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 5024))
sock.listen(5)

def server_thread(client_sock):
    sock_file_w = client_sock.makefile('w')
    sock_file_r = client_sock.makefile('r')
    filename = sock_file_r.readline()[:-1]
    
    client_sock.close()
while True:
    client_sock, addr = sock.accept()
    thread.start_new_thread(server_thread, (client_sock,))
    print('Client connected to source control: <' + str(addr) + '>')