import socket
from function import chat1,users


def bruh():

    serv1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv1.bind(('localhost', 1002))
    serv1.listen(5)
    print('yesconnect')

    conn1, addr = serv1.accept()
    b =conn1.recv(4096).decode()
    serv1.close()
    print(b)
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('localhost', int(b)))
    serv.listen(5)
    
    loginname=''
    login=False
    Chated=False
    while True:
        conn, addr = serv.accept()
        from_client = ''
        while True:  
            data = conn.recv(4096)
            if not data: break
            from_client += data.decode()
            if Chated==True:
                if from_client=='CloseC':
                    Chated=False
                    conn.send(b'\r\n\r\n')
                    from_client=''
                    print('close')
                print('yas')
                chat=open(r'chat.txt','a')
                chat.write(loginname+":"+from_client+'\n')
                chat.close()
                conn.send(b'\r\n\r\n')
            
            
                
            elif from_client =='LOGIN':
                conn.send(b'Type login:\r\n\r\n')
                logindata = conn.recv(4096)
                conn.send(b'Type pass:\r\n\r\n')
                passdata = conn.recv(4096)
                al=logindata.decode()+":"+passdata.decode()
                for k in users:
                    if k ==al:
                        conn.send(b'Welcome,to close connect type CLOSE\r\n\r\n')
                        login=True
                        loginname=logindata.decode()
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
                conn.send(b'COMMANDS:LOGIN,CLOSE,HELP,REGISTER,CHAT,SENDMAIL\r\n\r\n')
            elif from_client=='CHAT':
                    if login ==True:
                        chat1()
                        Chated=True
                        conn.send(b'Connected\r\n\r\n')


                    else: 
                        conn.send(b'You are not logged in\r\n\r\n')

            elif from_client=='REGISTER':
                conn.send(b'Type login:\r\n\r\n')
                logindataa = conn.recv(4096)
                conn.send(b'Type pass:\r\n\r\n')
                passdataa = conn.recv(4096)
                al=logindataa.decode()+":"+passdataa.decode()
                users.append(al)
                conn.send(b'account added\r\n\r\n')
                
            elif from_client=='SENDMAIL':
                if login ==True:
                    conn.send(b'Type name:\r\n\r\n')
                    namedata = conn.recv(4096)
                    conn.send(b'Type email:\r\n\r\n')
                    email = conn.recv(4096)
                    conn.send(b'email sent\r\n\r\n')
                    aem=str(namedata.decode())+','+"from: "+str(loginname)+" text:"+str(email.decode())+','
                    aem=str(aem)
                    email=open('emails.txt','a')
                    email.write(aem)
                    email.close()
                else:
                    conn.send(b'You are not logged in\r\n\r\n')
            
            elif from_client == 'CHECKMAIL':
                if login==True:
                    email=open('emails.txt','r')
                    g=email.read()
                    email.close()
                    g=str(g)
                    t=g.split(',')
                    bn=0
                    print(t)
                    mails=''
                    for bt in t:
                        bn+=1
                        if bt==loginname:
                            mails+=str(t[bn]+'\n')
                    conn.send(mails.encode()+b'\r\n\r\n')
                else:
                    conn.send(b'You are not logged in\r\n\r\n')

            else:
                conn.send(b'wrong command\r\n\r\n')
            from_client = ''
                       

bruh()


