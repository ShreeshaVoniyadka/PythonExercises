import socket
import threading
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',50000))
nickname=input("choose a nickname(password):  ")

def recieve():
    while(True):
        try:
            msg=client.recv(1024).decode('ascii')
            if msg=='nick':
                client.send(nickname.encode('ascii'))

            else:
                print(msg)
        except:
            print('no response')
            client.close()
            break
def write():
    while True:
        msg=f'{nickname}:{input("")}'
        client.send(msg.encode('ascii'))

recieve_thread=threading.Thread(target=recieve)
recieve_thread.start()
