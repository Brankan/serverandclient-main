# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:55:51 2021

@author: student
"""
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(('localhost', 1000))
client.listen(5)
while True:
    a=input('0:')
    client.send(a.encode())
    from_server=''
    while True:
        from_server += client.recv(4096).decode()
        print(from_server)
        if from_server =='stopconnect':
            break




