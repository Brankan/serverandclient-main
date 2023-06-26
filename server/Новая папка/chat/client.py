# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:57:11 2021

@author: student
"""

import socket
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect(('localhost', 1000))
while True:
    a=input('0:')
    client1.send(a.encode())
    from_server=''
    while True:
        from_server += client1.recv(4096).decode()
        print(from_server)
        if from_server =='stopconnect':
            break