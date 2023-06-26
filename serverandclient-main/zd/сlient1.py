import socket
import time
client10 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client10.connect(('localhost', 1001))
data = client10.recv(4096)
client10.close()
time.sleep(10)
print(data.decode())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', int(data.decode())))
while True:
    a=input('0:')
    client.send(a.encode())
    from_server=''
    while True:
        from_server += client.recv(4096).decode()
        if '\r\n\r\n' in from_server:
            print(from_server)
            break
    if from_server =='stopconnect\r\n\r\n':
        break
