import socket
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect(('192.168.124.232', 1000))
data = client1.recv(4096)
client1.close()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.124.232', int(data.decode())))
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
