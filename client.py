#!python3

import socket

HOST = 'localhost'
PORT = 8002

myFile = open('notok.jpg','rb')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))

#uso o b na frente para indicar que é do tipo byte
#sock.send(b'Sent')
sock.send(input('Enter file name: ').encode())
sock.send(myFile.read())

recv = sock.recv(1024).decode()
print(recv)

