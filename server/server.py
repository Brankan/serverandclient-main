import socket
from _thread import *
from common import *
from time import sleep


 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
s.connect(('localhost', 56789))

#s.sendall  "CONNECT\r\n\r\n"

#s.recv  wyswietl na ekranie

s.close()


s.sendall('GET /html HTTP/1.1\r\nHost: httpbin.org\r\n\r\n'.encode('utf-8'))
 
data = b''
 
while b'\r\n\r\n' not in data:
    data += s.recv(100)
 
contentlength = int(data.decode('utf-8').split('Content-Length: ')[1].split('\r\n')[0])
 
header_length = len(data.decode('utf-8').split('\r\n\r\n')[0])
 
while len(data) < contentlength + header_length:
    data += s.recv(100)
 
data = data.decode('utf-8')
 
print(data.split('\r\n\r\n')[0])
 
html = data.split('\r\n\r\n')[1]
 
with open('index.html', 'w') as f:
    f.write(html)
 
print("SAVED TO INDEX.HTML")
