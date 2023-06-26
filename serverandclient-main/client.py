import socket
from common import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ip_connection)


#LOGIN
login = input("Podaj login\n")
password = input("Podaj haslo\n")

send_data(s, f"LOGIN\r\n{login}\r\n{password}\r\n\r\n")
data = get_data(s)

print(data)
status_code, status_message, data = get_split_response(data)

session_id = ''
if status_code == 200:
    session_id = data
    print("Zalogowalem sie")

    #TODO: Obsluga chatu
    command = input("Co chcesz zrobic? Wyjscie to q\n")
    while command != 'q':

        send_to = input("Do kogo wyslac wiadomosc\n")
        message = input("Podaj wiadomosc\n")
        send_data(s, f"SEND\r\n{send_to}\r\n{message}\r\nsession_id:{session_id}\r\n\r\n")
        data = get_data(s)
        
        status_code, status_message, data = get_split_response(data)
        print(status_message, data)
        

        command = input("Co chcesz zrobic? Wyjscie to q\n")
else:
    print("Bład!",status_message, data)

# send_data(s, f"QUIT\r\nsession_id: {session_id}\r\n\r\n")
# data = get_data(s)

s.close()
