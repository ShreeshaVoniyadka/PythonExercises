import threading
import socket

host='127.0.0.1'
port = 50000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients=[]
nicknames=[]

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle(client):
    while(True):
        try:
            msg=client.recv(1024)
            broadcast(msg)
        except:
            index=client.index(client)
            clients.remove(client)
            nickname=nicknames[index]
            broadcast(f'{nickname} left the chat '.encode('ascii'))
            nicknames.remove(nickname)
            break

def recieve():
    while(True):
        client,address=server.accept()
        print(f"connected to the client : {str(address)}")
        client.send("nick".encode('ascii'))
        nickname=client.recv(1024).decode(nickname)
        client.append(client)

        print(f'nickname of the client {nickname}!')
        broadcast(f'{nickname} joined the room '.encode('ascii'))
        client.send("connected to the server".encode('ascii'))

        thread=threading.Thread(target=handle,args=(client,))
        thread.start()

recieve()