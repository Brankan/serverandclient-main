import socket
from common import*

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ip_connection)

send_data(s, "BLABLA asadad")