import socket
import random
import os


def bruh():
    serv1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv1.bind(('localhost', 1001))
    serv1.listen(5)
    
    def fun():
        while True:
            global b
            conn1, addr = serv1.accept()
            f =open('server1.py','r')
            g=f.read()
            f.close()
            b=random.randint(1,9999)
            conn1.send(str(b).encode())
            serv1.close()
            
            name='server'+str(b)+'.py'
            name=str(name)
            print(b)
            p=open(name,'w')
            p.write(str(g))
            p.close()
            os.startfile(name)
            
            print('yes')
            serv10 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('yesconnect')
            serv10.connect(('localhost', 1002))
            serv10.send(str(b).encode())
            serv10.close()
            break
    fun()
    

while True:
    bruh()    


