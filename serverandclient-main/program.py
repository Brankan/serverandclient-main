from function import chat1
chat1()
"""
komenda = "LOGIN\r\nmkozlowski\r\nLublin2021!dsa\r\n\r\n"

users = {'mkozlowski': 'Lublin2021!'}

parametry = komenda.split('\r\n')

if parametry[1] in users and users[parametry[1]] == parametry[2]:
    print("zalogowany")
else:
    print("bledny login")#


  print('YEEESSSS')
                            conn, addr = serv.accept()
                            from_client1 = ''
                            while True:  
                                data1 = conn.recv(4096)
                                print('YEEESSSS22222')
                                if not data: break
                                from_client1 += data1.decode()
                                if from_client1 =='CloseCon':
                                    break
                                chat=open('chat.txt','a')
                                chat.write(from_client1+'\n')
                                print(chat.read(),from_client1,'here')
                                chat.close()
                                conn.send(b'\r\n\r\n')
                                
                        break"""