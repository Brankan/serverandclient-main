import time
import os
clear = lambda: os.system('cls')
clear()


while True:

    chat=open('chat.txt','r')
    print(chat.read())
    chat.close()
    time.sleep(1)
    clear()


    