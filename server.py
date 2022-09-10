#!python3

import socket

HOST = 'localhost'
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

sock.listen(5)
while True:
    newSock, _ = sock.accept()
    #msg = newSock.recv(1024).decode()
    #print(msg)
    #newSock.send(b'Received')

    #Agora enviar arquivos
    fileName = newSock.recv(1024).decode()
    newFile = newSock.recv(100000000)
    with open(f'files/{fileName}.jpg', 'wb') as fi:
        fi.write(newFile)
    
    newSock.send(b'ok')
