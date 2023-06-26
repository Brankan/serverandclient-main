import socket
import random

def bruh():
    serv1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv1.bind(('192.168.124.232', 1000))
    serv1.listen(5)
    def fun():
        while True:
            global b
            conn1, addr = serv1.accept()
            b=random.randint(1,9999)
            conn1.send(str(b).encode())
            print('yes connect')
            conn1.close()
            break
    fun()
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('localhost', b))
    serv.listen(5)
    
    users=['oles:pass','mtt:user']
    
    login=False
    while True:
        conn, addr = serv.accept()
        from_client = ''
        while True:  
            data = conn.recv(4096)
            if not data: break
            from_client += data.decode()
            if from_client =='LOGIN':
                conn.send(b'Type login:\r\n\r\n')
                logindata = conn.recv(4096)
                conn.send(b'Type pass:\r\n\r\n')
                passdata = conn.recv(4096)
                al=logindata.decode()+":"+passdata.decode()
                for k in users:
                    if k ==al:
                        conn.send(b'Welcome,to see secret info,type SECRET,to close connect type CLOSE\r\n\r\n')
                        login=True
                if login==False:
                    conn.send(b'wrong pass or login\r\n\r\n')
            elif from_client =='SECRET':
                if login==True:
                    conn.send(b'This is Secret!\r\n\r\n')
                if login==False:
                    conn.send(b'wrong command\r\n\r\n')
            elif from_client=='CLOSE':
                    conn.send(b'stopconnect\r\n\r\n')
                    conn.close()
                    return ''
            elif from_client=='HELP':
                conn.send(b'COMMANDS:LOGIN,CLOSE,HELP\r\n\r\n')
            else:
                conn.send(b'wrong command\r\n\r\n')
            from_client = ''
                       

while True:
    bruh()
